from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

response = urlopen('https://www.naver.com/') 
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select('li.nav_item'):
    print(anchor.get_text())