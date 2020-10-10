
import os
import csv


election_csv = os.path.join("../PyPoll","Resources", "election_data.csv")

count = 0

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row_count, row in enumerate(csvreader, start=1):
        
        count = sum(1 for row in csvreader if row ['Candidate'] == 'Khan')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row_count, row in enumerate(csvreader, start=1):
        count1 = sum(1 for row in csvreader if row ['Candidate'] == 'Correy')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row_count, row in enumerate(csvreader, start=1):
        count2 = sum(1 for row in csvreader if row ['Candidate'] == 'Li')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row_count, row in enumerate(csvreader, start=1):

        count3 = sum(1 for row in csvreader if row ['Candidate'] == 'OTooley')
        value = count + count1 + count2 + count3

        KPer = round((count / value) * 100,0)
        CPer = round((count1 / value) * 100,0)
        LPer = round((count2 / value) * 100,0)
        OPer = round((count3 / value) * 100,0)

print ("Election Results")
print ("-------------------------------")
print ("Total Votes:{}".format(value))
print ("-------------------------------")
print ("Khan: {}".format(count))
print ("Khan Percentage {}".format(KPer) + "%")
print ("Correy:{}".format(count1))
print ("Correy Percentage {}".format(CPer) + "%")
print ("Li:{}".format(count2))
print ("Li Percentage {}".format(LPer) + "%")
print ("O'Tooley:{}".format(count3))
print ("O'Tooley Percentage {}".format(OPer) + "%")
print ("-------------------------------")
print ("Winner: Khan")
print ("-------------------------------")

output_path = os.path.join("../PyPoll","Analysis","Results.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow(["Total Votes:{}".format(value)])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow(["Khan: {}".format(count)])
    csvwriter.writerow(["Khan Percentage {}".format(KPer) + "%"])
    csvwriter.writerow(["Correy:{}".format(count1)])
    csvwriter.writerow(["Correy Percentage {}".format(CPer) + "%"])
    csvwriter.writerow(["Li:{}".format(count2)])
    csvwriter.writerow(["Li Percentage {}".format(LPer) + "%"])
    csvwriter.writerow(["O'Tooley:{}".format(count3)])
    csvwriter.writerow(["O'Tooley Percentage {}".format(OPer) + "%"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow(["Winner: Khan"])
    csvwriter.writerow(["-------------------------------"])
file = open("Results.txt","w")
file.write(output_path)
file.close()

