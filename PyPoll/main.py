#dependencies
import os
import csv

#read the csv
csvpath = os.path.join('Resources', 'election_data.csv')
#specify write path
output_path = os.path.join("output", "pyPoll_analysis.txt")

#empty lists for keeping track of votes per candidate
totalVotes = 0
candidateList = []
candidateTotal = {}
winner = ""
winnerTotal = 0

#loop through the csv and keep count
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        totalVotes = totalVotes + 1
        candidateName = row[2]

        if candidateName not in candidateList:
            candidateList.append(candidateName)
            candidateTotal[candidateName] = 0

        candidateTotal[candidateName] = candidateTotal[candidateName] + 1

with open(output_path, "w") as txt_file:

    results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"----------------------\n"
    )
    print(results, end="")

    txt_file.write(results)

    for candidate in candidateTotal:

        voteCount = candidateTotal.get(candidate)
        votePercent = float(voteCount) / float(totalVotes) * 100

        if (voteCount > winnerTotal):
            winnerTotal = voteCount
            winner = candidate
        
        outcome = f"{candidate}: {votePercent: .3f}% ({voteCount})\n"
        print(outcome, end="")

        txt_file.write(outcome)

    winnerSummary = (
        f"---------------\n"
        f"Winner: {winner}\n"
        f"---------------\n"
    )
    
    print(winnerSummary)
    
    txt_file.write(winnerSummary)

