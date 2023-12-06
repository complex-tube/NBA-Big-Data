from usecases.download_stats_usecase import DownloadStatsUseCase

from adapters.stats_repo import StatsRepo

class StatsPresenter:
    def __init__(self):
        pass

    def download_stats(self, stats_repo: StatsRepo, start_year: int, end_year: int):
        download_stats_usecase = DownloadStatsUseCase(stats_repo, stats_repo)
        download_stats_usecase.invoke(start_year, end_year)

