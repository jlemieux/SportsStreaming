from mitmproxy import http
from bs4 import BeautifulSoup


dependencies = {
  '//cdn.jsdelivr.net/npm/@clappr/player@0.4.0/dist/clappr.min.js',
  '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/hlsjs-p2p-engine.min.js',
  '//cdn.jsdelivr.net/npm/cdnbye@latest/dist/clappr-plugin.min.js',
  '//cdn.jsdelivr.net/gh/clappr/clappr-level-selector-plugin@latest/dist/level-selector.min.js'
}


class PatchStream:
  def __init__(self):
    pass

  def get_desired_script_tags(self, tag):
    return (
      tag.name == 'script' and
      (tag['src'] not in dependencies if tag.has_attr('src') else True)
    )

  def response(self, flow: http.HTTPFlow) -> None:
    if flow.request.path.startswith('/streams/'):
      soup = BeautifulSoup(flow.response.content, features="html.parser")
      tags = soup.findAll(self.get_desired_script_tags)
      for i, tag in enumerate(tags):
        if i == 0: # first tag is what we want
          new_tag = soup.new_tag('script')
          # patch for Chromium < v60
          new_script = tag.string.replace('gethlsUrl(vidgstream, )', 'gethlsUrl(vidgstream)')

          # make player smaller, so it's easier to go into fullscreen
          new_script = new_script.replace("height: '100%'", "height: '50%'")
          new_script = new_script.replace("width: '100%'", "width: '50%'")
          new_script = new_script.replace("offsetWidth,", "offsetWidth/2,")

          new_tag.string = new_script
          tag.replace_with(new_tag)
        else:
          tag.decompose()
      flow.response.text = str(soup)


addons = [PatchStream()]
