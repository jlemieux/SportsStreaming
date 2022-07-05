import requests
from bs4 import BeautifulSoup
from sports_streaming.util.async_html import AsyncHTMLSessionFixed


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
  asession = AsyncHTMLSessionFixed()
  r = await asession.get(url)
  await r.html.arender(timeout=30)
  soup = BeautifulSoup(r.html.html, features="html.parser")

  return soup
