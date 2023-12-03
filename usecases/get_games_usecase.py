from typing import List

import pandas

from usecases.interfaces.get_games_from_repo_interface import IGetGamesFromRepo


class GetGamesUseCase:
    get_games_from_repo: IGetGamesFromRepo

    def __init__(self, get_games_from_repo: IGetGamesFromRepo):
        self.get_games_from_repo = get_games_from_repo

    def invoke(self, season: int) -> List[pandas.DataFrame]:
        return self.get_games_from_repo.get_games(season)
