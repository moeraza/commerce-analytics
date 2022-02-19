import pandas as pd
from core.utils import convert_time_stamp
from core.log import *

def visit_dates(df_combined):
    '''
        A visit can include any interaction type (RemoveFromCart', 'ProductView', 'AddToCart' or 'Purchase), 
        therefore no need to remove any data points, simply min/max of date visit time
    '''
    logging.info('Starting to build visit date features')
    df = df_combined.groupby('user_id').agg({'interaction_time':['min','max']}).droplevel(axis=1, level=0).reset_index()
    df = df.rename({'min':'first_visit_date', 'max':'last_visit_date'}, axis=1)
    logging.info('Done building visit date features')
    return df



def avg_gap_between_vists(df_combined):
    '''
        Assumption here is that every user does not visit the website more then once an hour
        so we will take the first timestamp of every hour that the user logs on, and find the gaps there
    '''
    logging.info('Starting to build gap between visit feature')
    df = df_combined[['user_id','interaction_time']]
    del df_combined
    df['interaction_day'] = df.interaction_time.str[:13]
    df = df.groupby(['user_id','interaction_day']).agg({'interaction_time':'min'}).reset_index().drop('interaction_day',axis=1)
    df['interaction_time']  = pd.to_datetime(df.interaction_time)
    df = df.sort_values(by=['user_id','interaction_time'], ascending=True)
    df['visit_diff_seconds'] = df.groupby('user_id')['interaction_time'].diff().dt.total_seconds()
    df['visit_diff_seconds'] = df.visit_diff_seconds.fillna(-1)
    
    # Remove Nulls and 0's
    df = df[(df.visit_diff_seconds != 0) & (df.visit_diff_seconds != -1)]
    df = df.groupby('user_id').agg({'visit_diff_seconds':'mean'}).reset_index()
    
    # Convert from seconds to X days HH:MM:SS
    df['avg_gap_between_visits'] = df.apply(lambda x: convert_time_stamp(x['visit_diff_seconds']), axis=1)
    df = df.drop('visit_diff_seconds', axis=1)
    logging.info('Done building gap between visit feature')
    return df

def avg_monthly_spend(df_combined):
    logging.info('Starting to build avg monthly spend feature')
    df_combined = df_combined[df_combined.interaction_type=='Purchase']
    df = df_combined[['user_id','interaction_time', 'price']]
    del df_combined
    df['interaction_time'] = df.interaction_time.str[:7]
    df = df.groupby(['user_id','interaction_time']).agg({'price':'sum'}).reset_index()
    df = df.groupby('user_id').agg({'price':'mean'}).reset_index().rename({'price':'avg_monthly_spending'},axis=1)
    logging.info('Done building avg monthly spend feature')
    return df

def favorite_brand(df_combined):
    '''
        Assumption here is that people views the brands that they like most, but not necessairly purchase
        since it can be expensive or perhaps the are 'window shopping'.
        If the individual has viewed the most liked brand less then 5 times, then the result is indeterminant.
    '''
    logging.info('Starting to build favourite brand feature')
    df = df_combined[df_combined.interaction_type=='ProductView']
    del df_combined
    df = df[['user_id', 'brand']]
    df['counter'] = 1
    df = df.groupby(['user_id', 'brand']).agg({'counter':'sum'}).reset_index()
    df = df[df['counter'] >= 5]
    # Get Mode
    df = df[['user_id','brand']].groupby('user_id').agg(lambda x:x.value_counts().index[0]).reset_index().rename({'brand':'favorite_brand'}, axis=1)
    logging.info('Done building favourite brand feature')
    return df

def build_final_table(df_combined):
    unuqie_users = df_combined.user_id.drop_duplicates(keep='first').to_frame()
    final_df = pd.merge(unuqie_users, visit_dates(df_combined), on=['user_id', 'user_id'], how='left')
    final_df = pd.merge(final_df, avg_gap_between_vists(df_combined), on=['user_id', 'user_id'], how='left')
    final_df = pd.merge(final_df, avg_monthly_spend(df_combined), on=['user_id', 'user_id'], how='left')
    final_df = pd.merge(final_df, favorite_brand(df_combined), on=['user_id', 'user_id'], how='left')
    return final_df

    
    