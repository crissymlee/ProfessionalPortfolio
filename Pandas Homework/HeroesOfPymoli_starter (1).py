#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[253]:


# Dependencies and Setup
import pandas as pd
import os
import csv

# File to Load (Remember to Change These)
file_to_load = os.path.join("purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[254]:


#players = purchase_data.count()
#playersdf = dataframe.players
total = []
total = purchase_data['SN'].unique()
Players = len(total)
PlayersDf = pd.DataFrame(columns = ['Total Players'])
PlayersDf = PlayersDf.append({'Total Players' : Players},ignore_index=True)
PlayersDf


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[255]:


#calculations
unique_items_names = purchase_data["Item Name"].unique() #The unique items
unique_items = len(unique_items_names) #Number of Unique Items
av_price = purchase_data["Price"].mean() #Average Price
num_purchases = purchase_data["Purchase ID"].count() #Number of Purchases
total_rev = purchase_data["Price"].sum() #Total Revenue



#Summary
CalulationsDf = pd.DataFrame()
CalulationsDf = CalulationsDf.append({'Number of Unique Items' : unique_items, 
                                    'Average Price': av_price, 
                                    'Number of Purchases': num_purchases,
                                    'Total Revenue': total_rev},ignore_index=True)

Format_CalcDf = {'Number of Unique Items': '{0:,.0f}',
                'Average Price': '${0:,.2f}', 
                'Number of Purchases': '{0:,.0f}',
                'Total Revenue': '${0:,.2f}'}
CalulationsDf.style.format(Format_CalcDf).hide_index()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[256]:


#create a dict for Gender Counts and Percentages


#calculations
unique_player_gender = purchase_data.loc[:, ['SN', 'Age', 'Gender']].drop_duplicates()
unique_player_gender = unique_player_gender['Gender'].value_counts()
unique_player_gender_pct = unique_player_gender/Players*100

#summary
Gender_summary = pd.DataFrame({
    "Total Count": unique_player_gender, 
    "Percentage": unique_player_gender_pct
}).style.format({'Percentage': '{:.4}%'})
Gender_summary




    #WORKING BUT
    #THIS IS RETURNING ALL NOT UNIQUE SN right now
#gender_counts = purchase_data["Gender"].value_counts() #How total purchases of each gender
#percent = (gender_counts/num_purchases).apply('{:.2%}'.format) #percent of gender purchases
#unique_gender_counts = unique_gender_counts.groupby(purchase_data("Gender")["SN"].nunique()

#Gender_dict = {"Total Count": unique_gender_counts,
 #             "Percentage of Players": percent}

#Gender_dict = pd.DataFrame(Gender_dict)
#Gender_dict.head()


    #WORKING BUT LOOKS BAD & Not Unique SNs
#GenderDf
#frames = [gender_counts, percent]
#end= pd.concat((frames), axis=1)
#end


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[257]:


#gender_total_counts = purchase_data["Gender"].value_counts() #How many of the unique screenname genders

gender_analysis = purchase_data.groupby(['Gender'])['Price'].agg(['sum', 'count', 'mean'])
gen_sales_total = gender_analysis['sum'] #total of sales
av_tot_pur_val = gen_sales_total.div(unique_player_gender) #Avergae total per player
gender_counts = purchase_data['Gender'].value_counts() #How total purchases of each gender
av_pur_price = gender_analysis['mean']
tot_pur_val = gender_analysis.sum()


#create summary
Gender_total_dict = {'Purchase Count': gender_counts,
                     'Average Purchase Price': av_pur_price,
                     'Total Purchase Value': gen_sales_total,
                     'Avg Total Purchse per Person': av_tot_pur_val}

#clean
Format_CalcDf2 = {'Purchase Count': '{0:,.0f}',
                  'Average Purchase Price': '${0:,.2f}', 
                  'Total Purchase Value': '${0:,.2f}',
                  'Avg Total Purchse per Person': '${0:,.2f}'}

Gender_total_dict = pd.DataFrame(Gender_total_dict)


#Print
Gender_total_dict.style.format(Format_CalcDf2)

#Gender_total_dict.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[258]:


#Establish Bins
age_bin = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 1000]
name_bin = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']


