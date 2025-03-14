from player_reader import PlayerReader
from enum import Enum
class SortBy (Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, readeri):
        self.reader = readeri

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, mode = SortBy.POINTS):
        def sort_by_points(player):
            return player.points
        def sort_by_assists(player):
            return player.assists
        def sort_by_goals(player):
            return player.goals
        match mode:
            case SortBy.POINTS:
                k = sort_by_points
            case SortBy.ASSISTS:
                k = sort_by_assists
            case SortBy.GOALS:
                k = sort_by_goals
                
        sorted_players = sorted(
        self._players,
        reverse=True,
        key = k)

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result