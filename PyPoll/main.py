#total number of votes cast
# complete list of candidates who received votes
#the percentage of votes each each candidate won
#toal number of votes each candidate won
#the winner of the election based on popular vote

import csv
import os
import random

election_data = r'PyPoll\resources\election_data.csv'
list = {election_data[0]: 
        election_data[1]:
        election_data[2]}
row = list

total_votes = 0
name1 = ()
name2 = ()
name3 = ()
name1_votes = ()
name2_votes = ()
name3_votes  =()

#total votes
#for num in int(row[0]):
    #total_votes += num
    #print(total_votes)

#number of times a name appears
if row[2] in name1:
    name1 = list.append(name1)
    name1_votes = len(list)
    print(name1)
    print(name1_votes)

if row[2] in name2:
     name2 = list.append(name2)
     name2_votes = len(list)
     print(name2)
     print(name2_votes)

if row[2] in name3:
     name3 = list.append(name3)
     name3_votes = len(list)
     print(name3)
     print(name3_votes)

with open(election_data, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvfile)
     
candidate_name = input ("which candidate has the most votes?")
for row in csvreader:
     if candidate_name == row[2]:
     #percentages = (candidate_totalvotes/total_votes)*100

     #if candidate name is = to ballot id --> get sum of votes
     #sum_votes = total

#winner
#if name1_votes > name2_votes
#print (name1)
#elif name1_votes > name3_votes
#print(name1)
#elif name2_votes < name1_votes
#print(name2)
#elif name2_votes > name3_votes
#print (name2)
#else
#print (name3)


      #if candidate_name != candidate_options:
           # candidate_options.append(candidate_name)
            #candidate_votes[candidate_name] = 0
            #candidate_votes[candidate_name] = candidate_votes [candidate_name] + 1
            #print (candidate_name)

#print (f"election results")
#print ('---')
#print (f'{total_votes}')
#print ("{name1}:{percentage1},{vote_count1}")
#print ("{name2}:{percentage2},{vote_count2}")
#print ("{name3}:{percentage3},{vote_count3}")
#print ('---')
#print (f"Winner: Dianna DeGette")

#main = 'Analysis/mytextfile.txt'