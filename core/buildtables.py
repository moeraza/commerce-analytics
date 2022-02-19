import pandas as pd
from core.utils import get_configs
import numpy as np
from core.log import *

def load_data():
    TEST_MODE = get_configs()
    if TEST_MODE:
        args = {'nrows':5000}
    else:
        args = {}
    df_interactions = pd.concat([
        pd.read_csv('data/interactions-2019-Dec.csv', **args),
        pd.read_csv('data/interactions-2019-Nov.csv', **args),
        pd.read_csv('data/interactions-2019-Oct.csv', **args),
        pd.read_csv('data/interactions-2020-Feb.csv', **args),
        pd.read_csv('data/interactions-2020-Jan.csv', **args)
    ])
    df_items = pd.read_csv('data/items_catalog.csv')
    return df_interactions, df_items

def process_data(df_interactions, df_items):
    '''
    Combine and clean some data
    Assumptions/Notes: Going to grab the ID for (not set) incase there are item IDs that are popular 
                       but we just do not have the name for it
    '''
    combined_df = pd.merge(df_interactions, df_items, on=["item_id", "item_id"], how='left')
    combined_df['brand'] = np.where(combined_df['brand']=='(not set)',combined_df['item_id'], combined_df['brand'])
    combined_df = combined_df.drop('item_id',axis=1)
    return combined_df


# Unqiue interaction_types == ['RemoveFromCart', 'ProductView', 'AddToCart', 'Purchase']

