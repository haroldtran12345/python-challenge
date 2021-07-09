#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

csv_path = os.path.join( "Resources", "budget_data.csv")
path_out = os.path.join( "Analysis", "Financial_analysis.txt")


# In[2]:


month = 0
PnL = 0
past_rev = 0
change = 0
date = []
net_PnL = []


# In[3]:


with open(csv_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    month += 1
    PnL += int(first_row[1])
    past_rev = int(first_row[1])
    
    
    for row in csvreader:
        date.append(row[0])
        month += 1
        change = int(row[1])-past_rev
        net_PnL.append(change)
        past_rev = int(row[1])
        
        PnL = PnL + int(row[1])
         
    avg_change = sum(net_PnL)/len(net_PnL)

    great_inc = max(net_PnL)
    great = net_PnL.index(great_inc)
    great_date = date[great]

    great_dec = min(net_PnL)
    worst = net_PnL.index(great_dec)
    worst_date = date[worst]


# In[4]:


print("Financial Analysis")
print("---------------------")
print(f"Total Month: {month}")
print(f"Total: ${PnL}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {great_date} (${great_inc})")
print(f"Greatest Decrease in Profits: {worst_date} (${great_dec})")


# In[5]:


with open(path_out, "w") as results:
    results.write("\n\nFinancial Analysis\n")
    results.write("---------------------\n")
    results.write(f"Total Month: {month}\n")
    results.write(f"Total: ${PnL}\n")
    results.write(f"Average Change: ${round(avg_change,2)}\n")
    results.write(f"Greatest Increase in Profits: {great_date} (${great_inc})\n")
    results.write(f"Greatest Decrease in Profits: {worst_date} (${great_dec})\n")


# In[ ]:




