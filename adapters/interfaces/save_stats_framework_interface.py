from abc import ABC, abstractmethod
from typing import List

import pandas


class ISaveStatsFramework(ABC):

    @abstractmethod
    def save_stats(self, stats: List[pandas.DataFrame], season: int):
        pass
