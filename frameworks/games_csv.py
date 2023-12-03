import os.path
from typing import List

import pandas

from adapters.interfaces.save_games_framework_interaface import ISaveGamesFramework


class GamesCSV(ISaveGamesFramework):

    def __init__(self):
        pass

    def save_games(self, games: List[pandas.DataFrame], season: int):
        if not os.path.isdir('./data'):
            os.makedirs('./data')
            os.makedirs('./data/games')
        for game_index in range(0, len(games)):
            games[game_index].to_csv('./data/games/game-' + str(season) + '-' + str(game_index + 1) + '.csv')
