from . import card
from .card import CardType

import random


class _Pile:
    def __init__(self, cards=None):
        self.cards = list(cards) if cards is not None else []

    def add_card(self, card):
        self.cards.append(card)

    def add_card_bottom(self, card):
        self.cards.insert(0, card)

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def remove(self, card):
        if card:
            self.cards.remove(card)

    def cards_str(self):
        return ''.join(str(c) for c in self.cards)

    def __repr__(self):
        n = type(self).__name__
        return f'<{n} {self.to_str()}>'


class Library(_Pile):
    pass


class Graveyard(_Pile):
    pass


class Hand(_Pile):
    def get_land(self):
        for c in self.cards:
            if c.is_land(): return c

    def get_cycle(self, cost):
        for i in range(1, cost+1):
            for c in self.cards:
                if c.is_cycle(i): return c
