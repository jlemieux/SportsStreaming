import tables
import streams
import util


def show_menu(streamers):
  table = tables.mlb_streamers.create_table(streamers)
  print(table.draw())
  choice = util.menus.make_choice(max_choice=len(streamers))
  chosen = streamers[choice-1]
  print(f'You chose: {choice} - {chosen}')
  watch_streamer(chosen)


def watch_streamer(streamer):
  if streamer.stream.direct_link is None:
    streamer.stream.direct_link = streams.mlb.fetch_stream(streamer)
  
  print(f'Watching stream for: {streamer.stream.game}')
  print(f'Streamer: {streamer.name}')
  print(f'Opening browser to: {streamer.stream.direct_link}')
