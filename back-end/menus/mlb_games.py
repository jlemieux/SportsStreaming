import tables
import streamers
import util
from . import mlb_streamers

def show_menu(games):
  table = tables.mlb_games.create_table(games)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(games))
  chosen = games[choice-1]
  print(f'You chose: {choice} - {chosen}')
  mlb_streamers.show_menu(streamers.mlb.get_streamers(chosen))
