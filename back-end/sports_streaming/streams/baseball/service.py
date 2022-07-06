from bs4 import BeautifulSoup
import asyncio
import logging
from sports_streaming import util

LOGGER = logging.getLogger('main-app')

def get_stream(streamer):
  return _get_direct_stream(_bypass_tinyurl_site(streamer))


def _bypass_tinyurl_site(streamer):
  if util.async_html.AsyncHTMLSessionFixed.has_instance():
    LOGGER.info('Using existing singleton!')
    asession = util.async_html.AsyncHTMLSessionFixed.instance(None)
    LOGGER.info('Singleton retrieved!')
  else:
    LOGGER.info('Making new instance of Session!')
    asession = _get_asession()
    LOGGER.info('New instance retrieved!')
    

  # loop = asyncio.new_event_loop()
  loop = asession.custom_loop
  soup = loop.run_until_complete(
    util.soup.get_async_soup(streamer.stream.link_from_streamer, asession)
  )
  continue_button = soup.find('a', string='Click Here to Watch')
  return continue_button.get('href')

def _get_asession():
  loop = asyncio.new_event_loop()
  asession = loop.run_until_complete(
    _asession(loop)
  )
  return asession

async def _asession(loop):
  return util.async_html.AsyncHTMLSessionFixed.instance(loop)

# works for weak-streams embed link
def _get_direct_stream(streaming_site_link):
  soup = util.soup.get_soup(streaming_site_link)
  text_area_with_iframe = soup.select_one('#gamecard > textarea')
  iframe_html = util.soup.get_stripped_strings(text_area_with_iframe)[0]
  iframe = BeautifulSoup(iframe_html, features="html.parser").select_one('iframe')
  return iframe.get('src')
