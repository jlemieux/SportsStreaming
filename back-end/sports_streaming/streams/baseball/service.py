import re
from urllib.parse import unquote
from bs4 import BeautifulSoup
import logging
from sports_streaming import util


LOGGER = logging.getLogger('main-app')


def get_stream(streamer):
  return _get_direct_stream(_bypass_tinyurl_site(streamer))


def _bypass_tinyurl_site(streamer):
  soup = util.soup.get_soup(streamer.stream.link_from_streamer)
  df_pattern = re.compile("dF\('(.*)'\)")
  df_content = df_pattern.search(soup.script.string).group(1)

  # last char is offset
  offset = int(df_content[-1])

  # everything but last char is content
  decoded = unquote(df_content[:-1])

  # take offset of each decoded char
  transformed = ''.join([chr(ord(c)-offset) for c in decoded])

  # decode again
  real_html = unquote(transformed)

  soup = BeautifulSoup(real_html, features="html.parser")

  continue_button = soup.find('a', string='Click Here to Watch')

  return continue_button.get('href')


# works for weak-streams embed link
def _get_direct_stream(streaming_site_link):
  soup = util.soup.get_soup(streaming_site_link)
  text_area_with_iframe = soup.select_one('#gamecard > textarea')
  iframe_html = util.soup.get_stripped_strings(text_area_with_iframe)[0]
  iframe = BeautifulSoup(iframe_html, features="html.parser").select_one('iframe')
  return iframe.get('src')
