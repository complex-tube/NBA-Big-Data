import time
from typing import List

import pandas as pd
import requests

from adapters.interfaces.get_stats_from_framework_interface import IGetStatsFromFramework


class StatsRemote(IGetStatsFromFramework):
    def __init__(self):
        pass

    def get_stats(self, season: int) -> List[pd.DataFrame]:
        stats_list: List[pd.DataFrame] = []
        url = "https://www.balldontlie.io/api/v1/stats?per_page=100&"

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

                    stat_df = pd.DataFrame({
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
                    for stat in return_value:
                        stat_df.loc[len(stat)] = {
                            "stat_id": stat['id'] if stat['id'] != None else 0,
                            "ast": stat['ast'] if stat['ast'] != None else 0,
                            "blk": stat['blk'] if stat['blk'] != None else 0,
                            "dreb": stat['dreb'] if stat['dreb'] != None else 0,
                            "fg3_pct": stat['fg3_pct'] if stat['fg3_pct'] != None else 0,
                            "fg3a": stat['fg3a'] if stat['fg3a'] != None else 0,
                            "fg_pct": stat['fg_pct'] if stat['fg_pct'] != None else 0,
                            "fga": stat['fga'] if stat['fga'] != None else 0,
                            "fgm": stat['fgm'] if stat['fgm'] != None else 0,
                            "ft_pct": stat['ft_pct'] if stat['ft_pct'] != None else 0,
                            "fta": stat['fta'] if stat['fta'] != None else 0,
                            "ftm": stat['ftm'] if stat['ftm'] != None else 0,
                            "game_id": stat['game']['id'] if stat['game'] != None and stat['game']['id'] != None else 0,
                            "game_date": stat['game']['date'] if stat['game'] != None and stat['game']['date'] != None else 0,
                            "game_home_team_id": stat['game']['home_team_id'] if stat['game'] != None and stat['game']['home_team_id'] != None else 0,
                            "game_home_team_score": stat['game']['home_team_score'] if stat['game'] != None and stat['game']['home_team_score'] != None else 0,
                            "game_period": stat['game']['period'] if stat['game'] != None and stat['game']['period'] != None else 0,
                            "game_postseason": stat['game']['postseason'] if stat['game'] != None and stat['game']['postseason'] != None else 0,
                            "game_season": stat['game']['season'] if stat['game'] != None and stat['game']['season'] != None else 0,
                            "game_status": stat['game']['status'] if stat['game'] != None and stat['game']['status'] != None else 0,
                            "game_time": stat['game']['time'] if stat['game'] != None and stat['game']['time'] != None else 0,
                            "game_visitor_team_id": stat['game']['visitor_team_id'] if stat['game'] != None and stat['game']['visitor_team_id'] != None else 0,
                            "game_visitor_team_score": stat['game']['visitor_team_score'] if stat['game'] != None and stat['game']['visitor_team_score'] != None else 0,
                            "min": stat['min'] if stat['min'] != None else 0,
                            "oreb": stat['oreb'] if stat['oreb'] != None else 0,
                            "pf": stat['pf'] if stat['pf'] != None else 0,
                            "player_id": stat['player']['id'] if stat['player'] != None and stat['player']['id'] != None else 0,
                            "player_first_name": stat['player']['first_name'] if stat['player'] != None and stat['player']['first_name'] != None else 0,
                            "player_height_feet": stat['player']['height_feet'] if stat['player'] != None and stat['player']['height_feet'] != None else 0,
                            "player_height_inches": stat['player']['height_inches'] if stat['player'] != None and stat['player']['height_inches'] != None else 0,
                            "player_last_name": stat['player']['last_name'] if stat['player'] != None and stat['player']['last_name'] != None else 0,
                            "player_position": stat['player']['position'] if stat['player'] != None and stat['player']['position'] != None else 0,
                            "player_team_id": stat['player']['team_id'] if stat['player'] != None and stat['player']['team_id'] != None else 0,
                            "player_weight_pounds": stat['player']['weight_pounds'] if stat['player'] != None and stat['player']['weight_pounds'] != None else 0,
                            "pts": stat['pts'] if stat['pts'] != None else 0,
                            "reb": stat['reb'] if stat['reb'] != None else 0,
                            "stl": stat['stl'] if stat['stl'] != None else 0,
                            "team_id": stat['team']['id'] if stat['team'] != None and stat['team']['id'] != None else 0,
                            "team_abbreviation": stat['team']['abbreviation'] if stat['team'] != None and stat['team']['abbreviation'] != None else 0,
                            "team_city": stat['team']['city'] if stat['team'] != None and stat['team']['city'] != None else 0,
                            "team_conference": stat['team']['conference'] if stat['team'] != None and stat['team']['conference'] != None else 0,
                            "team_division": stat['team']['division'] if stat['team'] != None and stat['team']['division'] != None else 0,
                            "team_full_name": stat['team']['full_name'] if stat['team'] != None and stat['team']['full_name'] != None else 0,
                            "team_name": stat['team']['name'] if stat['team'] != None and stat['team']['name'] != None else 0,
                            "turnover": stat['turnover'] if stat['team'] != None and stat['turnover'] != None else 0,
                        }
                    stats_list.append(stat_df)
        return stats_list