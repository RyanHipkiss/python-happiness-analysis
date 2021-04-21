from utils import Json

class Data:
    def __init__(self, country, gender, mean):
        self.country = country
        self.gender = gender
        self.mean = mean

DataList = []
lastCountry = ""
import csv
with open('happiness.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:

        if not row[0]:
            country = lastCountry
        else:
            country = row[0]

        lastCountry = country
        DataList.append(Data(country, row[1], row[2]))

countryMeans = {}

for item in DataList:
    if not countryMeans.get(item.country):
        countryMeans[item.country] = {}

    countryMeans[item.country][item.gender] = item.mean


x = Json(countryMeans, 'results.json')
x.save()

