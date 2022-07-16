import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote


url = 'https://tinyurl.is/YND4?sport=baseball'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

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

stream_site_link = continue_button.get('href')

breakpoint()