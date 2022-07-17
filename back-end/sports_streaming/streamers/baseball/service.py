from sports_streaming import util
from sports_streaming.streamers.models import BaseballStreamer
from sports_streaming.streams.models import BaseballStream


MLB_STREAMER_TABLE = 'https://sportscentral.io/streams-table/{0}/baseball?new-ui=1'


def get_best_streamer(game_id):
  return _get_weak_spell(game_id)


def _get_weak_spell(game_id):
  streamers = get_streamers(game_id)
  weak_spell = next(
    (streamer for streamer in streamers if streamer.name == 'Weak_Spell'),
    None
  )
  if weak_spell is None:
    raise util.errors.NoWeakSpellFound(game_id=game_id)
  return weak_spell


def get_streamers(game_id):
  soup = util.soup.get_soup(MLB_STREAMER_TABLE.format(game_id))

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

  return BaseballStreamer(
    util.soup.get_stripped_strings(name)[0],
    BaseballStream(streamer.get('data-stream-link')),
    str(rank),
    util.soup.get_stripped_strings(reputation)[0],
    util.soup.get_stripped_strings(quality)[0],
    util.soup.get_stripped_strings(ads)[0],
    util.soup.get_stripped_strings(channel)[0],
    util.soup.get_stripped_strings(popularity)[0]
  )
