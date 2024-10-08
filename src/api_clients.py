import requests


def get_location_info(ip):  
    URL = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data["countryName"],
        "city": data["cityName"],
        "region": data["regionName"]
    }

