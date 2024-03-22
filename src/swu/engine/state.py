# pylint: disable=multiple-statements
# pylint: disable=too-many-instance-attributes

import random

from swu.core import CardBase

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.active_player = None
        self.initiative_player = None

        self.round = 0
        self.phase = None

        self.initiative_taken = False

class Player:
    def __init__(self):
        self.deck = Deck()
        self.discard = Discard()
        self.hand = Hand()
        self.space = Space()
        self.ground = Ground()

        self.leader = Leader()
        self.base = Base()
        self.resources = Resources()

        self.sideboard = Sideboard()

        self.resource_actions = 1
        self.passed = False

class Card:
    def __init__(self, card: CardBase, owner: Player):
        self.card = card
        self.owner = owner
        self.is_ready = False

    def ready(self):
        self.is_ready = True

    def exhaust(self):
        self.is_ready = False

    def actions(self):
        return []

class Zone:
    def __init__(self):
        self.cards = []

    def actions(self, game: Game):
        actions = []
        for card in self.cards:
            actions.extend(card.actions(game))

class Deck(Zone):
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

    def peek(self, index: int) -> Card:
        return self.cards[len(self.cards) - 1 - index]

    def actions(self, game: Game):
        return []

class Discard(Zone): pass
class Hand(Zone): pass

class Space(Zone): pass
class Ground(Zone): pass

class Base(Zone): pass
class Leader(Zone): pass

class Resources(Zone): pass

class Sideboard(Zone): 
    def actions(self, game: Game):
        return []
