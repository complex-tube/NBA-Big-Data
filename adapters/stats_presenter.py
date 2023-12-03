from usecases.download_stats_usecase import DownloadStatsUseCase

from adapters.stats_repo import StatsRepo

class StatsPresenter:
    def __init__(self):
        pass

    def download_stats(self, stats_repo: StatsRepo):
        download_stats_usecase = DownloadStatsUseCase(stats_repo, stats_repo)
        download_stats_usecase.invoke()

