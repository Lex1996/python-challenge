#importing the os module
import os

#importing the module to read csv files
import csv

#setting a path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Reading the CSV header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    #setting the variables for the calculations

    months = 0              #Variable to calculate the total number of months
    pl = 0                  #Variable for the initial Profit/Loss 
    prevpl = 0              #Variable for the previous Profit/Loss
    total_change = 0        #Variable to calculate the total change in Profit/Loss
    greatest_incr = 0       #Variable for the greatest increase in Profit/Loss
    greatest_decr = 0       #Variable for the greatest decrease in Profit/Loss

    #creating a space to store data

    greatest_incdate = ""   #Space to store the date corresponding to the greatest increase in Profit/Loss
    greatest_decdate = ""   #Space to store the date corresponding to the greatest decrease in Profit/Loss
    

    for row in csvreader:

        # assigning a variable to each column in the csv file
        date = row[0]
        profit_loss = int(row[1])

        #Setting initial designations for calculation of change in Profit/Loss
        months += 1
        pl += profit_loss

        #CALCULATION BEGINS

        if months > 1:
            change = profit_loss - prevpl   #Calculation of change in Profit/Loss
            total_change += change          #To find sum of change (to find the average)

            # Calculation for greatest increase in change
            if change > greatest_incr:
                greatest_incr = change
                greatest_incrdate = date

            # Calculation for greatest decrease in change
            if change < greatest_decr:
                greatest_decr = change
                greatest_decrdate = date

        prevpl = profit_loss

average_change = total_change / months

# Formating answers
total = "{:,.2f}".format(pl)
avg = "{:,.2f}".format(average_change)
incr = "{:,.2f}".format(greatest_incr)
decr = "{:,.2f}".format(greatest_decr)

# Printing the result
print("Financial Analysis\n")
print("----------------------------------------\n")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {greatest_incrdate} (${incr})")
print(f"Greatest Decrease in Profits: {greatest_decrdate} (${decr})")

#EXPORTING RESULTS TO A TXT FILE

# Creating a txt file
file = open("financial_analysis_result.txt","w")

# Importing all answers
file.write("Financial Analysis\n\n")
file.write("----------------------------------------\n\n")
file.write(f"Total Months: {months}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${avg}\n")
file.write(f"Greatest Increase in Profits: {greatest_incrdate} (${incr})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrdate} (${decr})\n")
