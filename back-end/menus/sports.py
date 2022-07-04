import tables
import games
import util
from . import mlb_games


SPORTS = ['Baseball', 'Basketball', 'Football']

def show_menu():
  table = tables.sports.create_table(SPORTS)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(SPORTS))
  chosen = SPORTS[choice-1]
  print(f'You chose: {choice} - {chosen}')
  if chosen == 'Baseball':
    mlb_games.show_menu(games.mlb.get_games())
