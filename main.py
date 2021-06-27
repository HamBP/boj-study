import requests
from bs4 import BeautifulSoup

bojID = 'sjy9484'
res = requests.get('https://solved.ac/profile/' + bojID)
soup = BeautifulSoup(res.content, 'html.parser')
ratingTag = soup.find('span', 'ProfileRatingCard__AcRatingDisplay-sc-989yd6-0 jaNtBE')
rating = ratingTag.contents[0].contents[0]
print(rating)
