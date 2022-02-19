import csv
import os
from typing import Counter

#Assign variable to load a file from a path
file_to_load = os.path.join('Resources/election_results.csv')
                            
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Votes Accumulator Initialized
Total_votes = 0

#Declare new list of candidate names
candidate_options = []

#Declare Candidate dictionary to accumulate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Ignore Headers
    #headers = next(file_reader)
  
    row_counter = 0
    #Loop through rows
    for row in file_reader:
        #row_counter = float(row_counter)
        
#print(type(row_counter))
        if row_counter == 0:
            print(row)
        row_counter = row_counter +1
        #print(row_counter)
         
'''        #Increment in loop
        Total_votes += 1
        
        #Add Candidate Name to list only if unique
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
                        
            #Begin tracking that candidates's vote count
            candidate_votes[candidate_name] = 0
            
        #Increment Votes
        candidate_votes[candidate_name] += 1
              # vote_percentage = (candidate_votes / Total_votes) * 100
    
    #Write election results to text file
with open(file_to_save,"w") as txt_file:
        
    election_results = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_votes:,}\n"
    f"----------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
        
    #Read candidate dictiionary to grab name, counts, and calculate percents
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(Total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        #Candidte results
        candidate_results = (f"{candidate_name} {vote_percentage:.1f}% ({votes:,})\n")
            
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
            
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
    
        #Determine winning candidates and set votes and count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
            
    #Print the winning candidate
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    #print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary) '''