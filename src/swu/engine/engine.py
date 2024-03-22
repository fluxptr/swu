import random

from swu.agent import Agent

from .enum import *
from .state import Game

class Engine:
    def __init__(self, db, agents):
        self.db = db
        self.agents = agents
        self.game = None
        self.active_player_index = 0

    def run(self):
        self.init_game()

        self.phase_setup()

        while True:
            self.game.round += 1 
            print(f'round: {self.game.round}')

            self.game.active_player = self.game.initiative_player

            self.phase_action()
            self.phase_regroup()

            if self.game.round > 10:
                break

        print("game over")

    def init_game(self):
        # init game
        self.game = Game()
        # set base
        # set leader

    def phase_setup(self):
        print("phase setup")
        self.game.phase = PhaseSetup()
        
        self.active_player_index = random.randint(0, len(self.agents)-1)
        self.game.initiative_player = self.game.players[self.active_player_index]

        # shuffle
        # draw(6)
        # mulligan

        # resource 2 cards

    def phase_action(self):
        print("phase action")
        self.game.phase = PhaseAction()

        while True:
            action = self.agents[self.active_player_index].take_action(self.game)
            print(action)
            action_type = type(action)
            if action_type == ActionPlayCard:
                print("play card")
                # play card
                pass
            elif action_type == ActionAbility:
                print("ability")
                # exhuast card, handle ability
                pass
            elif action_type == ActionAttack:
                print("attack")
                # attack
                pass
            elif action_type == ActionTakeInitiative:
                print("initiative")
                # give initiative to player, remove action as possibility
                pass
            elif action_type == ActionPass:
                print("pass")
                self.game.active_player.passed = True
                all_passed = all(player.passed for player in self.game.players)
                for player in self.game.players:
                    print(player.passed)

                if all_passed:
                    break # end action phase
            else:
                print("invalid action")

           # next player action
            self.active_player_index += 1
            if self.active_player_index >= len(self.game.players):
                self.active_player_index = 0

            self.game.active_player = self.game.players[self.active_player_index]

    def phase_regroup(self):
        print("phase regroup")
        self.game.phase = PhaseRegroup()

        # draw 2 cards

        # resource up to 1 card
        for agent in self.agents:
            index = agent.resource_card(self.game)
            # TODO convert hand index into resource

        # ready all cards
        # for leader, ground, space

        # reset state
        for player in self.game.players():
            player.passed = False
            player.resource_actions = 1

        pass
