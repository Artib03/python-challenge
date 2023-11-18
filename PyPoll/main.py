#total number of votes cast
# complete list of candidates who received votes
#the percentage of votes each each candidate won
#toal number of votes each candidate won
#the winner of the election based on popular vote

import csv
import os
import random

election_data = r'PyPoll\resources\election_data.csv'
row = zip(election_data[0], election_data[1], election_data[2])

total_votes = 0
name1 = ()
name2 = ()
name3 = ()
name1_votes = ()
name2_votes = ()
name3_votes  =()
percentage_rate = ()
candidate_name_list = []

with open(election_data, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvfile)

     for row in csvreader:
          total_votes = total_votes + 1
    #print(total_votes)

#number of times a name appears
if row[2] in name1:
    name1 = candidate_name_list.append(name1)
    name1_votes = len(candidate_name_list)
    print(name1)
    print(name1_votes)

if row[2] in name2:
     name2 = candidate_name_list.append(name2)
     name2_votes = len(candidate_name_list)
     print(name2)
     print(name2_votes)

if row[2] in name3:
     name3 = list.append(name3)
     name3_votes = len(list)
     print(name3)
     print(name3_votes)

#percent = round(int(row[8]) / total_votes * 100, 2)
        #percentage_rate.append(str(percent) + "%")

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

print (f"election results")
print ('---')
print (f'{total_votes}')
#print ("{name1}:{percentage1},{vote_count1}")
#print ("{name2}:{percentage2},{vote_count2}")
#print ("{name3}:{percentage3},{vote_count3}")
#print ('---') 
#print (f'{winner})                                                                                