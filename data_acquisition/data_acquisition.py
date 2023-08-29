import requests
from os.path import exists
import pandas as pd

from endpoints import *
from common.Common import headers
from common.Paths import STORAGE

def get_teams_df():
    team_dict = {}

    active_teams = requests.get(get_active_teams_endpoint(), headers=headers)
    if active_teams.status_code == 200:
        teams = active_teams.json()
        for team in teams:
            team_dict[team["Name"]] = {"Key": team["Key"], "ID": team["TeamID"]}

        teams_df = pd.DataFrame.from_dict(team_dict, orient='index')
        teams_df.reset_index().to_feather(f"{STORAGE}/base_teams_info.ftr")
    else:
        raise Exception(f"Failed to retrieve team data. Status code: {active_teams.status_code}")

    print(f'Teams\n{teams_df.to_string()}')

    return teams_df

def get_teams_list():
    if not exists(f"{STORAGE}/base_teams_info.ftr"):
        teams_df = get_teams_df()
        teams_list = teams_df["Key"].values
        return teams_list
    else:
        teams_df = pd.read_feather(f"{STORAGE}/base_teams_info.ftr")
        teams_list = teams_df["Key"].values
        return teams_list

def get_players_df(existing=True):
    teams = get_teams_list()
    players = {}
    player_file = f"{STORAGE}/base_players_info.ftr"

    if existing:
        # User wants to grab the player dataframe that already exists.
        if exists(player_file):
            players_df = pd.read_feather(player_file)
            print(f'Players: {players_df.to_string()}\n')
            return players_df
        else:
            print("No file containing basic player data exists. Pulling from web...")
            pass

    for team in teams:
        active_players = requests.get(get_players_by_team_endpoint(team), headers=headers)
        if active_players.status_code == 200:
            team_players = active_players.json()
            # print(f'Team players: {team_players}')
            for player in team_players:
                player_info = get_player_info_from_api_obj(player, team)
                players[player["PlayerID"]] = player_info

        else:
            raise Exception(f"Failed to retrieve player data. Status code: {active_players.status_code}")

    players_df = pd.DataFrame.from_dict(players, orient='index')
    players_df.reset_index().to_feather(player_file)

    print(f'Players: {players_df.to_string()}\n')

    return players_df

def get_player_info_from_api_obj(player: dict, team: str):
    # Other potentially informational fields: College, Experience,
    player_info = {"Team": team,
                   "Name": f"{player['ShortName']}",
                   "Type": player['PositionCategory'],
                   "Position": player['Position'],
                   "Status": player['Status'],
                   "Height": player["Height"],
                   "Weight": player["Weight"],
                   "Age": player["Age"],
                   "Active": player["Active"],
                   "TeamID": player["TeamID"]}
    return player_info

get_players_df(True)
