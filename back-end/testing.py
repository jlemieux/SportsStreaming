import traceback

try:
  l = []
  print(l[0])
except Exception as e:
  d = {'err': traceback.format_exc().split('\n')}
  print(d)
  for ll in d['err']:
    print(ll)
