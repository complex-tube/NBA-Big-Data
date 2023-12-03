from abc import ABC, abstractmethod
from typing import List

import pandas


class ISaveGamesRepo(ABC):

    @abstractmethod
    def save_games(self, games: List[pandas.DataFrame], season: int):
        pass
