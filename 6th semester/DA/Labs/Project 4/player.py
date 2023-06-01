class Player():
    def __init__(self, name):
        
        self.name = name
        self.cards = None
    
    ### -------------------------------------------------------------
    
    ### TO BE IMPLEMENTED - player's strategy 
    ### input: declared card, i.e., the card which is supposed
    ### to be the top card of the pile: If None - you can put any card you want because
    ### (a) it is the first turn (pile is empty) or (b) some cards were drawn in the previous turn)
    ### output: - player's true decision, player's declaration (if not equal - (s)he cheats)
    
    def putCard(self, declared_card):
        ### DO NOT REMOVE TRUE CARD cards.remove!!!
        ### return an object (not id): self.cards[id], not id
        ### for instance: return self.cards[0], self.cards[0] 
        ### IMPORTANT: If you want to draw cards instead of put, return "draw"
        ### for instance: return "draw" 
        return self.cards[0], self.cards[0] 
    
    ### TO BE IMPLEMENTED - Decide whether to check or not opponent's move (return True or False)
    def checkCard(self, opponent_declaration):
        pass
    
    ### Notification sent at the end of a round
    ### One may implement this method, capture data, and use it to get extra info
    ### -- checked = TRUE -> someone checked. If FALSE, the remaining inputs do not play any role
    ### -- iChecked = TRUE -> I decided to check my opponent (so it was my turn); 
    ###               FALSE -> my opponent checked and it was his turn
    ### -- iDrewCards = TRUE -> I drew cards (so I checked but was wrong or my opponent checked and was right); 
    ###                 FALSE -> otherwise
    ### -- revealedCard - some card (X, Y). Only if I checked.
    ### -- noTakenCards - number of taken cards
    def getCheckFeedback(self, checked, iChecked, iDrewCards, revealedCard, noTakenCards, log=True):
        if log: print("Feedback = " + self.name + " : checked this turn = " + str(checked) +
              "; I checked = " + str(iChecked) + "; I drew cards = " + 
                      str(iDrewCards) + "; revealed card = " + 
                      str(revealedCard) + "; number of taken cards = " + str(noTakenCards))
    
    
    ### -------------------------------------------------------------
    
    ### Init player's hand
    def startGame(self, cards):
        self.cards = cards
    
    ### Add some cards to player's hand (if (s)he checked opponent's move, but (s)he was wrong)
    def takeCards(self, cards_to_take):
        self.cards = self.cards + cards_to_take