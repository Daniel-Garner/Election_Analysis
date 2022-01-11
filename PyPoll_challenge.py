# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

file_to_load = 'Resources/election_results.csv'

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

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list=[]
county_votes={}


# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout.
largest_county=""
largest_turnout=0
largest_percentage=0


# 2: Track the largest county and county voter turnout.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            # Add the county name to the county list.
            county_list.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes: {county_votes}\n"
        f"-------------------------\n\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for county_name in county_votes:
            # Retrieve vote count and percentage.
        cnty_votes = county_votes[county_name]
        cnty_percentage = round(float(cnty_votes) / float(total_votes) * 100, 1)
        county_results = (
            f"-------------------------\n"
            f"{county_name}: {cnty_percentage:.1f}% ({cnty_votes:,})\n"
            f"-------------------------\n")

        print(county_results)
#county_percentage = (county_votes/total_votes)*100
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (cnty_votes > largest_turnout):
            largest_turnout = cnty_votes
            largest_county = county_name
            largest_percentage = cnty_percentage
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        txt_file.write(candidate_results)
        #  Save the candidate results to our text file.
       
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    county_turnout_summary=(
        f"-------------------------\n"
        f"Highest Turnout: {largest_county}\n"
        f"Voter Turnout: {largest_turnout}\n"
        f"Turnout Percentage:{largest_percentage:.1f}\n"    
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    print(county_turnout_summary)
    txt_file.write(county_turnout_summary)
    
    # Save the winning candidate's results to the text file.
  