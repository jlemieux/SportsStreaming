import logging
from sports_streaming import util
from sports_streaming.games.models import FootballGame


GAMES = 'https://reddit.nflbite.com/'
LOGGER = logging.getLogger('main-app')

def get_games():
  soup = util.soup.get_soup(GAMES)
  competitions = soup.select('#competitions > .competition')
  # _date = soup.select_one('#competitions > .date')
  games = _parse_games(competitions)
  if not games:
    raise util.errors.NoGamesFound(sport='football')
  return games


def _parse_games(competitions):
  games = []
  for competition in competitions:
    competition_name = util.soup.get_stripped_strings(
      competition.select_one('.info > .name')
    )[0]
    matches = competition.select('.matches > div')
    for match in matches:
      try:
        parsed_game = _parse_game(match, competition_name)
        games.append(parsed_game)
      except Exception as e:
        LOGGER.error('Could not parse football game.')
        LOGGER.error(e)
  return games

def _parse_game(match, competition_name):
  clickable_card = match.select_one('a')
  link = clickable_card.get('href')
  info_box, team1, team2 = clickable_card.select('.match > div')
  _time = info_box.select_one('.status')
  team1_name = team1.select_one('.team-name')
  team1_score = util.soup.get_stripped_strings(
    team1.select_one('.score')
  )[0]
  team2_name = team2.select_one('.team-name')
  team2_score = util.soup.get_stripped_strings(
    team2.select_one('.score')
  )[0]
  if not team1_score or not team2_score:
    score = ''
  else:
    score = f'{team1_score} - {team2_score}'
  return FootballGame(
    util.soup.get_stripped_strings(team1_name)[0],
    util.soup.get_stripped_strings(team2_name)[0],
    score,
    util.soup.get_stripped_strings(_time)[0],
    link,
    competition_name,
  )
