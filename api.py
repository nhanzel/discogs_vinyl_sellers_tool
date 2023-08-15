import requests

personal_access_token = ""


def set_token(token):
    global personal_access_token
    personal_access_token = token


def get_vinyl_ids(folder_name, username):
    url = f"https://api.discogs.com/users/{username}/collection/folders/{folder_name}/releases"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return [item["id"] for item in response.json()["releases"]]


def get_price_suggestions(vinyl_id):
    url = f"https://api.discogs.com/marketplace/price_suggestions/{vinyl_id}"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()


def get_info(vinyl_id):
    url = f"https://api.discogs.com/releases/{vinyl_id}"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()
