
import json
import csv
import requests

request = requests.get("https://jsonplaceholder.typicode.com/users")

#print(request.text)
data = json.loads(request.text)


with open('archives/employees.csv', 'a') as f:
    
    for item in data:
        name = item['name']
        city = item['address']['city']
        lat = item['address']['geo']['lat']
        lng = item['address']['geo']['lng']
        geo = f"({lat},{lng})"
        company = item['company']['name']
    
        csvdata = (name, city, geo, company)
        writer = csv.writer(f)
        writer.writerow(csvdata)




#print(data[9])
# my_list = list()
# for item in data:
    
