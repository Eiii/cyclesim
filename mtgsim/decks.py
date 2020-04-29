from .card import Card

cycle_deck = (
    (Card.Land(), 20),
    (Card.Card(), 8),
    (Card.Cycle(1), 28),
    (Card.Cycle(2), 4)
)

low_lands = (
    (Card.Land(), 16),
    (Card.Card(), 8),
    (Card.Cycle(1), 32),
    (Card.Cycle(2), 4)
)
