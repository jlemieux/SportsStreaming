import requests
import logging
from bs4 import BeautifulSoup
from sports_streaming.util.async_html import AsyncHTMLSessionFixed
from pyppeteer.errors import PageError


LOGGER = logging.getLogger('main-app')

def get_stripped_strings(soup):
  if soup is None:
    return ['']
  
  # generator of all strings in this tag or child tags
  gen = soup.stripped_strings
  if not gen:
    return ['']

  strings = list(gen) 
  if not strings:
    return ['']

  return strings


def get_soup(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, features="html.parser")
  return soup


async def get_async_soup(url, asession):
  for tries in range(1, 4):
    try:
      r = await asession.get(url)
      await r.html.arender(timeout=30)
      soup = BeautifulSoup(r.html.html, features="html.parser")
      break
    except PageError:
      LOGGER.warning(f'PageError for async page load on try={tries}... trying {3-tries} more times.')
      if tries == 3:
        raise

  return soup
