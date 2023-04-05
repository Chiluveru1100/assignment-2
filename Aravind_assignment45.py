import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('fertility_rate.csv')#Reading the csv file

df

df.isna().sum() # It gives sum of all Null Values 

df = df.dropna() # Droping all the Null values

df.shape

df.columns

df1 = df[['Country Name','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968','1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977']]

final_data = df1.loc[(df1["Country Name"] == "Afghanistan") | (df1["Country Name"] == "South Africa") | (df1["Country Name"] == "Zimbabwe")]

final_data.describe() # It gives the statistical information about the data

final_data = final_data.transpose() # Transposing the data 

final_data.columns = final_data.iloc[0]

final_data = final_data.iloc[1:,:] # This is the final Data set 

final_data[['Afghanistan','South Africa','Zimbabwe']].plot(figsize=(12,8)) #Ploting the data 

data = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv',skiprows = 2) # Reading the csv File

data1 = data[['Country Name','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968','1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977','1978', '1979', '1980']]

data1 = data1.dropna() # Droping the null Values 

s1 = data1[0:1] 
s2 = data1[136:137] 
s3 = data1[336:337]

final_data1 = pd.concat([s1,s2,s3],axis = 0) # Concatinating into single dataset

final_data1.describe()

final_data1 = final_data1.transpose() # Transposing the data

final_data1.iloc[0]

final_data1.columns = final_data1.iloc[0]

final_data1 = final_data1.iloc[1:,:] # Final data

final_data1[['Aruba','Austria','Canada']].plot(figsize=(12,8)) # Ploting the data

data_df = pd.read_csv('world_population.csv') # Reading the csv file

data_df = data_df.dropna() # Droping the null values 

data_df1 = data_df[['Country/Territory','2022 Population', '2020 Population', '2015 Population','2010 Population', '2000 Population', '1990 Population','1980 Population', '1970 Population']]

data_df1.dropna(inplace = True)

data_df_final = data_df1.transpose()

data_df_final.columns = data_df_final.iloc[0]

data_df_final =data_df_final.iloc[1:,:]

data_df_final[['Argentina','Uzbekistan','Venezuela']].plot(figsize=(14,8)) # Ploting the data

sns.scatterplot(data_df_final['Argentina'],data_df_final['Uzbekistan']) # Scatter plot
