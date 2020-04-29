from . import decks
from . import plot
from .game import Game
from .behaviors import mull_no_lands, play_land, cycle_all

import multiprocessing
import argparse
from collections import namedtuple, defaultdict
from functools import partial
from pathlib import Path


Turn = namedtuple('Turn', ['lands', 'hand'])
def episode(deck, mull_strat, behaviors):
    results = []
    num_turns = 5
    hand_size = 7
    game = Game(deck, hand_size)
    while mull_strat(game, hand_size) and hand_size > 0:
        hand_size -= 1
        game = Game(deck, hand_size)
    for _ in range(num_turns):
        game.reset_turn()
        for b in behaviors:
            b(game)
        results.append(Turn(game.num_lands, game.hand.cards_str()))
        game.draw()
    return results

def analyze(results):
    d = defaultdict(int)
    for r in results:
        for t, turn in enumerate(r):
            e = (t+1, turn.lands)
            d[e] += 1
    return defaultdict(int, {k:v/len(results) for k,v in d.items()})

###

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--episodes', type=float, default=1e4)
    parser.add_argument('--output', type=Path, default='out.png')
    return parser

def main():
    cmd_args = make_parser().parse_args()
    num_episodes = int(cmd_args.episodes)
    args = (decks.low_lands,
            mull_no_lands,
            [play_land, cycle_all])
    results = multiprocessing.Pool().starmap(episode,
                                             [args]*num_episodes,
                                             chunksize=100)
    anal = analyze(results)
    plot.land_turns_dist(anal, cmd_args.output)

if __name__=='__main__':
    main()
