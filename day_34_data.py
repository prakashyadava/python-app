import requests
import html
response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
data = response.json()
for _ in data["results"]:
    _["question"] = html.unescape(_["question"])
question_data = data["results"]
