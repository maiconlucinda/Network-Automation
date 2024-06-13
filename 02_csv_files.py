

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




with open('archives/passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter='/', lineterminator='\n')

    for row in reader:
        print(row)
print('#' * 80)



# We can also create a type of dialect, this is basically a way of explaning the code some characteristcs of our document
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('archives/items.csv', 'r') as file:
    reader = csv.reader(file, dialect='hashes')

    for row in reader:
        print(row)


with open('archives/items.csv', 'a') as file:
    reader = csv.reader(file)

    writer = csv.writer(file, dialect='hashes')
    writer.writerow(('spon', 3, 1.5))
print('#' * 80)







# ASSINEMENT
with open('archives/devices2.txt', 'r') as file:
    content = file.read().splitlines()

    devices = list()
    for device in content:
        devices.append(device.split(":"))

    print(devices)
    
