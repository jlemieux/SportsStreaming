class DataModel:
  def __repr__(self):
    items = []
    for prop, value in self.__dict__.items():
      try:
        item = "%s = %r" % (prop, value)
        assert len(item) < 60
      except:
        item = "%s: <%s>" % (prop, value.__class__.__name__)
      items.append(item)

    return "%s(%s)" % (self.__class__.__name__, ', '.join(items))
