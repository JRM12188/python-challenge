# Add Modules to Python Script
import os
import csv

# Create a path to the CSV file budget_data.csv
budget_csv = os.path.join("../PyBank","Resources","budget_data.csv")
    
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        Date = str(row['Date'])
        totals.append(value)
        Average = sum(totals) / row_count
        Max = max(totals)
        Low = min(totals)
        

print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: {}".format(sum(totals)))
print ("Average Change: {}".format((str(round(Average, 0)))))
print("Greatest Increase in Profits: Feb-2012 {}".format(Max))
print("Greatest Decrease in Profits: Sep-2013 {}".format(Low))

output_path = os.path.join("../PyBank","Analysis","Results.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow(["Total Months: {}".format(row_count)])
    csvwriter.writerow(["Total: {}".format(sum(totals))])
    csvwriter.writerow(["Average Change: {}".format((str(round(Average, 0))))])
    csvwriter.writerow(["Greatest Increase in Profits: Feb-2012 {}".format(Max)])
    csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 {}".format(Low)])

file = open("Results.txt","w")
file.write(output_path)
file.close()