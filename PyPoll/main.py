import os
import csv

# ------ PyPoll main solution -------
#Files and paths
election_data_csv = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Resources", "election_results.txt")

# Create dictionaries to store the vote counts and percentages
candidate_votes = {}
candidate_percentages = {}

# defining variables
total_votes = 0

# open and read the CSV file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(csv_reader)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Increment the total vote count
        total_votes += 1

        # Locating the candidate name from the row
        candidate = row[2]

        # If the candidate is already in the dictionary, increase their vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        # If the candidate is not in the dictionary, add them with an initial vote count of 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100 #divide and multiply by 100, into percentage
    candidate_percentages[candidate] = percentage

# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis results to a text file
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-------------------------"])
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        writer.writerow([f"{candidate}: {percentage:.3f}% ({votes})"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])

print("Results exported to:", output_file)
