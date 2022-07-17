import requests
import logging
from bs4 import BeautifulSoup


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
