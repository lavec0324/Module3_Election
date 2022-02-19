from asyncore import write
import csv
import os
from tkinter import N

#Assign variable to load a file from a path
file_to_load = os.path.join('Resources/election_results.csv')
                            
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Votes Accumulator Initialized
Total_votes = 0

#Declare new list of candidate names
candidate_options = []

#Declare new list of county names
county_options = []

#Declare Candidate dictionary to accumulate votes
candidate_votes = {}

#Declare County dictionary to accumulate votes
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Ignore Headers
    headers = next(file_reader)
    
    #Loop through rows
    for row in file_reader:
         
        #Increment in loop
        Total_votes += 1
        
        #Add Candidate Name and County to list only if unique

        candidate_county = row[1]
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
                                    
            #Begin tracking that candidates's vote count
            candidate_votes[candidate_name] = 0
                        
        #Increment Votes
        candidate_votes[candidate_name] += 1
       
        if candidate_county not in county_options:
            county_options.append(candidate_county)
            
            #Begin tracking that counties vote count
            county_votes[candidate_county] = 0
               
        #Increment County Votes
        county_votes[candidate_county] += 1
  
#Write election results and county headers to text file
with open(file_to_save,"w") as txt_file:
        
    election_results = (
    f"\nElection Results\n"
    f"--------------------------------\n"
    f"Total Votes: {Total_votes:,}\n"
    f"--------------------------------\n"
    f"\n"   
    f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
   
                    
    #Read ccounty dictionary to grab county, counts, and calculate percents
    
    for county_name in county_votes: 
        votes_county = county_votes[county_name]
        vote_percentage_county = float(votes_county) / float(Total_votes) * 100
            
        #County results
        county_results = (f"{county_name} {vote_percentage_county:.1f}% ({votes_county:,})")
        print(county_results)
        county_results = county_results + "\n"
        txt_file.write(county_results)

        #Determine winning candidates and set votes and count
        if (votes_county > winning_county_count) and (vote_percentage_county > winning_county_percentage):
            winning_county = county_name
            winning_county_count = votes_county
            winning_county_percentage = vote_percentage_county

    #Print the highest county turnout
    highest_turnout_county = (
        f"\n"
        f"--------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------------\n"
        f"\n")
    print(highest_turnout_county, end="")
        
    highest_turnout_county2 = (
        f"\n"
        f"--------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------------\n")
    txt_file.write(highest_turnout_county2)

    
    
    #Read candidate dictiionary to grab name, counts, and calculate percents
    for candidate_name in candidate_votes:

        votes_candidate = candidate_votes[candidate_name]
        vote_percentage_candidate = float(votes_candidate) / float(Total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        #Candidate results
        candidate_results = (f"{candidate_name} {vote_percentage_candidate:.1f}% ({votes_candidate:,})\n")
            
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
               
         #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
          
        #Determine winning candidates and set votes and count
        if (votes_candidate > winning_count) and (vote_percentage_candidate > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes_candidate
            winning_percentage = vote_percentage_candidate
    
    #Print the winning candidate  info
    winning_candidate_summary = (
    f"--------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------\n")
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)
    
