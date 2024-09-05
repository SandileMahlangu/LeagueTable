import unittest

from leagueTable import LeagueTable

class TestLeagueTable(unittest.TestCase):

    def setUp(self):
        """Set up the league table for testing."""
        self.league = LeagueTable()


    def test_single_match(self):
        """Test recording a single match."""
        
        self.league.record_match("Lions", 3, "Snakes", 3)
        ranked_teams = self.league.rank_teams()

        self.assertEqual(ranked_teams[0].name, "Lions")
        self.assertEqual(ranked_teams[0].points, 1)
        self.assertEqual(ranked_teams[1].name, "Snakes")
        self.assertEqual(ranked_teams[1].points, 1)

    def test_multiple_matches(self):
        """Test recording multiple matches and correct ranking."""
       
        self.league.record_match("Lions", 3, "Snakes", 3)
        self.league.record_match("Tarantulas", 1, "FC Awesome", 0)
        self.league.record_match("Lions", 1, "FC Awesome", 1)
        self.league.record_match("Tarantulas", 3, "Snakes", 1)
        self.league.record_match("Lions", 4, "Grouches", 0)
        
        ranked_teams = self.league.rank_teams()

        # Check rankings and points
        self.assertEqual(ranked_teams[0].name, "Tarantulas")
        self.assertEqual(ranked_teams[0].points, 6)
        self.assertEqual(ranked_teams[1].name, "Lions")
        self.assertEqual(ranked_teams[1].points, 5)
        self.assertEqual(ranked_teams[2].name, "FC Awesome")
        self.assertEqual(ranked_teams[2].points, 1)
        self.assertEqual(ranked_teams[3].name, "Snakes")
        self.assertEqual(ranked_teams[3].points, 1)
        self.assertEqual(ranked_teams[4].name, "Grouches")
        self.assertEqual(ranked_teams[4].points, 0)
       

    def test_tie_break_on_name(self):
        """Test that teams with the same points are sorted by name."""
       

        self.league.record_match("Lions", 3, "Snakes", 3)
        self.league.record_match("Lions", 1, "FC Awesome", 1)
        
        
        ranked_teams = self.league.rank_teams()

        # Check that teams with the same points are sorted alphabetically
        
        self.assertEqual(ranked_teams[0].name, "Lions")
        self.assertEqual(ranked_teams[1].name, "FC Awesome")
        self.assertEqual(ranked_teams[2].name, "Snakes")

    def test_draw_match(self):
        """Test recording a match that ends in a draw."""
        
        self.league.record_match("Lions", 3, "Snakes", 3)
        ranked_teams = self.league.rank_teams()

        self.assertEqual(ranked_teams[0].points, 1)
        self.assertEqual(ranked_teams[1].points, 1)
        self.assertEqual(ranked_teams[0].name, "Lions")
        self.assertEqual(ranked_teams[1].name, "Snakes")

    def test_no_matches(self):
        """Test the league table with no matches."""
        ranked_teams = self.league.rank_teams()
        self.assertEqual(len(ranked_teams), 0)

if __name__ == "__main__":
    unittest.main()

