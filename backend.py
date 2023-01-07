import requests


API_key = "74d0619acd1fccfb219a02f6b569af6f"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    total_values = 8 * forecast_days
    filtered_data = filtered_data[:total_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=3))
