#Import required libraries
import os
import csv
#Define csv path
pypoll = os.path.join("raw_data", "election_data_2.csv")
output_file = os.path.join("final_output.txt")

#Open csv file
with open(pypoll, newline="") as csvfile:

    csvreader= csv.reader(csvfile, delimiter=",")

    #Initialise total_votes
    total_votes = 0

    #Create a dictionary to get # of votes for each candidate, percentage votes
    candidate_names_lookup = {}

    #Create a list for storing the values
    candidate_list = []
    
    for row in csvreader:
        total_votes = total_votes + 1

        #conditonals to find out # of votes for each candidate
        if candidate_names_lookup.get(row[2]):
            candidate_names_lookup[row[2]] = candidate_names_lookup[row[2]] +  1
        else:
            candidate_names_lookup[row[2]] = 1
    #condition to get the total number of votes, percentage votes for each candidate  
    for key, value in candidate_names_lookup.items():
        percentage_votes =(value/total_votes)*100
        percentage_votes_roundup = round(percentage_votes,4)

        #adding the values to candidate list
        candidate_list.append(key + ": " + str(percentage_votes_roundup) + "% " + "(" + (str(value) + ")"))

    #Finding the max no of votes by candidate to determine winner
    winner = max(candidate_names_lookup, key=candidate_names_lookup.get)

    with open(output_file,"w") as text:
        #Summary
        print("ELECTION RESULTS")
        print("--------------------------")
        print(f"Total Votes Cast: {total_votes}")
        text.write(f"Total Votes Cast: {total_votes}\n")   
        print("--------------------------") 
        
        for candidate in candidate_list:
            print(candidate) 
            text.write(str(candidate))
            text.write("\n") 
              
        print("--------------------------")  
        print(f"Winner: {winner}")
        text.write(f"Winner: {winner}") 
        print("--------------------------")
