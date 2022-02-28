import os
import requests
from datetime import datetime

USER_NAME = "bl4ckst4ff"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": os.environ.get("PIXELA_TOKEN"),
#     "username": "bl4ckst4ff",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# commented out because i have now created the user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Reading Graph",
#     "unit": "Pg",
#     "type": "int",
#     "color": "momiji",
# }
#
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

yesterday = datetime(year=2022, month=0o2, day=26).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")
# add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# add_pixel_params = {
#     "date": f"{yesterday}",
#     "quantity": "30",
# }
#
# add_pixel_response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)

# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}"
# update_pixel_params = {
#     "quantity": "15",
# }
#
# update_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)

delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}"
delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
