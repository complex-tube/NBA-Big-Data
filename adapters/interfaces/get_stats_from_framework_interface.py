from abc import ABC, abstractmethod
from typing import List

import pandas


class IGetStatsFromFramework(ABC):
    @abstractmethod
    def get_stats(self, season: int) -> List[pandas.DataFrame]:
        pass
