import typing
import random

from utils.card import Card




class Game(object):
    
    def __init__(self):
        self.card_list = self.create_all_cards()
    


    ### this helps mix the right color for the right symbol returns list of strings
    
    def choose_symbols_color(self):
        """
        [It creates a list of all possible combinaison of symbols with the right colors !!!]

        Returns:
            [list]: [mix of symbols and possible colors]
        """ 

        list_of_symbols = []
        for color, symbols in Card.card_sets.items():
            for symbol in symbols:
                list_of_symbols.append(f'{color} {symbol}')
        return list_of_symbols


    ### This helpers will creates all cards pack
    def create_all_cards(self):
        """[It creates all the card that we need for the game each card being a string combination of color, symbol and value]

        Returns:
            [list]: [returns list of all cards generated]
        """
        all_cards = []

        for value in Card.values:
            for symbols in self.choose_symbols_color():
                all_cards.append(f'{value} {symbols}')
        return all_cards

    ### 
    
    def suffle_card_game(self, cards_list):
        """[Shuffles the card_list]

        Args:
            cards_list ([list]): [returns the same list of card suffled]
        """
        random.shuffle(cards_list)

