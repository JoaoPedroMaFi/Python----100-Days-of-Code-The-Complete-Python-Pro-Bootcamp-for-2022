import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
print(response.content.decode())
website_html = response.content.decode()

soup = BeautifulSoup(website_html, "html.parser")
all_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
all_titles.reverse()

with open("top_100_movies.txt", "w", encoding='utf-8') as file:
    file.write("\n".join(all_titles))
