from twython import Twython
from datetime import datetime

import requests
import json

with open("config.json", "r") as f:
    config = json.load(f)


def update_desc(text):
    twitter = Twython(
        app_key=config["consumer_key"],
        app_secret=config["consumer_secret"],
        oauth_token=config["access_token"],
        oauth_token_secret=config["access_token_secret"],
    )

    data = twitter.update_profile(description=text)
    return data


def get_weather_of(city):
    base_url = (
        "http://api.openweathermap.org/data/2.5/weather?appid="
        + config["weather"]
        + "&q="
        + city
        + "&units="
        + config["units"]
    )
    response = requests.get(base_url)
    data = response.json()
    return data


def generate_desc_content(weather):
    now = datetime.now().strftime("%H:%M")

    desc = weather["weather"][0]["description"]
    temp = round(weather["main"]["temp"])
    temp_symbol = (
        "°C"
        if config["units"] == "metric"
        else "°F"
        if config["units"] == "imperial"
        else "K"
    )
    feels_like = round(weather["main"]["feels_like"])
    city = config["city"]

    return (
        "Current weather in "
        + city
        + ": "
        + str(temp)
        + str(temp_symbol)
        + ". "
        + "Feels like "
        + str(feels_like)
        + str(temp_symbol)
        + ". "
        + str(desc.upper())
        + " | Last update: "
        + now
        + " | Made using Python"
    )


def main():
    weather = get_weather_of(config["city"])
    desc_content = generate_desc_content(weather)

    update_desc(desc_content)

    log_prefix = "[" + datetime.now().strftime("%H:%M") + "]"

    print(log_prefix + " Successfully updated description")


if __name__ == "__main__":
    main()
