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

        #keep track of current candidate
        current = row[2]

        #if statement to check if the candidate has changed. I used AskBCS and Sunshine helped clue me in on using if statements for PyBank, https://pythontic.com/containers/dictionary/notin
        if current not in election_results['candidates']:
            #if not, add them to the dictionary under the candidates key
            election_results['candidates'].append(current)
            #Then start tallying their votes
            election_results['can_votes'].append(1)
        else:
            #if the candidate has not changed, 
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
    #because x is a string in this example, need to convert it to a int. Referenced Stackoverflow examples: https://stackoverflow.com/questions/5316720/how-can-i-convert-string-values-from-a-dictionary-into-int-float-datatypes

    intx = election_results['candidates'].index(x)

    #making this variable easy to access for the percentage calc
    candidate_votes = election_results['can_votes'][intx]

    #calc the percentage and round to three decimal places
    percentage = round((candidate_votes / total_votes) * 100,3)

    #write to the out_put list for each candidate's name, percent, and votes then repeat
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

#My output variables might not be the most efficient, I was reading https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals to figure out how to do this and wanted to put it in variables
#Also looked at https://realpython.com/python-string-concatenation/ for putting strings together. 
out_put2 = f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"
out_put_joined1 = "\n".join(out_put)
out_put3 = f"\n-------------------------\nWinner: {winner}\n-------------------------"
out_put_final = out_put2 + out_put_joined1 + out_put3

#Print to terminal
print(out_put_final)

#Print to file
#This code is pulled from my PyBank code except I deleted the unnecessary write statements and changed the variable name. In PyPoll, I believe I was more efficient in writing the output. 
output_path = os.path.join('Analysis', 'analysis.txt')

with open(output_path, 'w') as f:
    f.write(f'{out_put_final}\n')