import util


class Stream(util.printing.DataModel):
  def __init__(self, game, link_from_streamer):
    self.game = game
    self.link_from_streamer = link_from_streamer
    self.direct_link = None


class MLBStream(Stream):
  def __init__(self, game, link_from_streamer):
    super().__init__(game, link_from_streamer)
