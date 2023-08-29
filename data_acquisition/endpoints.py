from common.Common import API_KEY

# FantasyData Endpoints:

def get_players_by_team_endpoint(team: str):
    """
    Returns the required endpoint for retrieving player data by team.

    Parameters
    team (str): Team abbreviation (e.g. WAS, for Washington Commanders)

    """
    players_by_team_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/PlayersBasic/{team}?key={API_KEY}"
    return players_by_team_endpoint

def get_bye_weeks_by_season(season: str):
    """
    Returns the required endpoint for retrieving team bye weeks for any specified season.

    Parameters
    season (str): Season descriptor (e.g. 2015REG, 2015PRE, 2015POST)

    """
    bye_weeks_by_season_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Byes/{season}?key={API_KEY}"
    return bye_weeks_by_season_endpoint

def get_player_details_by_player_endpoint(player_id: int):
    """
    Returns the required endpoint for retrieving player details by player id.

    Parameters
    player_id (int): Integer representing a given player (e.g. 732)

    """
    player_details_by_player_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Player/{player_id}?key={API_KEY}"
    return player_details_by_player_endpoint

def get_player_details_by_team_endpoint(team: str):
    """
    Returns the required endpoint for retrieving player details by team abbreviation.

    Parameters
    team (str): Team abbreviation (e.g. WAS, for Washington Commanders)

    """
    player_details_by_team_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Players/{team}?key={API_KEY}"
    return player_details_by_team_endpoint

def get_game_bye_weeks_by_season_endpoint(season: str):
    """
    Returns the required endpoint for retrieving team bye weeks for any specified season.

    Parameters
    season (str): Season descriptor (e.g. 2015REG, 2015PRE, 2015POST)

    """
    game_bye_weeks_by_season_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Byes/{season}?key={API_KEY}"
    return game_bye_weeks_by_season_endpoint

def get_game_schedule_by_season_endpoint(season: str):
    """
    Returns the required endpoint for retrieving schedules for any specified season.

    Parameters
    season (str): Season descriptor (e.g. 2015REG, 2015PRE, 2015POST)

    """
    game_schedule_by_season_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Schedules/{season}?key={API_KEY}"
    return game_schedule_by_season_endpoint

def get_game_scores_by_season_endpoint(season: str):
    """
    Returns the required endpoint for retrieving game scores for a specified week of a season.

    Parameters
    season (str): Season descriptor (e.g. 2015REG, 2015PRE, 2015POST)

    """
    game_scores_by_season_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Scores/{season}?key={API_KEY}"
    return game_scores_by_season_endpoint

def get_game_scores_by_season_week_endpoint(date: str):
    """
    Returns the required endpoint for retrieving game scores for a specified week of a season.

    Parameters
    date (str): Date descriptor (e.g. 2021-SEP-12, 2021-NOV-28)

    """
    game_scores_by_season_week_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/ScoresByDate/{date}?key={API_KEY}"
    return game_scores_by_season_week_endpoint

def get_stadiums_endpoint():
    """
    Returns the required endpoint for retrieving all stadiums.

    """
    stadiums_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Stadiums?key={API_KEY}"
    return stadiums_endpoint

def get_active_teams_endpoint():
    """
    Returns the required endpoint for retrieving all stadiums.

    """
    active_teams_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/Teams?key={API_KEY}"
    return active_teams_endpoint

def get_team_game_logs_by_season_endpoint(season: str, team_id: int, numberofgames: int):
    """
    Returns the required endpoint for retrieving game log of total team statistics.

    Parameters
    season (str): Season descriptor (e.g. 2019POST, 2020)
    team_id (int): Unique ID of team (e.g. 8)
    numberofgames (int): How many games to return (e.g. all, 10, 25)

    """
    team_game_logs_by_season_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStatsBySeason/{season}/" \
        f"{team_id}/{numberofgames}?key={API_KEY}"
    return team_game_logs_by_season_endpoint

def get_team_season_stats_endpoint(season: str):
    """
    Returns the required endpoint for retrieving game log of total team statistics.

    Parameters
    season (str): Season descriptor (e.g. 2019POST, 2020)

    """
    team_season_stats_endpoint = \
        f"https://api.sportsdata.io/v3/nfl/scores/json/TeamSeasonStats/{season}?key={API_KEY}"
    return team_season_stats_endpoint

