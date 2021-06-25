# libraries
import os
import csv

# set path for file
csvpath = os.path.join("Resources","budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header
    csv_header = next(csvreader)
    
    # loop through the rows
    for row in csvreader:
        # store the csv as a list
        data = list(csvreader)
        # get the total number of months by counting rows (excluding header)
        total_months = len(data)
        # get the total amount of profit/losses over the entire period
       



            


        







    
