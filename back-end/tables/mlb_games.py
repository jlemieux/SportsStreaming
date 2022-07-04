import util


def create_table(games):
  header = ['#', 'Team 1', 'Team 2', 'Score', 'Time']
  rows = [
    [i, game.team1, game.team2, game.score, game.time]
    for i, game in enumerate(games, start=1)
  ]
  return util.tables.create_base_table(header, rows)
