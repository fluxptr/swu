import os
import json

from .card import CardBase

class Database:
    def __init__(self, path):
        self.path = path
        self.cards = self.load_sets(path)

        self.cards_by_name = {}
        self.cards_by_id = {}
        for card in self.cards:
            self.cards_by_name[card.fullname] = card
            self.cards_by_id[card.id] = card

    def load_sets(self, directory_path):
        cards = []
        for filename in os.listdir(directory_path):
            if filename.endswith(".json"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, "r") as f:
                    try:
                        data = json.load(f)
                        for card in data:
                            cards.append(CardBase(card))
                    except json.JSONDecodeError:
                        print(f"Error parsing JSON file: {filename}")
        return cards
