import pandas as pd

# read excel file
df = pd.read_excel('supermarket_sales.xlsx')
#print(df)

# select columns
df = df[['Gender', 'Product line', 'Total']]
#print(df)

# pivot table: how much each gender is paid in each product line?
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
#print(pivot_table)

# export pivot table to excel file
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)