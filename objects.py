from generic import Data 

class SearchObject:
    def retrieveValuesByKey(self, key, data):
        values = []
        for item in data:
            if item is key:
                values.append(data.get(item))
            elif data.get(item).get(key):
                values.append(
                    data.get(item).get(key)
                )
        
        return values


class CsvToObject:
    def __init__(self, filename):
        self.data = []
        self.convertedData = []
        self.filename = filename
                
    def setCsv(self):
        import csv 
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                self.data.append(row)

        return self

    def convert(self):
        lastCountry = ""
        DataList = []

        for data in self.data:
            if not data[0]:
                country = lastCountry
            else:
                country = data[0]

            lastCountry = country
            DataList.append(Data(country, data[1], data[2]))
        
        countryMeans = {}
        for item in DataList:
            if not countryMeans.get(item.country):
                countryMeans[item.country] = {}
            countryMeans[item.country][item.gender] = item.mean

        self.convertedData = countryMeans
        return self.convertedData

    