import pandas as pd

#goupil full dataset can be downloaded from the Getty Provenance Index github repo: https://github.com/thegetty/provenance-index-csv/tree/main/goupil#files
#this data is offered under the Creative Commons CC1.0 Universal Public Domain Dedication
df = pd.read_csv('goupil.full.dataset.csv')

#select required columns from main Goupil dataset, and drop all rows where required columns are empty
required_columns = ['sale_date_year', 'transaction', 'buy_auth_name_1', 'buy_auth_addr_1', 'sale_location']
df = df[required_columns].dropna()

#only keep rows where work was 'sold' ('Vendu'), and the date year is given a valid value (e.g. higher than 0).
df = df[df.transaction == 'Vendu']
df = df[df.sale_date_year > 0]

#get rid of sale locations where exact location is unknown; can alter blacklist as required.
location_blacklist = ['vente publique', 'Vente publique', 'Exposition de St. Quentin', 'Exposition Saint Quentin', 'Vente publique Frais 20%', 'Vendu en vente publique par Paul Chevallier 18 FÃ©vrier 1882', 'Vente publique frais 20%','[vente publique, rayé]', 'Vendu en vente publique par M. Paul Chevallier']
df = df[~df.sale_location.isin(location_blacklist)]

#get rid of sale locations where exact location is unknown
name_blacklist = ['NON-UNIQUE']
df = df[~df.buy_auth_name_1.isin(name_blacklist)]

#save new filtered dataset to a csv file
df.to_csv('goupil_pandas_cleaned.csv', index=False)

#create table of unique Buyer name values, with index
table_1 = pd.DataFrame({"Name":df['buy_auth_name_1'].unique()})
table_1['Category'] = "Buyer"

#create table of unique Sale Location values with index
table_2 = pd.DataFrame({"Name":df['sale_location'].unique()})
table_2['Category'] = "Sale Location"

#merge two tables to create a Node table of all Buyers and Sale Locations
node_table = pd.merge(table_1, table_2, how='outer')

#save new Node table to csv file
node_table.to_csv('goupil_node_keys.csv')