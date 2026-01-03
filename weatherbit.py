import requests
import config
from datetime import datetime

KEY = config.api_key
url = "https://api.weatherbit.io/v2.0/current"


def forecast_dscrpt(description, temp, precip_rating, wnd_spd, app_temp, sunrise, sunset):

    print('=' * 40)
    print("      ==== FORECAST DESCRIPTION ==== ")
    print('=' * 40 + '\n')
    print('=' * 40)
    print(description)
    print('=' * 40)
    print(f"Temperature: {temp}°F")
    print('=' * 40) 
    print(f"Feels like { app_temp}°F")
    print('=' * 40)
    if precip_rating > 0: 
        print("Raining") 
    else:
        print("No precipitation")
    print('=' * 40)
    # Convert m/s to mph
    print(f"Wind speed: {int(wnd_spd)}MPH")
    print('=' * 40)
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

def main():
    print("=" * 40)
    usr_city = input("Enter a city to get weather details: ")
    usr_cntry = input("Enter a country code (e.g. US, GB, or JP): ")
    state = input("Enter a State code (e.g. CA, IL, or NY): ")
    city = f"{usr_city.strip().title()},{usr_cntry.strip().upper()}"

    print('=' * 38)
    print(f"=======  WEATHER FORECAST =======")
    print(f"        {usr_city.title()}, {state.strip().upper()}")

    params = {
    "city": city, 
    "key": KEY,
    'units': "I"
    }

    # DEBUG
    response = requests.get(url, params=params)
    data = response.json()
    print("Parsed JSON:", data)


    temp = data['data'][0]['temp']
    app_temp = data['data'][0]['app_temp']
    precip_rating = data['data'][0]['precip']
    wnd_spd = data['data'][0]['wind_spd'] * 2.23694
    description = data['data'][0]['weather']['description']
    state = data['data'][0]['state_code']
    city = data['data'][0]['city_name']
    sunrise = data['data'][0]['sunrise']
    sunset = data['data'][0]['sunset']

    forecast_dscrpt(description, temp, precip_rating, wnd_spd, app_temp, sunrise, sunset)


if __name__ == '__main__':
    main()