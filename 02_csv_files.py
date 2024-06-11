

# READING CSV FILE
# Open the CSV, read it and performe some maths with the values
import csv

with open('archives/airtravel.csv', 'r') as f:
    reader = csv.reader(f)

    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]

    max_1958 = max(year_1958.values())
    
    for key, value in year_1958.items():
        if max_1958 == value:
            print(f"The busiest month:{key}, flights:{value.strip()}")





# WRITING CSV FILE

with open('archives/people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)

    #we use tuple to add the values that we want to add
    csvdata = (5, "Maicon", "Ireland")

    writer.writerow(csvdata)


with open('archives/numbers_2.csv', 'w') as numbercsv:
    writer = csv.writer(numbercsv)

    writer.writerow(['x', 'x**2, x**3, x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])