import os
import csv

#define a function to check whether the string in 2nd column is an integer
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False
datafiles = ["budget_data_1", "budget_data_2"]
for data in datafiles:
    #Reading csv file
    pybank = os.path.join("raw_data", data+".csv")
    with open(pybank, newline="") as csvfile:

        csvreader= csv.reader(csvfile, delimiter=",")

        #initialze variables
        total_months = 0
        total_revenue = 0
        revenue_change = 0
        first_row = 0
        second_row = 0
        counter = 0
        revenue_difference_list = []
        revenue_lookup = {}
        for row in csvreader:   
            #finding total no of months
            total_months = total_months + 1
            #calculating total revenue
            if row[1].isdigit():
                total_revenue = total_revenue + int(row[1])
            #finding revenue increase
            if is_digit(row[1]):
                first_row = second_row
                second_row = int(row[1])
                if counter >= 2:
                    revenue_difference = (second_row - first_row)
                    revenue_difference_list.append(revenue_difference)
                    month = row[0]
                    revenue_lookup[month]=revenue_difference
                    #calculating the average revenue_change
                    revenue_change = revenue_change + revenue_difference      
                    average_revchange = revenue_change/(total_months-1) 
            counter  = counter + 1
        
        #Printing summary values
        print(data)
        print(f"Total Months: {total_months}")    
        print(f"Total Revenue: ${total_revenue}")    
        print(f"Average Revenue Change: {average_revchange}")   

        # Finding the greatest revenue_increase and decrease
        greatest_revincrease = max(revenue_difference_list)      
        greatest_revdecrease = min(revenue_difference_list)    

        #for loop for finding the month corresponding to the gretest_increase and greatest_decrese in revenue
        for key, value in revenue_lookup.items():
            if greatest_revincrease == value:
                month_revincrease = key, greatest_revincrease
                print(f"Greatest Increase in Revenue: {month_revincrease}")
            if greatest_revdecrease == value:
                month_revdecrease = key, greatest_revdecrease
                print(f"Greatest Decrease in Revenue: {month_revdecrease}")

    #Creating a list of output results
    output_results = ["FINANCIAL ANALYSIS",f"Total Months: {total_months}",f"Total Revenue: ${total_revenue}",f"Average Revenue Change: {average_revchange}", f"Greatest Increase in Revenue: {month_revincrease}", f"Greatest Decrease in Revenue: {month_revdecrease}"  ]
    
    # path for the output file
    output_file = os.path.join("final_output_" + data + ".txt")

    #  Open the output file
    with open(output_file,"w") as text:
    
        for x in output_results:
            text.write(str(x))
            text.write("\n")


            
            
