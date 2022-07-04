from texttable import Texttable


def create_base_table(header, rows):
  table = Texttable(max_width=0)
  nCols = len(header)
  table.set_cols_align(['c'] * nCols)
  table.set_cols_dtype(['t'] * nCols)
  table.set_cols_valign(['m'] * nCols)
  table.add_rows([header] + rows)
  return table
