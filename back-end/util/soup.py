import requests
from requests_html import AsyncHTMLSession
import asyncio
import pyppeteer
from bs4 import BeautifulSoup

class AsyncHTMLSessionFixed(AsyncHTMLSession):
  """
  pip3 install websockets==6.0 --force-reinstall
  """
  def __init__(self, **kwargs):
    super(AsyncHTMLSessionFixed, self).__init__(**kwargs)
    self.__browser_args = kwargs.get("browser_args", ["--no-sandbox"])

  @property
  async def browser(self):
    if not hasattr(self, "_browser"):
      self._browser = await pyppeteer.launch(
        ignoreHTTPSErrors=not(self.verify),
        headless=True, handleSIGINT=False,
        handleSIGTERM=False, handleSIGHUP=False,
        args=self.__browser_args
      )
    return self._browser


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


async def get_async_soup(url):
  # asyncio.set_event_loop(asyncio.SelectorEventLoop())
  # session = HTMLSession()

  # asession = AsyncHTMLSession(loop=asyncio.new_event_loop())
  # r = session.get(url)
  # r.html.render(timeout=30)
  # soup = BeautifulSoup(r.html.html, features="html.parser")

  asession = AsyncHTMLSessionFixed()
  r = await asession.get(url)
  await r.html.arender(timeout=30)
  soup = BeautifulSoup(r.html.html, features="html.parser")

  return soup
