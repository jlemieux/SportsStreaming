from sports_streaming import util
from sports_streaming.games.models import BaseballGame


GAMES = 'https://redditmlbstreams.live/'


def get_games():
  soup = util.soup.get_soup(GAMES)

  # title = soup.select_one('#content div.header > h2.title')
  games = soup.select('#content div.body ul.competitions div.competition')
  games = [
    _parse_game(game)
    for game in games
  ]
  if not games:
    raise util.errors.NoGamesFound(sport='baseball')
  return games


def _parse_game(game):
  link = game.select_one('a')
  team1 = game.select_one('span.competition-cell-side1 > span.name')
  team2 = game.select_one('span.competition-cell-side2 > span.name')
  score = game.select_one('span.competition-cell-score')
  time = game.select_one('span.competition-cell-time')
  if time is None: # if game hasn't started yet, its called cell-status
    time = game.select_one('span.competition-cell-status')

  score_strings = util.soup.get_stripped_strings(score)

  return BaseballGame(
    util.soup.get_stripped_strings(team1)[0],
    util.soup.get_stripped_strings(team2)[0],
    # score has time in it (<score> 4-2 <time> 11:00 </time> </score>)
    # so ['4-2', '11:00'], take score[0] if len==2, else its just time ['11:00']
    score_strings[0] if len(score_strings) == 2 else '',
    util.soup.get_stripped_strings(time)[0],
    GAMES + link.get('href')
  )
