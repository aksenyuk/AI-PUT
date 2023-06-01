import traceback

import numpy as np
import random
import logging

class Game():
    def __init__(self, players, log=False):
        self.players = players
        self.deck = self.getDeck()
        self.player_cards = self.getShuffled(self.deck)
        self.game_deck = self.player_cards[0] + self.player_cards[1]

        self.cheats = [0, 0]
        self.moves = [0, 0]
        self.checks = [0, 0]
        self.draw_decisions = [0, 0]

        for i, cards in zip([0, 1], self.player_cards):
            self.players[i].startGame(cards.copy())
            if log:
                print("Player (" + str(i + 1) + "): " + self.players[i].name + " received:")
                print(self.players[i].cards)

        ### Which card is on top
        self.true_card = None
        ### Which card was declared by active player
        self.declared_card = None

        ### Init pile: [-1] = top card
        self.pile = []

        ### Which player moves
        self.player_move = np.random.randint(2)

    def getDeck(self):
        return [(number, color) for color in range(4) for number in range(9, 15)]

    def getShuffled(self, deck):
        D = set(deck)
        A = set(random.sample(deck, 8))
        B = set(random.sample(list(D - A), 8))
        C = D - A - B
        if len(A.intersection(B)) > 0: print("Shuffle error 1")
        if len(A.intersection(B)) > 0: print("Shuffle error 2")
        if len(A.intersection(C)) > 0: print("Shuffle error 3")
        DS = A | B | C
        if not DS == D: print("Shuffle error 4")
        return list(A), list(B), list(C)

    def takeTurn(self, log=False):

        self.player_move = 1 - self.player_move

        if log:
            print("")
            print("")
            print("==== CURRENT STATE ================================")
            print("==== " + self.players[self.player_move].name + " MOVES ====")
            print("Player (0): " + self.players[0].name + " hand:")
            print(self.players[0].cards)
            print("Player (1): " + self.players[1].name + " hand:")
            print(self.players[1].cards)
            print("Pile: ")
            print(self.pile)
            print("Declared top card:")
            print(self.declared_card)
            print("")

        activePlayer = self.players[self.player_move]
        opponent = self.players[1 - self.player_move]
        self.moves[self.player_move] += 1

        self.previous_declaration = self.declared_card
        decision = activePlayer.putCard(self.declared_card)

        if decision == "draw":

            if log: print("[+] " + activePlayer.name + " decides to draw cards")

            self.draw_decisions[self.player_move] += 1

            toTake = self.pile[max([-3, -len(self.pile)]):]
            for c in toTake: self.pile.remove(c)
            activePlayer.takeCards(toTake)
            for c in toTake: self.player_cards[self.player_move].append(c)

            self.declared_card = None
            self.true_card = None

            activePlayer.getCheckFeedback(False, False, False, None, None, log)
            opponent.getCheckFeedback(False, False, False, None, None, log)

        else:
            self.true_card, self.declared_card = decision
            if self.true_card != self.declared_card: self.cheats[self.player_move] += 1

            if log: print("[+] " + activePlayer.name + " puts " + str(self.true_card) +
                          " and declares " + str(self.declared_card))

            if not self.debugMove(): return False, self.player_move

            activePlayer.cards.remove(self.true_card)
            self.player_cards[self.player_move].remove(self.true_card)
            self.pile.append(self.true_card)

            try:
                opponent_check_card = opponent.checkCard(self.declared_card)
            except Exception as e:
                logging.error(traceback.format_exc())
                return False, self.player_move

            if opponent_check_card:

                self.checks[1 - self.player_move] += 1

                if log: print("[!] " + opponent.name + ": " + "I want to check")
                toTake = self.pile[max([-3, -len(self.pile)]):]
                for c in toTake: self.pile.remove(c)

                if not self.true_card == self.declared_card:
                    if log: print("\tYou are right!")
                    activePlayer.takeCards(toTake)

                    activePlayer.getCheckFeedback(True, False, True, None, len(toTake), log)
                    opponent.getCheckFeedback(True, True, False, tuple(toTake[-1]), len(toTake), log)

                    for c in toTake: self.player_cards[self.player_move].append(c)
                else:
                    if log: print("\tYou are wrong!")
                    opponent.takeCards(toTake)

                    activePlayer.getCheckFeedback(True, False, False, None, len(toTake), log)
                    opponent.getCheckFeedback(True, True, True, tuple(toTake[-1]), len(toTake), log)

                    for c in toTake: self.player_cards[1 - self.player_move].append(c)

                if log:
                    print("Cards taken: ")
                    print(toTake)

                self.declared_card = None
                self.true_card = None
            else:
                activePlayer.getCheckFeedback(False, False, False, None, None, log)
                opponent.getCheckFeedback(False, False, False, None, None, log)

        if not self.debugGeneral(): return False, self.player_move
        return True, self.player_move

    def isFinished(self, log=False):
        if len(self.players[self.player_move].cards) == 0:
            if log: print(self.players[self.player_move].name + " wins!")
            return True
        return False

    def debugMove(self):
        if (self.true_card is None):
            print("[ERROR] You had to put any card or Draw.")
            return False
        if (self.previous_declaration is not None) and (self.true_card[0] < self.previous_declaration[0]) and \
                len(self.players[self.player_move].cards) == 1:
            print("[ERROR] Last played card should be valid (it is revealed, you cannot cheat)!")
            return False
        if np.array(self.true_card).size != 2:
            print("[ERROR] You put too many cards!")
            return False
        if self.true_card not in self.player_cards[self.player_move]:
            print("[ERROR] You do not have this card!")
            return False
        if self.true_card not in self.deck:
            print("[ERROR] There is no such card!")
            return False
        if (self.previous_declaration is not None) and len(self.pile) == 0:
            print("[ERROR] Inconsistency")
            return False
        if (self.previous_declaration is not None) and (self.declared_card[0] < self.previous_declaration[0]):
            print(len(self.pile))
            print(self.previous_declaration)
            print(self.declared_card)
            print(self.pile[-1])
            print("[ERROR] Improper move!")
            return False
        return True

    def debugGeneral(self):
        A = set(self.players[0].cards)
        B = set(self.players[1].cards)
        C = set(self.player_cards[0])
        D = set(self.player_cards[1])
        P = set(self.pile)
        E = set(self.game_deck)

        if not A == C:
            print("Error 001")
            return False
        if not B == D:
            print("Error 002")
            return False
        if not A | B | P == E:
            print("Error 003")
            print(A)
            print(B)
            print(P)
            print(E)
            return False
        return True