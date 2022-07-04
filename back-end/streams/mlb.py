from bs4 import BeautifulSoup
import util
import asyncio


def fetch_stream(streamer):
  return get_direct_stream(bypass_tinyurl_site(streamer))

def bypass_tinyurl_site(streamer):
  loop = asyncio.new_event_loop()
  soup = loop.run_until_complete(
    util.soup.get_async_soup(streamer.stream.link_from_streamer)
  )
  # soup = util.soup.get_soup(streamer.stream.link_from_streamer, render_js=True)
  continue_button = soup.find('a', string='Click Here to Watch')
  return continue_button.get('href')

# works for weak-streams embed link
def get_direct_stream(streaming_site_link):
  soup = util.soup.get_soup(streaming_site_link)
  text_area_with_iframe = soup.select_one('#gamecard > textarea')
  iframe_html = util.soup.get_stripped_strings(text_area_with_iframe)[0]
  iframe = BeautifulSoup(iframe_html, features="html.parser").select_one('iframe')
  return iframe.get('src')
