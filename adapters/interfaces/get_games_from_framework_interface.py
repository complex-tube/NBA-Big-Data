from abc import ABC, abstractmethod
from typing import List

import pandas


class IGetGamesFromFramework(ABC):
    @abstractmethod
    def get_games(self, season: int) -> List[pandas.DataFrame]:
        pass
