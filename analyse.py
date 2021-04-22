from generic import Json
from maths import Maths
from objects import CsvToObject, SearchObject

csvObject = CsvToObject('data/happiness.csv').setCsv().convert()
searchObject = SearchObject()

cGenderHappiness = [Maths.float(x) for x in searchObject.retrieveValuesByKey('Both', csvObject)]
mGenderHappiness = [Maths.float(x) for x in searchObject.retrieveValuesByKey('Male', csvObject)]
fGenderHappiness = [Maths.float(x) for x in searchObject.retrieveValuesByKey('Female', csvObject)]

Json.save({
    'global': {
        'means': {
            'both': Maths.mean(cGenderHappiness),
            'female': Maths.mean(fGenderHappiness),
            'male': Maths.mean(mGenderHappiness)
        },
        'both': cGenderHappiness,
        'female': fGenderHappiness,
        'male': mGenderHappiness
    }
}, 'test.json')