import requests
import os
from dotenv import load_dotenv

load_dotenv()

pixela_url = "https://pixe.la/v1/users"

create_user_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

create_graph_params = {
    "id": "graph1",
    "name": "Commits Tracker",
    "unit":"commit",
    "type" : "int",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN" : os.getenv("PIXELA_TOKEN")
}

create_entry_params = {
    "date" : "20240203",
    "quantity": "10"
}
#-> for creating a user -<#
# response = requests.post(pixela_url, json = create_user_params) 
# print(response.json())

#-> for creating a new graph -<#
# response = requests.post(f"{pixela_url}/{os.getenv("PIXELA_USERNAME")}/graphs", json=create_graph_params, headers=headers)
# print(response.json())

#-> for adding a pixel to graph -<#
response = requests.post(f"{pixela_url}/{os.getenv("PIXELA_USERNAME")}/graphs/graph1", json=create_entry_params, headers=headers)
print(response.json())