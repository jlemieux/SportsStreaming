from sports_streaming import util, cli, streams


def show_menu(streamers):
  table = cli.tables.baseball.streamers.create_table(streamers)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(streamers))
  chosen = streamers[choice-1]
  print(f'You chose: {choice} - {chosen}')
  _watch_streamer(chosen)


def _watch_streamer(streamer):
  stream = streams.baseball.service.get_stream(streamer)
  
  print(f'Streamer: {streamer.name}')
  print(f'Opening browser to: {stream}')
