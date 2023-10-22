#Python script to analyze voting data

#Some of what I struggled with most here is if the results need to be dynamic or if I look at the results and print them myself
#I wasn't sure based on class how to call a x index in a list or dictionary. I chose to go with dictionary based on some after hours help Dallin provided to another student

import os
import csv

#read data from this file
election_csv = os.path.join("Resources", "election_data.csv")

#Create some dictionary for the results
election_results = {
    'total_votes': 0,
    'candidates': [],
    'can_votes': [],
    'can_percent': []

}

#current to compare to our dictionary values.
current = []

with open(election_csv) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #for loop to collect some data and perform some calcs
    for row in csvreader:
        
        #increment the total votes count
        election_results['total_votes'] += 1

        current = row[2]

        if current not in election_results['candidates']:
            election_results['candidates'].append(current)
            election_results['can_votes'].append(1)
        else:
            index = election_results['candidates'].index(current)
            election_results['can_votes'][index] += 1


#At this point I was confusing myself about should all this be stored in the dictionary and retrived from there or am I over complicating it?
#I'm still confused on the syntax to pass and pull variables from dictionaries and ensuring they're the right type

vote_percents = []
total_votes = int(election_results['total_votes'])
candidate_totals = []
out_put = []
previous_can_votes = None

#loop through dictionary to find candidate totals 
for x in election_results['candidates']:
    #because x is a string in this example, need to convert it to a int 
    intx = election_results['candidates'].index(x)


    candidate_votes = election_results['can_votes'][intx]


    percentage = round((candidate_votes / total_votes) * 100,3)

    out_put.append(f'{x}: {percentage:.3f}% ({candidate_votes})')

    #if the previous candidate exists - this should be false on the first run through since variable set to None outside the loop
    if previous_can_votes is not None:
        if candidate_votes > previous_can_votes:
            winner = x
    else: 
        #so I believe this else statement should make the first candidate the winner, but then the nested loop should update that anytime another candidate has more votes
        winner = x
        #Need to remember to set the previous candidate before moving on to next loop
        previous_can_votes = candidate_votes

out_put2 = f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"

out_put_joined1 = "\n".join(out_put)

out_put3 = f"\n-------------------------\nWinner: {winner}\n-------------------------"

out_put_final = out_put2 + out_put_joined1 + out_put3

print(out_put_final)

output_path = os.path.join('Analysis', 'analysis.txt')

with open(output_path, 'w') as f:
    f.write(f'{out_put_final}\n')