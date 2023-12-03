import os
from typing import List

import pandas

from adapters.interfaces.save_stats_framework_interface import ISaveStatsFramework


class StatsCsv(ISaveStatsFramework):
    def __init__(self):
        pass

    def save_stats(self, stats: List[pandas.DataFrame], season: int):
        if not os.path.isdir('./data'):
            os.makedirs('./data')
            os.makedirs('./data/stats')
        for stat_index in range(0, len(stats)):
            stats[stat_index].to_csv('./data/stats/stats-' + str(season) + '-' + str(stat_index + 1) + '.csv')
