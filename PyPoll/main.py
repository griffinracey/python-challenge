# Modules
import os
import csv

row_count = 0
candidates_list_unclean = []
candidates_list = []
stockham = 0
stockham_percent = 0.00
degette = 0
degette_percent = 0.00
doane = 0
doane_percent = 0.00
win_count = 0
win_index = 0
winner_list = []

# reading in csv & prining headers
path = os.path.join("Resources", "election_data.csv")
with open(path) as file:
    csv_reader = csv.reader(file,delimiter=",")

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')

    # The total number of votes cast
    for row in csv_reader:
        row_count = row_count + 1

# A complete list of candidates who received votes
        if row[2] not in candidates_list:
            candidates_list.append(row[2])

# The total number of votes each candidate won
        if row[2] == 'Charles Casper Stockham':
            stockham = stockham + 1
        elif row[2] == 'Diana DeGette':
            degette = degette + 1
        elif row[2] == 'Raymon Anthony Doane':
            doane = doane + 1

# The percentage of votes each candidate won
    stockham_percent = round(((stockham / row_count) * 100),3)
    degette_percent = round(((degette / row_count) * 100),3)
    doane_percent = round(((doane / row_count) * 100),3)

# The winner of the election based on popular vote
    winner_list = [stockham,degette,doane]
    for i in range(len(winner_list)):
        if winner_list[i] > win_count:
            win_count = winner_list[i]
            win_index = i
        if win_index == 0:
            winner = 'Charles Casper Stockham'
        elif win_index == 1:
            winner = 'Diana DeGette'
        elif win_index == 2:
            winner = 'Raymon Anthony Doane'

    print("-----------------------------")
    print(f'Total Votes: {row_count}')
    print("-----------------------------")
    print(f'Charles Casper Stockham: {stockham_percent}% ({stockham})')
    print(f'Diana DeGette: {degette_percent}% ({degette})')
    print(f'Raymon Anthony Doane: {doane_percent}% ({doane})')
    print("-----------------------------")
    print(f'Winner: {winner}')

# Choosing file to send text output to
output_file = os.path.join("Analysis","analysis.txt")

with open(output_file, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")

    # Take terminal outputs and send to txt file
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f'Total Votes: {row_count}'])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f'Charles Casper Stockham: {stockham_percent}% ({stockham})'])
    csvwriter.writerow([f'Diana DeGette: {degette_percent}% ({degette})'])
    csvwriter.writerow([f'Raymon Anthony Doane: {doane_percent}% ({doane})'])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
