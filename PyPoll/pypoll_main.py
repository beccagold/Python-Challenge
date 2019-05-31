import csv

# files to load and output
file_to_load = 'rawelection_data.csv'
file_to_output = 'analysis.txt'

#variables
total_votes = 0
num_candidates = 0
candidate_list = []
candidate_votes = {}
max_votes = -1

# read csv
with open(file_to_load) as polldata:
    reader = csv.DictReader(polldata)

    for row in reader:
        candidate_current = row['Candidate']
        if candidate_current not in candidate_list:
            num_candidates = num_candidates+1
            candidate_list.append(candidate_current)
            candidate_votes[candidate_current]=0

        candidate_votes[candidate_current] = candidate_votes[candidate_current] +1
        total_votes = total_votes +1
        
        if candidate_votes[candidate_current] > max_votes:
            max_votes = candidate_votes[candidate_current]
            candidate_winner = candidate_current

output = 'Election Results\n....................\nTotal Votes: %d\n....................' %(total_votes)

#print(output)
for name in candidate_list:
    results = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+total_votes), candidate_votes[name]))
    output = output + '\n' + results

#print(output)
final_output = output + '\n....................\n  Winner: %s\n....................\n' %(candidate_winner)
print(final_output)