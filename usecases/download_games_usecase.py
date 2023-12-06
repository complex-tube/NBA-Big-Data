from usecases.interfaces.get_games_from_repo_interface import IGetGamesFromRepo
from usecases.interfaces.save_games_repo_interface import ISaveGamesRepo


class DownloadGamesUseCase:
    get_games_from_repo: IGetGamesFromRepo
    save_games_repo: ISaveGamesRepo

    def __init__(self, get_games_from_repo: IGetGamesFromRepo, save_games_repo: ISaveGamesRepo):
        self.get_games_from_repo = get_games_from_repo
        self.save_games_repo = save_games_repo

    def invoke(self, start_year: int, end_year: int):
        seasons = range(start_year, end_year + 1)

        for season in seasons:
            self.save_games_repo.save_games(self.get_games_from_repo.get_games(season), season)
