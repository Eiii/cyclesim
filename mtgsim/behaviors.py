def mull_to(count, game, hand_size):
    return hand_size != count

def mull_no_lands(game, hand_size):
    return game.hand.get_land() is None

def play_land(game):
    if (land_card := game.hand.get_land()):
        game.play_land(land_card)

def cycle_all(game):
    while (cycle_card := game.hand.get_cycle(game.avail_lands())):
        game.cycle(cycle_card)
