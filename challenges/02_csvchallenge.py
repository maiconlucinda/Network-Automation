import csv

# Challenge #1
# Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv. After writing into the file, read and print out the file contents. Use the default , (comma) as the delimiter.

with open('archives/people1.csv', 'w') as ourfile:
    writer = csv.writer(ourfile)

    csvdata = [['Dan', 34, 'Bucharest'], ['Andrei',21, 'London'], ['Maria', 45, 'Paris']]

    for item in csvdata:
        writer.writerow(item)


with open('archives/people1.csv', 'r') as ourfile:
    reader = csv.reader(ourfile)

    for item in reader:
        print(item)





# Challenge #2
# Change the solution from the previous challenge and use : (colon) as the delimiter.
with open('archives/people2.csv', 'w') as ourfile:
    writer = csv.writer(ourfile,delimiter=':')

    csvdata = [['Dan', 34, 'Bucharest'], ['Andrei',21, 'London'], ['Maria', 45, 'Paris']]

    for item in csvdata:
        writer.writerow(item)

with open('archives/people2.csv', 'r') as ourfile:
    reader = csv.reader(ourfile, delimiter=':')

    for row in reader:
        print(row)