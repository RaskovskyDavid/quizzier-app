import requests

path = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url=path, params=parameters)
data = response.json()["results"]
question_data = data
