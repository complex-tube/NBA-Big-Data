from usecases.interfaces.get_stats_from_repo_interface import IGetStatsFromRepo
from usecases.interfaces.save_stats_repo_interface import ISaveStatsRepo


class DownloadStatsUseCase:
    get_stats_from_repo: IGetStatsFromRepo
    save_stats_repo: ISaveStatsRepo

    def __init__(self, get_stats_from_repo: IGetStatsFromRepo, save_stats_repo: ISaveStatsRepo):
        self.get_stats_from_repo = get_stats_from_repo
        self.save_stats_repo = save_stats_repo

    def invoke(self, start_year: int, end_year: int):
        seasons = range(start_year, end_year + 1)

        for season in seasons:
            self.save_stats_repo.save_stats(self.get_stats_from_repo.get_stats(season), season)
