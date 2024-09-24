import sqlite_lib as sb

'''
import sqlite3
import pandas as pd

conn = sqlite3.connect('E-commerce Customer Behavior - Sheet1.db')

df = pd.read_csv('E-commerce Customer Behavior - Sheet1.csv')
df.to_sql('e_commerce', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
'''
sb.connect('e-commerce Customer Behavior - Sheet1.db')

print(sb.run_query_select('select count(*) from e_commerce')[0][0])

print(sb.run_query_select('select avg(age) from e_commerce')[0][0])

print(sb.run_query_select('select gender, count(*) from e_commerce where gender = "Male"')[0])
print(sb.run_query_select('select gender, count(*) from e_commerce where gender = "Female"')[0])

print(sb.run_query_select('select gender, avg("Items Purchased") from e_commerce where gender = "Male"')[0])
print(sb.run_query_select('select gender, avg("Items Purchased") from e_commerce where gender = "Female"')[0])

print(sb.run_query_select('select count(DISTINCT "Membership Type") from e_commerce')[0][0])

print(sb.run_query_select('select "Membership Type" ,count(*) from e_commerce where "Membership Type" = "Gold"')[0])
print(sb.run_query_select('select "Membership Type" ,count(*) from e_commerce where "Membership Type" = "Silver"')[0])
print(sb.run_query_select('select "Membership Type" ,count(*) from e_commerce where "Membership Type" = "Bronze"')[0])

print(sb.run_query_select('select "City", count(*) from e_commerce where "City" = "New York"')[0])

print(sb.run_query_select('select "City", count(*) from e_commerce group by "City" order by count(*) desc'))

print(sb.run_query_select('select gender, sum("Total Spend") from e_commerce where gender = "Male"')[0])
print(sb.run_query_select('select gender, sum("Total Spend") from e_commerce where gender = "Female"')[0])

print(sb.run_query_select('select "Customer Id", max("Items Purchased") from e_commerce')[0])
print(sb.run_query_select('select "Customer Id", min("Items Purchased") from e_commerce')[0])


sb.close()

