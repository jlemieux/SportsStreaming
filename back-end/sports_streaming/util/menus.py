def make_choice(max_choice):
  while True:
    choice = input('Select #: ')
    if not valid_choice(choice, max_choice):
      continue
    break
  return int(choice)


def valid_choice(choice, max_choice):
  if not choice:
    return False
  
  try:
    choice = int(choice)
  except:
    return False
  
  if not 0 < choice <= max_choice:
    return False
  
  return True
