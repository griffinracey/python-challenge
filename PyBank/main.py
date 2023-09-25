# Modules
import os
import csv

profit_list = []
date_list = []
change_list = []

row_count = 0
profit_tot = 0
max_profit = 0
min_profit = 0
max_index = 0
min_index = 0

# Set path for file
path = os.path.join("Resources", "budget_data.csv")

# Read in csv
with open(path) as file:
    csv_reader = csv.reader(file,delimiter=",")

    print(csv_reader)

    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_reader:
        row_count = row_count + 1
        profit_list.append(int(row[1]))
        date_list.append(str(row[0]))

    #  Create list of month to month change
    for i in range((len(profit_list))-1):
        change_list.append(profit_list[i+1] - profit_list[i])
     

    # The total number of months included in the dataset
    print(f'There are {row_count} months in the dataset')

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f'The net total amount of Profits/Losses is {sum(profit_list)} over the period of the dataset')
    print(f'The average of these changes is: ${round((sum(change_list))/len(change_list),2)}')

    # The greatest increase in profits (date and amount) over the entire period
    for i in range(len(change_list)):
        # check to see if current value is greater than current max
        if change_list[i] > max_profit:
            max_profit = change_list[i]
            max_index = i

    # print out greatest increase and date
    print(f'The greatest increase in profits is ${change_list[max_index]} and it was on {date_list[max_index + 1]}')


# The greatest decrease in profits (date and amount) over the entire period 
    for i in range(len(change_list)):
        # check to see if current value is less than current min
        if change_list[i] < min_profit:
            min_profit = change_list[i]
            min_index = i

    # print out greatest decrease and date
    print(f'The greatest decrease in profits is ${change_list[min_index]} and it was on {date_list[min_index + 1]}')

# Open the file using "write" mode. Specify the variable to hold the contents
output_file = os.path.join("Analysis", "analysis.txt")

with open(output_file, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow([f'There are {row_count} months in the dataset'])
    csvwriter.writerow([f'The net total amount of Profits/Losses is {sum(profit_list)} over the period of the dataset'])
    csvwriter.writerow([f'The average of these changes is: ${round((sum(change_list))/len(change_list),2)}'])
    csvwriter.writerow([f'The greatest increase in profits is ${change_list[max_index]} and it was on {date_list[max_index + 1]}'])
    csvwriter.writerow([f'The greatest decrease in profits is ${change_list[min_index]} and it was on {date_list[min_index + 1]}'])