from sports_streaming import util, streamers, cli


def show_menu(games):
  table = cli.tables.baseball.games.create_table(games)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(games))
  chosen = games[choice-1]
  print(f'You chose: {choice} - {chosen}')
  cli.menus.baseball.streamers.show_menu(streamers.baseball.service.get_streamers(chosen.id))
