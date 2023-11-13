#total number of votes cast
# complete list of candidates who received votes
#the percentage of votes each each candidate won
#toal number of votes each candidate won
#the winner of the election based on popular vote

import csv
import os
import random

election_data = r'PyPoll\resources\election_data.csv'

total_votes = 0
name_count = 0

#candidate_list = candidate["name"]
#candidate_list = [row[1]]

with open(election_data, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvfile)

total_votes = total_votes + 1
print (total_votes)

f = open(election_data, 'r') 
lines = f.readlines ()
for line in lines:
      print (line.split(','))
      break

# winner = str(input(who is the winner?))
#print (name_winner)

#main.py = 'Analysis/mytextfile.txt'