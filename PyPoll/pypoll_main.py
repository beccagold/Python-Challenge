import csv
import os
file_load = 'rawelection_data.csv'
file_output = 'pypoll_analysis.txt'

#variables
total = 0
num_candidates = 0
maxv = 0

#empty list or dictionary
candidates = []
candidatev = {}

# read csv
with open(file_load) as polldata:
    reader = csv.DictReader(polldata)

    for row in reader:
        candidatecurrent = row['Candidate']
        
        if candidatecurrent not in candidates:
            candidates.append(candidatecurrent)
            num_candidates+=1#increase candidate number by 1 for  votes summary
            candidatev[candidatecurrent]=0
        candidatev[candidatecurrent] += 1
        total +=1
        if candidatev[candidatecurrent] > maxv:
            winner = candidatecurrent
            maxv = candidatev[candidatecurrent]
#initial output
output = '\nElection Results\n_________________\nTotal Votes: %d\n_________________' %(total)
#loop to post every outpyt per candidate
for name in candidates:
    
    results = ('  %s: %.3f%% (%d)' %(name,  100*candidatev[name]/(total), candidatev[name]))#convert to % and f statement
    output = output+'\n'+results #combines to 1 output for the final variable to print

#prints the entire output easier for writing a file
final_output = output +'\n_________________\n  Winner: %s\n_________________\n' %(winner)#combines the looped output and winner ouput
print(final_output)

with open(file_output, 'w') as fileoutput:#writes the file using variable
    fileoutput.write(final_output)