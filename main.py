#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv

csv_path = os.path.join( "Resources", "election_data.csv")
path_out = os.path.join( "Analysis", "Results.txt")

county = []
vote = []
candidate = []
otooley = []
khan = []
correy = []
li = []

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        vote.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
        for can in candidate:
            if can == "khan":
                khan.append(candidate)
                vote_khan = len(khan)
            elif can == "correy":
                correy.append(candidate)
                vote_correy = len(correy)
            elif can == "li":
                li.append(candidate)
                vote_li = len(li)
            else:
                otooley.append(candidate)
                vote_otooley = len(otooley)
                
        vote_total = len(row [1])

    percentage_khan = round(((vote_khan / vote_total) * 100), 2)
    percentage_correy = round(((vote_correy / vote_total) * 100), 2)
    percentage_li = round(((vote_li / vote_total) * 100), 2)
    percentage_otooley = round(((vote_otooley / vote_total) * 100), 2)

    def winner(candidate):
        return max(set(candidate), key = candidate.count)
    
print("Election Results")
print("----------------------------")
print(f"Total votes:  {vote}")
print("----------------------------")
print(f"Khan: %{percentage_khan} ({vote_khan})")
print(f"Correy: %{percentage_correy} ({vote_correy})")
print(f"Li: %{percentage_li} ({vote_li})")
print(f"O'Tooley: %{percentage_otooley} ({vote_otooley})")
print("----------------------------")
print(f"Winner: ({winner})")
print("----------------------------")


# In[ ]:


with open(path_out, "w") as results:
    results.write("Election Results\n")
    results.write("----------------------------\n")
    results.write(f"Total votes:  {vote}\n")
    results.write("----------------------------\n")
    results.write(f"Khan: %{percentage_khan} ({vote_khan})\n")
    results.write(f"Correy: %{percentage_correy} ({vote_correy})\n")
    results.write(f"Li: %{percentage_li} ({vote_li})\n")
    results.write(f"O'Tooley: %{percentage_otooley} ({vote_otooley})\n")
    results.write("----------------------------\n")
    results.write(f"Winner: ({winner})\n")
    results.write("----------------------------\n")


# In[ ]:




