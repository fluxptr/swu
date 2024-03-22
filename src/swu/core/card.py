
class CardBase:
    def __init__(self, data):
        self.set = data['Set']
        self.number = data['Number']
        self.id = f"{self.set} - {self.number}"

        self.name = data['Name']
        self.subtitle = data.get('Subtitle', '')
        self.fullname =  f"{self.name} - {self.subtitle}" if len(self.subtitle) > 0 else self.name
        
        self.type = data['Type']
        self.aspects = [] # TODO
        self.traits = [] # TODO
        self.arena = '' # TODO
        self.cost = data.get('Cost', 0)
        self.power = data.get('Power', 0)
        self.HP = data.get('HP', 0)
        # TODO text, actions
        self.doublesided = data.get('DoubleSided', False)
        self.rarity = data['Rarity']
        self.unique = data.get('Unique', False)
        