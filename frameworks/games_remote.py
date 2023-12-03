import time
from typing import List

import pandas as pd
import requests

from adapters.interfaces.get_games_from_framework_interface import IGetGamesFromFramework


class GamesRemote(IGetGamesFromFramework):
    def __init__(self):
        pass

    def get_games(self, season: int) -> List[pd.DataFrame]:
        games_list: List[pd.DataFrame] = []
        url = "https://www.balldontlie.io/api/v1/games?per_page=100&"

        response = requests.get(url + 'seasons[]=' + str(season) + '&page=' + str(1))
        while response.status_code == 429:
            response = requests.get(url + 'seasons[]=' + str(season) + '&page=' + str(1))
            time.sleep(1)
        print(url + 'seasons[]=' + str(season) + '&page=' + str(1))

        if response.status_code != 429:
            total_pages = response.json()['meta']['total_pages']
            if total_pages != 0:
                for i in range(1, total_pages + 1):
                    response = requests.get(url + 'seasons[]=' + str(season) + '&page=' + str(i))
                    print(url + 'seasons[]=' + str(season) + '&page=' + str(i))
                    while response.status_code == 429:
                        response = requests.get(url + 'seasons[]=' + str(season) + '&page=' + str(i))
                        time.sleep(1)

                    games = pd.DataFrame({
                        "game_id": [],
                        "date": [],
                        "home_team_abbreviation": [],
                        "home_team_city": [],
                        "home_team_conference": [],
                        "home_team_division": [],
                        "home_team_full_name": [],
                        "home_team_name": [],
                        "home_team_score": [],
                        "period": [],
                        "postseason": [],
                        "season": [],
                        "status": [],
                        "time": [],
                        "visitor_team_abbreviation": [],
                        "visitor_team_city": [],
                        "visitor_team_conference": [],
                        "visitor_team_division": [],
                        "visitor_team_full_name": [],
                        "visitor_team_name": [],
                        "visitor_team_score": []
                    })
                    return_value = response.json()['data']
                    for game in return_value:
                        games.loc[len(games)] = {
                            "game_id": game['id'],
                            "date": game['date'],
                            "home_team_abbreviation": game['home_team']['abbreviation'],
                            "home_team_city": game['home_team']['city'],
                            "home_team_conference": game['home_team']['conference'],
                            "home_team_division": game['home_team']['division'],
                            "home_team_full_name": game['home_team']['full_name'],
                            "home_team_name": game['home_team']['name'],
                            "home_team_score": game['home_team_score'],
                            "period": game['period'],
                            "postseason": game['postseason'],
                            "season": game['season'],
                            "status": game['status'],
                            "time": game['time'],
                            "visitor_team_abbreviation": game['visitor_team']['abbreviation'],
                            "visitor_team_city": game['visitor_team']['city'],
                            "visitor_team_conference": game['visitor_team']['conference'],
                            "visitor_team_division": game['visitor_team']['division'],
                            "visitor_team_full_name": game['visitor_team']['full_name'],
                            "visitor_team_name": game['visitor_team']['name'],
                            "visitor_team_score": game['visitor_team_score']
                        }
                    games_list.append(games)
        return games_list
