import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
# returns a list, and each item is an instance of the Tag Class
questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText(),
          "--",
          question.select_one(".vote-count-post").getText())
