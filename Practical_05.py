
.


import pandas as pd 
# Loading the datasets 
df1 = pd.read_csv("d1.csv")
df2 = pd.read_csv("d2.csv")
df3 = pd.read_csv("d3.csv")
print("[+]Available Data Sets : ")
print(df1.head())
print(df2.head())
print(df3.head())


print("[+]Null Values in DataSet-1: ")
mis_match_count = df1.isnull().sum()
print(mis_match_count)

# Printing the count of NULL values in DataSet-2 
print("[+]Null Values in DataSet-2 : ")
mis_match_count = df2.isnull().sum()
print(mis_match_count)

# Printing the the count of NULL values in the DataSet-3 
print("[+]Null Values in DataSet-3 : ")
mis_match_count = df3.isnull().sum()
print(mis_match_count)

# First Merging the dataset1 and dataset2 
merged_dataset = pd.merge(df1,df2,on=["Rank","State","Population"])

# Second Merging the merged_dataset and dataset3 in order to 
# merge three data sets 
merged_dataset = pd.merge(merged_dataset,df3,on=["Rank","State","Population"])
# Merged Table By Overriding the Mergee 
print(merged_dataset)
