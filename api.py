import requests

personal_access_token = "kzWHayyiXOkEyOeIjhLMQWMrOAIblEOwCxYQHrOf"


def get_price_suggestions(vinyl_id):
    url = f"https://api.discogs.com/marketplace/price_suggestions/{vinyl_id}"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()


def get_market_snapshot(vinyl_id):
    url = f"https://api.discogs.com/marketplace/stats/{vinyl_id}"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()


def get_info(vinyl_id):
    url = f"https://api.discogs.com/releases/{vinyl_id}"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()


def get_have_want_ratio(vinyl_id):
    url = f"https://api.discogs.com/releases/{vinyl_id}/stats"
    headers = {"Authorization": f"Discogs token=" + personal_access_token}
    response = requests.get(url, headers=headers)
    return response.json()
