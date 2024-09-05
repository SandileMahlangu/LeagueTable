class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.draws = 0     
        self.goals_for = 0
        self.goals_against = 0

    def update_stats(self, goals_for, goals_against):
        self.goals_for += goals_for
        self.goals_against += goals_against
        
        if goals_for > goals_against:
            self.wins += 1
            self.points += 3
        elif goals_for == goals_against:
            self.draws += 1
            self.points += 1
      


class LeagueTable:
    def __init__(self):
        self.teams = {}

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)

    def record_match(self, team1_name, team1_goals, team2_name, team2_goals):
        self.add_team(team1_name)
        self.add_team(team2_name)
        
        team1 = self.teams[team1_name]
        team2 = self.teams[team2_name]
        
        team1.update_stats(team1_goals, team2_goals)
        team2.update_stats(team2_goals, team1_goals)

    def rank_teams(self):
        
        # Sort by points in descending order, and by name in ascending order if the team has equal points
        ranked_teams = sorted(self.teams.values(), key=lambda x: (-x.points, x.name))
        return ranked_teams

#display log table
def display_table(league_table):
  
    n=0

    print("\n")
    
    ranked_teams = league_table.rank_teams()
    current_rank = 1  # Start the rank count at initial 1

    #for n, team in enumerate(league_table.rank_teams(), start=1):
    for n, team in enumerate(ranked_teams):
        pt = "pt" if team.points == 1 else "pts"
        
        # If this is not the first team and the points are the same as the previous team, reuse the rank
        if n > 0 and team.points == ranked_teams[n - 1].points:
            # Same rank as previous team
            rank_to_display = current_rank  
        else:
            # New rank for a different point value
            rank_to_display = n + 1 
            # Update the current rank 
            current_rank = rank_to_display  

        print(f"{rank_to_display:<2}{team.name:<20}{team.points} {pt}")
       
if __name__ == "__main__":
    league = LeagueTable()

    while True:
        print("\nEnter match results (one per line)")       
        print("Once Finished, Type 'done' on the next line to calculate:")
        
        # collect matches in lines
        match_inputs = []
        while True:
            match_input = input()
            if match_input.lower() == 'done':
                break
            match_inputs.append(match_input)

        for match_input in match_inputs:
            try:
                # Split the input based on the comma first
                team1Data, team2Data = match_input.split(',')
                
                # Split each part by spaces
                team1_name, team1_goals = team1Data.rsplit(' ', 1)
                team2_name, team2_goals = team2Data.strip().rsplit(' ', 1)
                
                # Convert the goals to integers
                team1_goals = int(team1_goals)
                team2_goals = int(team2_goals)
                
                # Record the match result in the league table
                league.record_match(team1_name, team1_goals, team2_name, team2_goals)
            except ValueError:
                print(f"Invalid input: '{match_input}'. Please enter the match result in the correct format.")
   
        # Display the current league table after entering all results
        display_table(league)
        
        # Ask if the user wants to enter more results
        more_results = input("Do you want to enter more results? (Y/N): ")
        if more_results.lower() == 'n':
            break
