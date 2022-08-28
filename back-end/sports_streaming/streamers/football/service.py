import re
from sports_streaming import util
from sports_streaming.streamers.models import FootballStreamer
from sports_streaming.streams.models import FootballStream


NFL_STREAMER_TABLE = 'https://sportscentral.io/streams-table/{0}/american-football?new-ui=1'

def get_best_streamer(streams_link):
  return _get_weak_spell(streams_link)


def _get_weak_spell(streams_link):
  game_id = _get_game_id(streams_link)
  streamers = get_streamers(game_id)
  weak_spell = next(
    (streamer for streamer in streamers if streamer.name == 'Weak_Spell'),
    None
  )
  if weak_spell is None:
    raise util.errors.NoWeakSpellFound(game_id=game_id)
  return weak_spell

def _get_game_id(streams_link):
  pattern = 'streamsMatchId = ([0-9]+);'
  soup = util.soup.get_soup(streams_link)
  scripts = soup.select('script')
  game_id = None
  for script in scripts:
    content = script.string
    if content is None:
      continue
    match = re.search(pattern, content)
    if match is None:
      continue
    game_id = match.group(1)
    break
  if game_id is None:
    raise util.errors.NoGameIdFound(streams_link=streams_link)
  return game_id

def get_streamers(game_id):
  soup = util.soup.get_soup(NFL_STREAMER_TABLE.format(game_id))

  # headers = soup.select_one('#streams table > thead > tr')
  streamers = soup.select('table > tbody > tr')
  streamers = [
    _parse_streamer(streamer, rank)
    for rank, streamer in enumerate(streamers, start=1)
  ]
  if not streamers:
    raise util.errors.NoStreamersFound(game_id=game_id)
  return streamers


# td elements within each streamer tr
# 1 = logo
# 2 = rank
# 3 = name
# 4 = reputation
# 5 = quality
# 6 = language
# 7 = ads
# 8 = channel
# 9 = popularity
def _parse_streamer(streamer, rank):
  name = streamer.select_one(':nth-child(3)')
  reputation = streamer.select_one(':nth-child(4)')
  quality = streamer.select_one(':nth-child(5)')
  ads = streamer.select_one(':nth-child(7)')
  channel = streamer.select_one(':nth-child(8)')
  popularity = streamer.select_one(':nth-child(9) span.votes-count')

  return FootballStreamer(
    util.soup.get_stripped_strings(name)[0],
    FootballStream(streamer.get('data-stream-link')),
    str(rank),
    util.soup.get_stripped_strings(reputation)[0],
    util.soup.get_stripped_strings(quality)[0],
    util.soup.get_stripped_strings(ads)[0],
    util.soup.get_stripped_strings(channel)[0],
    util.soup.get_stripped_strings(popularity)[0]
  )
