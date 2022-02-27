import os
import requests

USER_NAME = "bl4ckst4ff"
TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": "bl4ckst4ff",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# commented out because i have now created the user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": "",
    "name": "",
    "unit": "",
    "type": "",
    "color": ""

}
graph_response = requests.post(graph_endpoint, TOKEN)

