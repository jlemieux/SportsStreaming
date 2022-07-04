import util
from .models import MLBStreamer
from streams.models import MLBStream

# # testing only
# from bs4 import BeautifulSoup
# import mock_data

MLB_STREAMER_TABLE = 'https://sportscentral.io/streams-table/{0}/baseball?new-ui=1'

def get_streamers(game):
  soup = util.soup.get_soup(MLB_STREAMER_TABLE.format(game.id))
  # soup = BeautifulSoup(mock_data.mock_streamers, features="html.parser")

  # headers = soup.select_one('#streams table > thead > tr')
  streamers = soup.select('table > tbody > tr')
  streamers = streamers[:5] # take top 5 streamers
  return [
    parse_streamer(streamer, rank, game)
    for rank, streamer in enumerate(streamers, start=1)
  ]


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
def parse_streamer(streamer, rank, game):
  name = streamer.select_one(':nth-child(3)')
  reputation = streamer.select_one(':nth-child(4)')
  quality = streamer.select_one(':nth-child(5)')
  ads = streamer.select_one(':nth-child(7)')
  channel = streamer.select_one(':nth-child(8)')
  popularity = streamer.select_one(':nth-child(9) span.votes-count')

  return MLBStreamer(
    util.soup.get_stripped_strings(name)[0],
    MLBStream(game, streamer.get('data-stream-link')),
    str(rank),
    util.soup.get_stripped_strings(reputation)[0],
    util.soup.get_stripped_strings(quality)[0],
    util.soup.get_stripped_strings(ads)[0],
    util.soup.get_stripped_strings(channel)[0],
    util.soup.get_stripped_strings(popularity)[0]
  )
