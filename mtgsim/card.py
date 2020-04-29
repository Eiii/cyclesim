from enum import Enum
from functools import partial

class CardType(Enum):
    Land = 'Land'
    Card = 'Card'
    Cycle = 'Cycle'

class Card:
    def __init__(self, type_, cyc_cost=None):
        self.type = type_
        if cyc_cost:
            self.cycle_cost = cyc_cost

    def __repr__(self):
        return f'<Card str(self)>'

    def __str__(self):
        if self.type == CardType.Land:
            return 'L'
        elif self.type == CardType.Card:
            return 'X'
        elif self.type == CardType.Cycle:
            return 'c' if self.cycle_cost == 1 else 'C'

    def is_land(self):
        return self.type == CardType.Land

    def is_cycle(self, max_cost):
        return self.type == CardType.Cycle and \
            self.cycle_cost <= max_cost

    @classmethod
    def Land(cls):
        c = cls(CardType.Land)
        return c

    @classmethod
    def Card(cls):
        c = cls(CardType.Card)
        return c

    @classmethod
    def Cycle(cls, cycle_cost):
        c = cls(CardType.Cycle, cycle_cost)
        return c
