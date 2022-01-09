#Open the data file.
#C:\Users\JamesGarner\Desktop\BootCamp\Module 3\Election_Analysis\Resources
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes=0
candidate_options=[]
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percent=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    #print each row in the CSV
    for row in file_reader:
        total_votes += 1

#Write down the names of all the candidates.
        candidate_name=row[2]
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percent=float(votes)/float(total_votes)*100
    #print(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
    canidate_results=(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
    print(canidate_results)
    txt_file.write(candidate_results)
    if (votes > winning_count) and (vote_percent > winning_percent):
        winning_count=votes
        winning_candidate=candidate_name
        winning_percent=vote_percent
winning_candidate_summary=(
    f"----------------------------------\n"
    f"winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"----------------------------------\n")

#print(winning_candidate_summary)



#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election
# Open the election results and read the file
