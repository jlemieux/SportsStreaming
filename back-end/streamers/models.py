import util


class Streamer(util.printing.DataModel):
  def __init__(self, name, stream):
    self.name = name
    self.stream = stream


class MLBStreamer(Streamer):
  def __init__(
    self, name, stream, rank, reputation,
    quality, ads, channel, popularity
  ):
    super().__init__(name, stream)
    self.rank = rank
    self.reputation = reputation
    self.quality = quality
    self.ads = ads
    self.channel = channel
    self.popularity = popularity
