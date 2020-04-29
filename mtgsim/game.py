from . import pile

class Game:
    def __init__(self, deck_spec, num_cards=7):
        self.init_piles(deck_spec)
        self.init_hand(num_cards)
        self.init_state()

    def reset_turn(self):
        self.used_mana = 0

    def init_piles(self, spec):
        self.graveyard = pile.Graveyard()
        self.library = pile.Library()
        self.fill_library(spec)
        self.library.shuffle()

    def fill_library(self, spec):
        for card, count in spec:
            for _ in range(count):
                self.library.add_card(card)

    def init_hand(self, count):
        self.hand = pile.Hand()
        for _ in range(count):
            self.hand.add_card(self.library.draw())

    def init_state(self):
        self.num_lands = 0

    def draw(self):
        self.hand.add_card(self.library.draw())

    def play_land(self, card):
        assert card.is_land()
        self.hand.remove(card)
        self.num_lands += 1

    def avail_lands(self):
        return self.num_lands - self.used_mana

    def cycle(self, card):
        assert card.cycle_cost <= self.avail_lands()
        self.used_mana += card.cycle_cost
        self.hand.remove(card)
        self.graveyard.add_card(card)
        self.draw()
