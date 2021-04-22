from utils import Json, Maths, CsvToObject, SearchObject

class Data:
    def __init__(self, country, gender, mean):
        self.country = country
        self.gender = gender
        self.mean = mean

x = CsvToObject('happiness.csv')
x.setCsv()
data = x.convert()

z = SearchObject()
data = z.retrieveValuesByKey('Both', data)

Json.save({
    'meanBoth': Maths.sigfig(Maths.mean(data))
}, 'test.json')