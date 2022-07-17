from mitmproxy import http
from bs4 import BeautifulSoup


dependencies = {
  '//cdn.jsdelivr.net/npm/@clappr/player@0.4.0/dist/clappr.min.js',
  '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/hlsjs-p2p-engine.min.js',
  '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/clappr-plugin.min.js',
  '//cdn.jsdelivr.net/gh/clappr/clappr-level-selector-plugin@latest/dist/level-selector.min.js'
}


class Filter:
  def __init__(self):
    pass    

  def filterScriptTags(self, tag):
    return (
      tag.name == 'script' and
      (tag['src'] not in dependencies if tag.has_attr('src') else True)
    )

  def response(self, flow: http.HTTPFlow) -> None:
    if flow.request.path.startswith('/streams/'):
      soup = BeautifulSoup(flow.response.content, features="html.parser")
      tags = soup.findAll(self.filterScriptTags)
      for i, tag in enumerate(tags):
        if i == 0: # first tag is what we want
          new_tag = soup.new_tag('script')
          new_script = tag.string.replace('gethlsUrl(vidgstream, )', 'gethlsUrl(vidgstream)')
          new_tag.string = new_script
          tag.replace_with(new_tag)
        else:
          tag.decompose()
      flow.response.text = str(soup)


addons = [Filter()]
