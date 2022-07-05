from sports_streaming import util


class Stream(util.printing.DataModel):
  def __init__(self, link_from_streamer):
    self.link_from_streamer = link_from_streamer


class BaseballStream(Stream):
  def __init__(self, link_from_streamer):
    super().__init__(link_from_streamer)
