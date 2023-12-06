from typing import List

import pandas

from usecases.interfaces.get_stats_from_repo_interface import IGetStatsFromRepo
from usecases.interfaces.save_stats_repo_interface import ISaveStatsRepo

from adapters.interfaces.get_stats_from_framework_interface import IGetStatsFromFramework
from adapters.interfaces.save_stats_framework_interface import ISaveStatsFramework


class StatsRepo(IGetStatsFromRepo, ISaveStatsRepo):
    get_stats_from_framework: IGetStatsFromFramework
    save_stats_framework: ISaveStatsFramework

    def __init__(self, get_stats_from_framework: IGetStatsFromFramework, save_stats_framework: ISaveStatsFramework):
        self.get_stats_from_framework = get_stats_from_framework
        self.save_stats_framework = save_stats_framework
        pass

    def get_stats(self, season: int) -> List[pandas.DataFrame]:
        try:
            return self.get_stats_from_framework.get_stats(season)
        except:
            print('Не удалось получить доступ к API')
            return []

    def save_stats(self, stats: List[pandas.DataFrame], season: int):
        self.save_stats_framework.save_stats(stats, season)
