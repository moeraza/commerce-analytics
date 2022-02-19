from core.buildtables import load_data, process_data
from core.buildfeatures import build_final_table
import os
from core.log import *

def main():
    store_logs()
    
    df_interactions, df_items = load_data()
    df_combined = process_data(df_interactions=df_interactions, df_items=df_items)
    del df_interactions, df_items
    final_df = build_final_table(df_combined)
    print(final_df)
    return final_df

if __name__=='__main__':
    main()