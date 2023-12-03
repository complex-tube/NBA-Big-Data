import pandas

from adapters.stats_presenter import StatsPresenter
from adapters.games_presenter import GamesPresenter
from adapters.games_repo import GamesRepo
from adapters.stats_repo import StatsRepo

from frameworks.elk import ELK
from frameworks.games_remote import GamesRemote
from frameworks.games_csv import GamesCSV
from frameworks.stats_remote import StatsRemote
from frameworks.stats_csv import StatsCsv


class UI:

    elk: ELK

    def __init__(self):
        self.elk = ELK()
        pass

    def chosen(self):
        pass

    def launch_logstash_clicked(self):
        self.elk.delete_indices()
        self.elk.clear_null_file()
        self.elk.launch_logstash()

    def launch_elk_clicked(self):
        self.elk.launch_elasticsearch()
        self.elk.launch_kibana()

    def connect_to_elastic(self):
        self.elk.connect_to_elastic()

    def download_games_option_chosen(self):
        games_presenter = GamesPresenter()
        games_remote = GamesRemote()
        games_csv = GamesCSV()
        games_repo: GamesRepo = GamesRepo(games_remote, games_csv)
        games_presenter.download_games(games_repo)

    def download_stats_option_chosen(self):
        stat_presenter = StatsPresenter()
        stats_remote = StatsRemote()
        stats_csv = StatsCsv()
        stats_repo = StatsRepo(stats_remote, stats_csv)
        stat_presenter.download_stats(stats_repo)

    def exit(self):
        print('Закройте все окна командой строки: elasticserach, kibana и logstash')
