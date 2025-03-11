import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), # 16
            Player("Lemieux", "PIT", 45, 54), #99
            Player("Kurri", "EDM", 37, 53), #90
            Player("Yzerman", "DET", 42, 56), #98
            Player("Gretzky", "EDM", 35, 89) #124
        ]
class Test_nhl(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    def test_correct_players(self):
        self.assertAlmostEqual(self.stats._players[0].name, "Semenko")
        self.assertAlmostEqual(self.stats._players[1].name, "Lemieux")
        self.assertAlmostEqual(self.stats._players[2].name, "Kurri")
        self.assertAlmostEqual(self.stats._players[3].name, "Yzerman")
        self.assertAlmostEqual(self.stats._players[4].name, "Gretzky")
    def test_search(self):
        self.assertAlmostEqual(self.stats.search("Semenko").name, Player("Semenko", "EDM", 4, 12).name)
    def test_wrongsearch(self):
        self.assertAlmostEqual(self.stats.search("Avacyn"), None)
    def test_team(self):
        self.assertAlmostEqual(self.stats.team("PIT")[0].name, "Lemieux")
    def test_top3_best_performers(self):
        playerlist = self.stats.top(2)
        self.assertAlmostEqual(playerlist[0].name, "Gretzky")
        self.assertAlmostEqual(playerlist[1].name, "Lemieux")
        self.assertAlmostEqual(playerlist[2].name, "Yzerman")
    def test_top3_best_goals(self):
        playerlist2 = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(playerlist2[0].name, "Lemieux")
        self.assertEqual(playerlist2[1].name, "Yzerman")
        self.assertEqual(playerlist2[2].name, "Kurri")
    def test_top3_best_assists(self):
        playerlist3 = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(playerlist3[0].name, "Gretzky")
        self.assertEqual(playerlist3[1].name, "Yzerman")
        self.assertEqual(playerlist3[2].name, "Lemieux")