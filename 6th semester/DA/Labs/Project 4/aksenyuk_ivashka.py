import numpy as np
import random
from player import Player


class Aksenyuk_Ivashka(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.potential_opponents_cards = [(number, color) for color in range(4) for number in range(9, 15)]
        self.cards_in_pile = []
        self.ACE = 14
        self.bluff_epsilon = 0.3
        self.check_epsilon = 0.3
        self.bluff_flag = False
        self.check_flag = False
        self.prev_num_cards = 99
    

    def putCard(self, declared_card):
        self.adjust_opponent_cards(declared_card)
        
        if declared_card:
            self.cards_in_pile.append(declared_card)
            if declared_card in self.potential_opponents_cards:
                self.potential_opponents_cards.remove(declared_card)

        if self.bluff_flag:
            self.adjust_bluff_rate()
            self.bluff_flag = False
        self.prev_num_cards = len(self.cards)

        if not declared_card:
            if len(self.cards) > self.prev_num_cards:
                self.adjust_pile()
            else:
                for _ in range(3):
                    if self.cards_in_pile:
                        self.potential_opponents_cards.append(self.cards_in_pile.pop(-1))
            return self.play_min_card()
        
        if not self.cards_in_pile:
            return self.play_min_card()

        if len(self.cards) == 1:
            last_card = self.cards[0]
            if last_card[0] >= declared_card[0]:
                self.cards_in_pile.append(last_card)
                return last_card, last_card
            else:
                self.cards_in_pile = self.cards_in_pile[:max([-3, -len(self.cards_in_pile)])]
                return "draw"
            
        if np.random.rand() < self.bluff_epsilon:
            self.bluff_flag = True
            self.prev_num_cards = len(self.cards)
            card_to_play = self.cheat(declared_card)
            if card_to_play == 'draw':
                return card_to_play
            self.cards_in_pile.append(card_to_play[0])
            return card_to_play

        valid_cards = [card for card in self.cards if card[0] >= declared_card[0]]
        if valid_cards:
            card_to_play = self.get_min_card(valid_cards)
            self.cards_in_pile.append(card_to_play)
            return card_to_play, card_to_play
        else:
            self.bluff_flag = True
            card_to_play = self.cheat(declared_card)
            if card_to_play == 'draw':
                return card_to_play
            self.cards_in_pile.append(card_to_play[0])
            return card_to_play
            
            
    def cheat(self, opponent_card):
        card_to_play = self.get_min_card()
        cards_to_bluff = [card for card in self.cards if card[0] >= opponent_card[0]]
        if not cards_to_bluff:
            cards_to_bluff = [card for card in self.potential_opponents_cards if card[0] >= opponent_card[0]]

        if cards_to_bluff:
            return card_to_play, random.choice(cards_to_bluff)
        
        elif opponent_card[0] == self.ACE:
            aces_left = [card for card in self.potential_opponents_cards if card[0] == self.ACE]
            if aces_left:
                return card_to_play, random.choice(aces_left)
            else:
                return 'draw'
        else:
            next_card = (opponent_card[0]+1, random.choice(range(4)))
            return card_to_play, next_card


    def play_min_card(self):
        card_to_play = self.get_min_card()
        self.cards_in_pile.append(card_to_play)
        return card_to_play, card_to_play
    

    def adjust_opponent_cards(self, declared_card):
        if declared_card and declared_card in self.potential_opponents_cards:
            self.potential_opponents_cards.remove(declared_card)
    

    def checkCard(self, opponent_declaration):
        if self.check_flag:
            self.adjust_check_rate(opponent_declaration)
            self.check_flag = False

        if opponent_declaration in self.potential_opponents_cards:
            self.potential_opponents_cards.remove(opponent_declaration)

        if opponent_declaration in self.cards_in_pile or opponent_declaration in self.cards:
            self.check_flag = True
            return True

        if np.random.rand() < self.check_epsilon:
            self.check_flag = True
            return True
        else:
            return False

    
    def adjust_bluff_rate(self):
        if len(self.cards) > self.prev_num_cards:
            self.adjust_pile()
            self.bluff_epsilon -= 0.1
        else:
            self.bluff_epsilon += 0.05
        self.bluff_epsilon  = max(0, min(1, self.bluff_epsilon))
        self.prev_num_cards = len(self.cards)


    def adjust_check_rate(self, opponent_declaration):
        if len(self.cards) > self.prev_num_cards:
            self.check_epsilon -= 0.1
        elif opponent_declaration in self.cards or opponent_declaration in self.cards_in_pile:
            self.check_epsilon += 0.05
        else:
            self.check_epsilon += 0.05
        self.check_epsilon = max(0, min(1, self.check_epsilon))
        self.prev_num_cards = len(self.cards)



    def get_min_card(self, cards=None):
        if not cards:
            cards = self.cards
        min_card_idx = np.argmin(cards, axis=0)[0]
        card_to_play = cards[min_card_idx]
        return card_to_play
    
    
    def adjust_pile(self):
        for card in self.cards:
            if card in self.cards_in_pile:
                self.cards_in_pile.remove(card)


    def startGame(self, cards):
        self.cards = cards
        self.prev_num_cards = len(self.cards)
        for card in cards:
            self.potential_opponents_cards.remove(card)
    
    
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take
        for card in cards_to_take:
            if card in self.potential_opponents_cards:
                self.potential_opponents_cards.remove(card)
            if card in self.cards_in_pile:
                self.cards_in_pile.remove(card)
