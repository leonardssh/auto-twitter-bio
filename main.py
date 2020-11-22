# Used to make call to the twitter API
from twython import Twython

# Used to read the config file
from datetime import datetime

# Used to make call to the openweathermap.org API
import requests

# Used to read the config file
import json

# Read the config file
with open("config.json", "r") as f:
    config = json.load(f)


def update_bio(text):
    """
    Update the Twitter biography of the user
    Args:
        text (str): The new biography content
    Returns:
        data (any): The Twitter response
    """

    twitter = Twython(
        app_key=config["consumer_key"],
        app_secret=config["consumer_secret"],
        oauth_token=config["access_token"],
        oauth_token_secret=config["access_token_secret"],
    )

    data = twitter.update_profile(description=text)
    return data


def get_weather_of(city):
    """
    Get the weather of a specific city
    Args:
        city (str): The name of the city whose weather we want
    Returns:
        weather (str): The weather of the city
    """

    # Read the config file
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

    # Returns weather info
    return data


def generate_bio_content(weather):
    """
    Generate the bio content
    Args:
        weather (str): The weather of the city
    Returns:
        bio_content (str): The final bio content
    """

    # The current time (hours and minutes)
    now = datetime.now().strftime("%I:%M %p")

    # Some useful variables
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

    # Returns the final string wich contain the city, the current temp, the felt temp, the weather and the last update
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
    """
    Main code which call the other functions
    """

    # Get the weather of the city
    weather = get_weather_of(config["city"])

    # Get the bio content
    bio_content = generate_bio_content(weather)

    # Update the biography
    update_bio(bio_content)

    # Log
    log_prefix = "[" + datetime.now().strftime("%I:%M %p") + "]"

    print(log_prefix + " Successfully updated biography")


if __name__ == "__main__":
    main()
