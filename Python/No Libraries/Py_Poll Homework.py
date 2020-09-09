#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import os
import csv

#bring in csv
file = os.path.join('..','PyBank','election_data.csv')
file_df = pd.read_csv(file)
file_df.head()


# In[93]:


#calculate how many lines there are - total votes
total = file_df['Voter ID'].count()

#list of candidates
#candidate = file_df['Candidate'].unique()

#How many votes each
candidate = file_df.Candidate.value_counts()

#Percentages
percent = (file_df.Candidate.value_counts()/total).apply('{:.0%}'.format)
percent_df = percent

#group them
#end= candidates.groupby('total').nunique

#winner
winner = candidate.max()


# In[94]:


print('Election Results')
print('--------------------------')
print(f"Total Votes: {total}")
print('--------------------------')
print(f"{percent}{candidate}")
print('--------------------------')
print(f"Winner: {winner}")
print('--------------------------')


# In[ ]:




