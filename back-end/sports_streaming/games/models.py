from sports_streaming import util


class Game(util.printing.DataModel):
  def __init__(self, team1, team2, score, time, link):
    self.team1 = team1
    self.team2 = team2
    self.score = score
    self.time = time
    self.link = link


class BaseballGame(Game):
  def __init__(self, team1, team2, score, time, link):
    super().__init__(team1, team2, score, time, link)
    self.id = link.split('/')[-1]
