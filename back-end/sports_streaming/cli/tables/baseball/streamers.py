from sports_streaming import util


def create_table(streamers):
  header = ['#', 'Name', 'Reputation', 'Quality', 'Ads', 'Channel', 'Popularity']
  rows = [
    [i, s.name, s.reputation, s.quality, s.ads, s.channel, s.popularity]
    for i, s in enumerate(streamers, start=1)
  ]
  return util.tables.create_base_table(header, rows)
