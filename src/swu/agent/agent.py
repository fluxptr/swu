from swu.engine.state import Game
from swu.engine.enum import ActionPass
from swu.core import Deck

class Agent:
    def __init__(self, deck: Deck):
        self.deck = deck

    def resrouce_setup(self, game: Game):
        pass

    def resource_card(self, game: Game):
        pass

    def take_action(self, game: Game):
        pass


class RandomAgent(Agent):
    def resource_setup(self, game: Game):
        return [0,1]
    
    def resource_card(self, game: Game):
        return -1
    
    def take_action(self, game: Game):
        return ActionPass()
    