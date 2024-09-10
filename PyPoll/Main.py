import csv
import os
# create path to folder 
file_path = os.path.join("Resources","election_data.csv")
file_output = os.path.join("Analysis","election_analysis.txt")



# Check if the input file exists
if not os.path.exists(file_path):
    print(f"Error: The file {file_path} was not found.")
else:
    # Open and read the CSV file
    with open(file_path, 'r') as file:
        elect_reader = csv.reader(file)
        header = next(elect_reader)
    
        # Initialize variables
        total_votes = 0
        candidates = {}
        percent_won=[]
        total_won=[]
        winner=("", 0)
        
    # Count votes and collect candidates
        for row in elect_reader:
            total_votes += 1
            candidate = row[2].strip()  # Candidate is in the third column
        # Increment vote count for the candidate
            if candidate in candidates:
                    candidates[candidate] += 1
            else:
                    candidates[candidate] = 1

        # Determine the winner
        winner = max(candidates, key=candidates.get)

        # Prepare the output
        output = []
        output.append("Election Results")
        output.append("-------------------------")
        output.append(f"Total Votes: {total_votes}")
        output.append("-------------------------")

        # Calculate and print the results for each candidate
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            output.append(f"{candidate}: {percentage:.3f}% ({votes})")

        output.append("-------------------------")
        output.append(f"Winner: {winner}")
        output.append("-------------------------")

        # Print the results to the terminal
        for line in output:
            print(line)

        # Write the results to the output file
        with open(file_output, 'w') as file:
            for line in output:
                file.write(line + "\n")

# Print confirmation
print(f"Results have been written to {file_output}")