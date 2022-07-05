from sports_streaming import util


def create_table(sports):
  header = ['#', 'Sport']
  rows = [
    [i, sport]
    for i, sport in enumerate(sports, start=1)
  ]
  return util.tables.create_base_table(header, rows)
