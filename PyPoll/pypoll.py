#importing the os module
import os

#importing the module to read csv files
import csv

#setting a path for the csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Creating a txt file
file = open("election_results.txt","w")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Reading the CSV header
    csv_header = next(csvreader)

    # Setting the variables for the calculations

    total_votes = 0     # Variable that stores the total number of votes casted
    dict = {}           # Creating a space (dictionary) to store the Candidate Name and the corresponding number of votes

    for row in csvreader:

        # assigning a variable for the Candidate name in the csv file
        name = row[2]

        # CALCULATIONS BEGIN

        # Calculating the total number of votes
        total_votes += 1
        
        # Finding the unique Candidate names and calculating their individual number of votes
        if name in dict:

            dict[name] += 1

        else:

            dict[name] = 1

    # PRINTING RESULTS FOR THE CODE AND FOR THE TXT FILE
    
    print("Election Results\n")
    file.write("Election Results\n\n")
    print("----------------------------------------\n")
    file.write("----------------------------------------\n\n")
    print(f"Total votes: {total_votes}\n")
    file.write(f"Total votes: {total_votes}\n\n")
    print("----------------------------------------\n\n")
    file.write("----------------------------------------\n\n")

    # Iterating through the dictionary to get individual results
    for name in dict:

        # Calculating the percentage of individual votes
        percentage = dict[name]/total_votes * 100

        # Formating the individual total number of votes
        votes = "{:,}".format(dict[name])

        # Printing the required results
        print(f"{name}: {percentage:.3f}% ({votes})")
        file.write(f"\n{name}: {percentage:.3f}% ({votes})\n")
    
    print("\n----------------------------------------\n")
    file.write("\n----------------------------------------\n\n")

    # Iterating through the dictionary to get the Winner

    # Providing variables to start calculations

    winner = ""     # Variable to store the name of the winning candidate
    max = 0         # Variable to store the number of votes of the winning candidate
    
    for name in dict:

        # Calculating the number of votes corresponding to a candidate
        votes_max = dict.get(name)

        # Iteration
        if votes_max > max:
            max = votes_max
            winner = name

    #Printing the winner
    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}")
