import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://recharge.pulsebroadband.in/static/'

# Send a GET request to the URL
response = requests.get(url)
print(response.text)
# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# Find specific elements on the webpage
# For example, let's find all the links (anchor tags) on the page
# links = soup.find_all('a')

# # Print out the URLs of all the links found
# for link in links:
#     print(link.get('href'))
