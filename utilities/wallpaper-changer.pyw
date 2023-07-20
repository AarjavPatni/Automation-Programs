import pendulum
import requests
import ctypes
from time import sleep

# Set your latitude and longitude
LATITUDE = 25.2048
LONGITUDE = 55.2708

# API endpoint to get the sunrise and sunset times
API_URL = 'https://api.sunrise-sunset.org/json'

# Windows API constant to set the desktop wallpaper
SPI_SETDESKWALLPAPER = 20

# Paths to the daytime and nighttime wallpapers
DAYTIME_WALLPAPER = r"C:\Users\Aarjav\Pictures\Wallpapers\daytime.jpg"
NIGHTTIME_WALLPAPER = r"C:\Users\Aarjav\Pictures\Wallpapers\nighttime.png"


def get_sunrise_sunset():
    # Get the current date and time in your timezone
    now = pendulum.now()

    # Construct the API request
    params = {
        'lat': LATITUDE,
        'lng': LONGITUDE,
        'formatted': 0,
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    # Parse the sunrise and sunset times from the API response
    sunrise_time = pendulum.parse(
        data['results']['sunrise']).in_timezone(now.timezone_name)
    sunset_time = pendulum.parse(
        data['results']['sunset']).in_timezone(now.timezone_name)

    # Return the sunrise and sunset times
    return sunrise_time, sunset_time


def set_wallpaper(wallpaper_path):
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    # Call the Windows API to set the desktop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        wallpaper_path,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )


if __name__ == '__main__':
    # Get the sunrise and sunset times
    sunrise_time, sunset_time = get_sunrise_sunset()

    # Get the current time
    now = pendulum.now()

    for i in range(2):
        # Determine whether it is currently daytime or nighttime
        if sunrise_time < now < sunset_time:
            # Set the daytime wallpaper
            set_wallpaper(DAYTIME_WALLPAPER)
        else:
            # Set the nighttime wallpaper
            set_wallpaper(NIGHTTIME_WALLPAPER)

        sleep(10)
