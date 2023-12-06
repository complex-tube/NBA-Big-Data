from typing import List

import pandas

from usecases.interfaces.get_games_from_repo_interface import IGetGamesFromRepo
from usecases.interfaces.save_games_repo_interface import ISaveGamesRepo
from adapters.interfaces.get_games_from_framework_interface import IGetGamesFromFramework
from adapters.interfaces.save_games_framework_interaface import ISaveGamesFramework


class GamesRepo(IGetGamesFromRepo, ISaveGamesRepo):

    get_games_from_framework: IGetGamesFromFramework
    save_games_framework: ISaveGamesFramework

    def __init__(self, get_games_from_framework: IGetGamesFromFramework, save_games_framework: ISaveGamesFramework):
        self.get_games_from_framework = get_games_from_framework
        self.save_games_framework = save_games_framework

    def get_games(self, season: int) -> List[pandas.DataFrame]:
        try:
            return self.get_games_from_framework.get_games(season)
        except:
            print('Не удалось получить доступ к API')
            return []

    def save_games(self, games: List[pandas.DataFrame], season: int):
        self.save_games_framework.save_games(games, season)

