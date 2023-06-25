import os
import csv

# ----- PyBank main solution -----
# Setting paths for csv files
budget_data_csv = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Resources", "financial_analysis.txt")

# Open and read the CSV file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header row so it isn't read by the csv reader with next function
    next(csv_reader)

# Define lists
    dates = []
    profit_losses = []

    # Extracting the dates and profit/losses
    for row in csv_reader:
        date = row[0]
        dates.append(date)
        profit_loss = int(row[1])
        profit_losses.append(profit_loss)

    # Calculating total months by using the len function
    total_months = len(dates)
    total_profit_losses = sum(profit_losses)

    print("Total months:", total_months)
    print("Total: $", total_profit_losses)

    # Calculating the average change
    changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
    average_change = sum(changes) / len(changes)

    # Print the financial analysis into terminal
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:", total_months)
    print("Total: $", total_profit_losses)
    print("Average Change: $", round(average_change, 2))

    # Finding the greatest increase in profits (date and amount)
    max_increase = max(changes)
    max_increase_index = changes.index(max_increase) + 1
    max_increase_date = dates[max_increase_index]

    print("Greatest Increase in Profits:", max_increase_date, "($", max_increase, ")")

    # Calculating greatest decrease in profits (date and amount)
    max_decrease = min(changes)
    max_decrease_index = changes.index(max_decrease) + 1  # Add 1 to the index since changes list has one less
    max_decrease_date = dates[max_decrease_index]  # Get the correct month for the index
    max_decrease_amount = max_decrease

    print("Greatest Decrease in Profits:", max_decrease_date, "($", max_decrease_amount, ")")

 # Exporting the results to a text file using writer csv file function
    with open(output_file, "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["-------------------------"])
        writer.writerow([f"Total Months: {total_months}"])
        writer.writerow([f"Total: ${total_profit_losses}"])
        writer.writerow([f"Average Change: ${round(average_change, 2)}"])
        writer.writerow([f"Greatest Increase in Profits: {max_increase_date} (${max_increase})"])
        writer.writerow([f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount})"])
