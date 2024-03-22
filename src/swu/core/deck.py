import json

class Deck:
    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = json.loads(file.read())
            #print(data)
            self.name = data["name"]
            self.leader = data["leader"]
            self.base = data["base"]
            self.cards = data["cards"]
    