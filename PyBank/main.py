#Python script to analyze the financial records of your company
#import items as shown in code from class
import os
import csv

#read the csv file using code shown from class
budget_csv = os.path.join("Resources", "budget_data.csv")

#create some variables to store the data
#months_list will store all the entries for column 1
months_list = []
#variable to count the number of months
months_count = 0

#need variable to hold all the profit and losses in a list
pl_list = []

#need to keep track of current and previous months p&l's so we can track changes, etc. 
pl_current = 0
pl_previous = None
pl_change = []
#change is going to be used to populate change list
change = 0
previous_change = 0

#need variable to total p&l's 
pl_sum = 0

#need variables for increases and decreases
pl_increase = 0
pl_increase_string = []
pl_decrease = 0
pl_decrease_string = []

with open(budget_csv) as csvfile: 
    #comma separated values
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    next(csvreader)

    #loop through to collect data
    for row in csvreader:
        #add column 0 to months_list
        months_list.append(row[0])

        #increment the number of total months
        months_count +=1
        
        #add column 1 to the pl_list
        pl_list.append(row[1])

        #set the current month p&l to row(1)
        pl_current = int(row[1])

        #if statement to get the p&l changes over time
        if pl_previous:
            change = pl_current - pl_previous
            pl_change.append(change)
        
        #need a way to check if the current change is greater than the last change
        if pl_increase < change: 
            #if the current largest increase in P&L is less than the current change then the higher change is passed to the variable
            pl_increase = change
            #then, still only if the current change is more, we will rewrite the string that should include the date
            pl_increase_string = f'{row[0]} (${pl_increase})'
        
        #same except for decrease
        if pl_decrease > change:
            pl_decrease = change
            pl_decrease_string = f'{row[0]} (${pl_decrease})'

        #calculate the sum of p&l's 
        pl_sum = int(pl_sum + pl_current)
        
        #set the previous months value before the loop ends
        pl_previous = pl_current

#calculate the average
pl_change_sum = sum(pl_change)
pl_average = round((pl_change_sum) / (len(pl_change)),2)

#I thought I'd make the output strings (o1 = output 1, o2 = output 2, and so on) into variables to make it less typing later. 
o1 = f'Financial Analysis'
o2 = f'----------------------------'
o3 = f'Total Months: {months_count}'
o4 = f'Total: ${pl_sum}'
o5 = f'Average Change: ${pl_average}'
o6 = f'Greatest Increase in Profits: {pl_increase_string}'
o7 = f'Greatest Decrease in Profits: {pl_decrease_string}'

#print results to terminal 
print(o1)
print(o2)
print(o3)
print(o4)
print(o5)
print(o6)
print(o7)

#using this write method found on YouTube because I was getting some extra characters when I tried to copy paste the versions from class. YouTube video citation is in the readme. 
#writing out each variable. I did consider zipping the outputs into one but I was again having trouble with extra characters in the output file. 
output_path = os.path.join('Analysis', 'analysis.txt')

with open(output_path, 'w') as f:
    f.write(f'{o1}\n')
    f.write(f'{o2}\n')
    f.write(f'{o3}\n')
    f.write(f'{o4}\n')
    f.write(f'{o5}\n')
    f.write(f'{o6}\n')
    f.write(f'{o7}\n')    

