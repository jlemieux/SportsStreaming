from sports_streaming import util, cli, games


SPORTS = ['Baseball', 'Basketball', 'Football']


def show_menu():
  table = cli.tables.sports.create_table(SPORTS)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(SPORTS))
  chosen = SPORTS[choice-1]
  print(f'You chose: {choice} - {chosen}')
  if chosen == 'Baseball':
    cli.menus.baseball.games.show_menu(games.baseball.service.get_games())
