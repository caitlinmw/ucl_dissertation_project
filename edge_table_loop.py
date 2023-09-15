import pandas as pd

#use filtered table created by running process_goupil.py
df = pd.read_csv('goupil_pandas_cleaned.csv')

#use Node table created by running process_goupil.py
node_table = pd.read_csv('goupil_node_keys.csv')

#create new dictionary to store values
node_table_dict = dict(node_table)

#iterate through the filtered dataset, checking for matches against the Sale Location and the Buyer name
#create a Source field for Sale Locations and allocate Node index as an ID
#create a Target field for Buyers and allocate Node index as an ID
for df_index, df_row in df.iterrows():
        
    for node_index, node_row in node_table.iterrows():
        
        if df_row.sale_location == node_row.Name:
            df.at[df_index, "Source"] = node_index

    for node_index, node_row in node_table.iterrows():

        if df_row.buy_auth_name_1 == node_row.Name:
            df.at[df_index, "Target"] = node_index

#output new Edge table as csv
df.to_csv('new_edge_table.csv', index=False)