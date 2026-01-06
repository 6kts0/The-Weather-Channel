"""
Import your weatherbit API key into config.py
"""

import requests
import config
from datetime import datetime
import ollama

KEY = config.api_key
url = "https://api.weatherbit.io/v2.0/current"


def forecast_dscrpt(description, temp, precip_rating, wnd_spd, app_temp, ollama_fil_response):

    print('=' * 45)
    print("+         =======  SUMMARY  =======         +")
    print('=' * 45 + '\n')
    print(f"{ollama_fil_response}")
    print('=' * 45)
    print(f"{description}")
    print('=' * 45)
    print(f"Temperature: {temp}°F")
    print('=' * 45) 
    print(f"Feels like {app_temp}°F")
    print('=' * 45)
    if precip_rating > 0: 
        print("Raining") 
    else:
        print("No precipitation")
    print('=' * 45)
    print(f"Wind speed: {int(wnd_spd)}MPH")
    print('=' * 45)

def ollama_descript(data):
    client = ollama.Client()
    ollama_response = client.chat(
        model='Konsumer/weather:latest',
        messages=[
            {
                "role": "user",
                "content": f"Summarize this weather data in 100 words or less: {data}. Use Imperial units."
            }
        ]
    )

    ollama_fil_response = (ollama_response['message']['content'])
    return ollama_fil_response
    


def main():
    print("=" * 45)
    usr_city = input("Enter a city to get weather details: ")
    usr_cntry = input("Enter a country code (e.g. US, GB, or JP): ")
    state = input("Enter a State code (e.g. CA, IL, or NY): ")
    city = f"{usr_city.strip().title()},{usr_cntry.strip().upper()}"

    print('=' * 45)
    print(f"      =======  WEATHER FORECAST  =======    ")
    print(f"                  {usr_city.title()}, {state.strip().upper()}")

    params = {
    "city": city, 
    "key": KEY,
    'units': "I"
    }

    # DEBUG
    response = requests.get(url, params=params)
    data = response.json()
    #print("Parsed JSON:", data)

    
    temp = data['data'][0]['temp']
    app_temp = data['data'][0]['app_temp']
    precip_rating = data['data'][0]['precip']
    wnd_spd = data['data'][0]['wind_spd'] * 2.23694
    description = data['data'][0]['weather']['description']
    state = data['data'][0]['state_code']
    city = data['data'][0]['city_name']

    ollama_summary = ollama_descript(data)
    forecast_dscrpt(description, temp, precip_rating, wnd_spd, app_temp, ollama_summary)

if __name__ == '__main__':
    main()