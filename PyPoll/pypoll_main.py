import csv
file_load = 'rawelection_data.csv'
file_output = 'pypoll_analysis.txt'

#variables
total = 0
num_candidates = 0
max_votes = -1
#empty list or dictionary
candidates = []
candidate_votes = {}

# read csv
with open(file_load) as polldata:
    reader = csv.DictReader(polldata)

    for row in reader:
        candidate_current = row['Candidate']
        if candidate_current not in candidates:
            num_candidates+=1#increase candidate number by 1 for  votes summary
            candidates.append(candidate_current)
            candidate_votes[candidate_current]=0

        candidate_votes[candidate_current] += 1
        total +=1
        
        if candidate_votes[candidate_current] > max_votes:
            max_votes = candidate_votes[candidate_current]
            winner = candidate_current
#initial output
output = '\nElection Results\n_________________\nTotal Votes: %d\n_________________' %(total)

#loop to post every outpyt per candidate
for name in candidates:
    results = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+total), candidate_votes[name]))#convert to % and f statement
    output = output+'\n'+results #combines to 1 output for the final variable to print

#prints the entire output
final_output = output +'\n_________________\n  Winner: %s\n_________________\n' %(winner)#combines the looped output and winner ouput
print(final_output)

with open(file_output, 'w') as outputfile:#writes the file
    outputfile.write(final_output)