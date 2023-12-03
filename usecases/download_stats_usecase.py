from usecases.interfaces.get_stats_from_repo_interface import IGetStatsFromRepo
from usecases.interfaces.save_stats_repo_interface import ISaveStatsRepo


class DownloadStatsUseCase:
    get_stats_from_repo: IGetStatsFromRepo
    save_stats_repo: ISaveStatsRepo

    def __init__(self, get_stats_from_repo: IGetStatsFromRepo, save_stats_repo: ISaveStatsRepo):
        self.get_stats_from_repo = get_stats_from_repo
        self.save_stats_repo = save_stats_repo

    def invoke(self):
        seasons = range(1900, 2024)

        for season in seasons:
            self.save_stats_repo.save_stats(self.get_stats_from_repo.get_stats(season), season)
