import requests
from bs4 import BeautifulSoup

res = requests.get('https://solved.ac/profile/sjy9484')
soup = BeautifulSoup(res.content, 'html.parser')
rating = soup.find('span', 'ProfileRatingCard__AcRatingDisplay-sc-989yd6-0 jaNtBE')
print(rating)
