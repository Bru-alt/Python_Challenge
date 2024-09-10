import csv
import os
# create path to folder 
file_path = os.path.join("Resources","budget_data.csv")
file_output = os.path.join("Analysis","budget_analysis.txt")

# Open and read the CSV file
# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: {file_path} does not exist.")
else:
    # Open and read the CSV file
    with open(file_path, mode='r') as file:
        budget_reader = csv.reader(file)

        # Read and print the header
        header = next(budget_reader)
        #print(header)
        
        # Initialize variables
        total_months = 0
        net_total = 0
        prev_value = None  # To store the previous month's Profit/Losses

        month_of_change = []
        net_change_list = []
        greatest_increase = ["", 0]
        greatest_decrease = ["", 0]

        # Loop through each row in the data
        for row in budget_reader:
            # Track the total number of months
            total_months += 1
            current_value = int(row[1])  # Current month's profit/loss

            # Track the net total profit/loss
            net_total += current_value

            # Calculate the monthly change if not the first month
            if prev_value is not None:
                change = current_value - prev_value
                net_change_list.append(change)
                month_of_change.append(row[0])

                # Check if this is the greatest increase
                if change > greatest_increase[1]:
                    greatest_increase = [row[0], change]

                # Check if this is the greatest decrease
                if change < greatest_decrease[1]:
                    greatest_decrease = [row[0], change]

            # Updating previous value to the current value
            prev_value = current_value

    # Print results 
    with open(file_output, mode='w') as file:
        file.write("Financial Analysis\n")
        file.write("-----------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Net Total: ${net_total}\n")
        if net_change_list:
            average_change = sum(net_change_list) / len(net_change_list)
            file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n")
        file.write(f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

    print(f"Results have been written to {file_output}")
        
    