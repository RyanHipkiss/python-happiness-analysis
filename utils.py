class Json:
    @staticmethod
    def save(data, filename):
        import json
        with open(filename, 'w') as file:
            json.dump(data, file)

class Data:
    def __init__(self, country, gender, mean):
        self.country = country
        self.gender = gender
        self.mean = mean


from math import log10, floor
#Math functions
class Maths:
    @staticmethod
    def mean(values):
        return sum(values) / len(values)

    @staticmethod
    def sigfig(number, sf=3):
        return round(number, sf-int(floor(log10(abs(number))))-1)

class SearchObject:
    def retrieveValuesByKey(self, key, data):
        values = []
        for item in data:
            values.append(
                float(data.get(item).get(key))
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

    