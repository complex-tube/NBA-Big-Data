from usecases.download_games_usecase import DownloadGamesUseCase
from adapters.games_repo import GamesRepo

class GamesPresenter:
    def __init__(self):
        pass

    def download_games(self, games_repo: GamesRepo, start_year: int, end_year: int):
        download_games_usecase = DownloadGamesUseCase(games_repo, games_repo)
        download_games_usecase.invoke(start_year, end_year)