#Establish DF
age_df = purchase_data.loc[:, ["SN", "Age"]].drop_duplicates()
ages = age_df["Age"]

#Categorize existing players using the age bins
ages["Age"] = pd.cut(ages, age_bin, labels=name_bin)

#Calculate the numbers and percentages by age group - rounding to 2 decimals
ages = (pd.DataFrame(ages["Age"].value_counts()))
ages.sort_index(inplace=True)
ages['Percentage'] =  pd.Series(["{0:.2f}%".format((age_count / Players) * 100) for age_count in ages["Age"]], index = ages.index)



#name the columns
ages.rename(columns={'Age': 'Age Range Count'}, inplace=True)

#Print
ages


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[259]:


#Bin the purchase_data by age
purchase_data["Ages"] = pd.cut(purchase_data["Age"], age_bin, labels=name_bin)

#Run basic calculations
sales_by_age = purchase_data.groupby(["Ages"])["Price"].agg(['sum', 'count', 'mean'])
sales_count =sales_by_age['count']
sales_av = sales_by_age['mean']
sales_age = sales_by_age['sum']
av_sales_person = sales_by_age['sum'] /                     ages['Age Range Count']

#Create a summary
sales_age_summary = pd.DataFrame({
                    "Purchase Count": sales_count,
                    "Average Purchase Price": sales_av,
                    "Total Sales per Person": sales_age,
                    "Avg Sales per Person": av_sales_person})

#clean
Format_CalcDf3 = {'Average Purchase Price': '${:.3}', 
                    'Total Sales per Person': '${:.6}', 
                    'Avg Sales per Person': '${:.3}'}


#Print
sales_age_summary.style.format(Format_CalcDf3)


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[271]:


#Make df for specific columns
top_spenders = purchase_data.groupby(["SN"])["Price"].agg(['sum', 'count', 'mean'] )

#calculations
purchase_count =  top_spenders['count']
av_prch_price = top_spenders['mean']
prch_per_person = top_spenders['sum']


#Summary
top_spenders_summary = pd.DataFrame({'Purchase Count': purchase_count,
                                     'Average Purchase Price': av_prch_price,
                                     'Total Sales per Person': prch_per_person})

#acending order
top_spenders_summary = top_spenders_summary.sort_values('Purchase Count', ascending = False)                                      

#clean
Format_CalcDf4 = ({'Average Purchase Price': '${:.3}', 
                    'Total Sales per Person': '${:.6}', 
                    'Avg Sale per Person': '${:.3}'})
top_spenders_summary2 = top_spenders_summary.style.format(Format_CalcDf4)





#Print
top_spenders_summary2


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[250]:


#make df for specific columns
most_pop = purchase_data.groupby(['Item ID', 'Item Name'])['Price'].agg(['sum', 'count', 'mean'])

#name the columns
most_pop.columns = ["Item Total Sales", "Purchase Count", "Avg Item Price"]

#Calculations
most_pop_df = pd.DataFrame(most_pop).sort_values("Purchase Count", ascending=False)

#clean
Format_CalcDf5 =({'Avg Item Price': '${:.6}', 
                    'Item Total Sales': '${:.4}'})

#Print
most_pop_df.style.format(Format_CalcDf5)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[246]:


#sort
most_prof = pd.DataFrame(most_pop)                     .sort_values("Item Total Sales", ascending=False) 
 
#clean    
Format_CalcDf6 = ({'Avg Item Price': '${:.6}', 
                   'Item Total Sales': '${:.4}'})

#print
most_prof.style.format(Format_CalcDf6)


# In[ ]:




