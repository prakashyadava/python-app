import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "bchjbhj4bhbshjfb4tb5t75"
USERNAME = "duke12prakash"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
    "timezone": "Asia/Kolkata"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
graph_pixel_config = {
    "date":"20211012",
    "quantity": "5.41"
}
graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
response = requests.post(url=graph_pixel_endpoint,json=graph_pixel_config,headers=headers)
print(response.text)
