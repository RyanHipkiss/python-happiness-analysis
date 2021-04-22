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
