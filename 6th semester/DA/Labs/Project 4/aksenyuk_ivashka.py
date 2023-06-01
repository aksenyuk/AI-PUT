import numpy as np
import random
from player import Player

class Aksenyuk_Ivashka(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards_in_game = [(number, color) for color in range(4) for number in range(9, 15)]
        self.ARTIFICIAL_CARD = 99
        self.ERROR_COST = 3
        self.bluff_epsilon = 0.5
        self.check_epsilon = 0.3
        self.bluff_flag = False
        self.check_flag = False
        self.prev_num_cards = 0
    

    def putCard(self, declared_card):

        if self.check_flag:
            self.adjust_check_rate()
            self.check_flag = False

        if declared_card in self.cards_in_game:
            self.cards_in_game.remove(declared_card)

        if not declared_card:
            card_to_play = self.get_min_card()
            if card_to_play in self.cards_in_game:
                self.cards_in_game.remove(card_to_play)
            return card_to_play, card_to_play

        if len(self.cards) == 1:
            last_card = self.cards[0]
            if last_card[0] >= declared_card[0]:
                return last_card, last_card
            else:
                return "draw"

        card_values = np.array(self.cards)[:, 0]
        higher_card_idx = np.argmin(np.where(card_values >= declared_card[0], card_values, self.ARTIFICIAL_CARD))
        if card_values[higher_card_idx] != self.ARTIFICIAL_CARD:
            card_to_play = self.cards[higher_card_idx]
            if card_to_play[0] >= declared_card[0]:
                if card_to_play in self.cards_in_game:
                    self.cards_in_game.remove(card_to_play)
                return card_to_play, card_to_play
        
        if np.random.rand() < self.bluff_epsilon:
            card_to_play = self.get_min_card()
            if card_to_play in self.cards_in_game:
                self.cards_in_game.remove(card_to_play)
            bluff_cards = [card for card in self.cards_in_game if card[0] >= declared_card[0]]
            self.bluff_flag = True
            self.prev_num_cards = len(self.cards)
            if len(bluff_cards):
                return card_to_play, random.choice(bluff_cards)
            else:
                return card_to_play, random.choice(self.cards_in_game)

        return "draw"


    def checkCard(self, opponent_declaration):

        if self.bluff_flag:
            self.adjust_bluff_rate()
            self.bluff_flag = False

        if opponent_declaration in self.cards_in_game:
            self.cards_in_game.remove(opponent_declaration)
        else:
            return True
        
        if np.random.rand() < self.check_epsilon:
            self.check_flag = True
            self.prev_num_cards = len(self.cards)
            return True
        else:
            return False


    def adjust_bluff_rate(self):
        if len(self.cards) - self.prev_num_cards == self.ERROR_COST:
            self.bluff_epsilon -= 0.01
        else:
            self.bluff_epsilon += 0.01
        self.bluff_epsilon  = max(0, min(1, self.bluff_epsilon))
        self.prev_num_cards = len(self.cards)


    def adjust_check_rate(self):
        if len(self.cards) - self.prev_num_cards == self.ERROR_COST:
            self.check_epsilon -= 0.01
        else:
            self.check_epsilon += 0.01
        self.check_epsilon  = max(0, min(1, self.check_epsilon))
        self.prev_num_cards = len(self.cards)


    def get_min_card(self):
        min_card_idx = np.argmin(self.cards, axis=0)[0]
        card_to_play = self.cards[min_card_idx]
        return card_to_play
    

    def get_max_card(self):
        max_card_idx = np.argmax(self.cards, axis=0)[0]
        card_to_play = self.cards[max_card_idx]
        return card_to_play
    

    def startGame(self, cards):
        self.cards = cards
        self.prev_num_cards = len(self.cards)
        for card in cards:
            if card in self.cards_in_game:
                self.cards_in_game.remove(card)

    
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take
        for card in cards_to_take:
            if card in self.cards_in_game:
                self.cards_in_game.remove(card) 