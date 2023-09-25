# Modules
import os
import csv

profit_list = []
date_list = []

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

    # The total number of months included in the dataset
    print(f'There are {row_count} months in the dataset')

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f'The net total amount of Profits/Losses is {sum(profit_list)} over the period of the dataset')
    print(f'The average of these changes is: {(sum(profit_list))/len(profit_list)}')

    # The greatest increase in profits (date and amount) over the entire period
    for i in range(len(profit_list)):
        if profit_list[i] > max_profit:
            max_profit = profit_list[i]
            max_index = i
    print(f'The greatest increase in profits is ${profit_list[max_index]} and it was on {date_list[max_index]}')


# The greatest decrease in profits (date and amount) over the entire period 
    for i in range(len(profit_list)):
        if profit_list[i] < min_profit:
            min_profit = profit_list[i]
            min_index = i
    print(f'The greatest decrease in profits is ${profit_list[min_index]} and it was on {date_list[min_index]}')