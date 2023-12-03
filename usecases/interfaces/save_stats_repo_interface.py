from abc import ABC, abstractmethod
from typing import List

import pandas


class ISaveStatsRepo(ABC):

    @abstractmethod
    def save_stats(self, stats: List[pandas.DataFrame], season: int):
        pass