import random

"""

        PLAYERS - CLASS

"""



class Player(object):
    '''
        Creates a instance Player containing:
        A name nammed name
        A list of Card (each player start with 10 Card) nammed cards
        A play() method that throw a Card in the Board
        A shuffle() method that shuffle all the Card of the player.
    '''

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    
    def play(self):
        """[an Helper use to delete a card]

        Returns:
            [Card]: [card deleted from the player cards after (played) put on the board by the player]
        """      
        return self.cards.pop()

    def shuffle(self):
        """[shuffles all card of the player]
        """        
        random.suffle(self.cards)

    