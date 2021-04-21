class Json:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
    
    def save(self):
        import json
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)