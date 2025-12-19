# Domestic Weather Forecaster

A simple Python application for fetching and displaying local weather forecasts.

## Features

- Retrieves current weather conditions for your location
- Displays multi-day weather forecasts
- Shows temperature, humidity, wind speed, and conditions
- Easy-to-read command-line interface

## Requirements

- Python 3.7 or higher
- `requests` library for API calls
- An API key from a weather service provider (e.g., OpenWeatherMap, WeatherAPI)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/The-Weather-Channel.git
cd The-Weather-Channel
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application from the command line:

```bash
python weather_forecaster.py
```

You will be prompted to specify a location:

```bash
usr_map = input("Enter a city to fetch the current weather: ")
```

## Example Output

```
=================================================================

                 --- TODAYS FORECAST ---

=================================================================
Enter a city to fetch the current weather: new york
=================================================================
The weather in New York today is 49 degrees fahrenheit at 03:17PM.
=================================================================

               --- Near Future Forecast ---

=================================================================
On 2025/12/18 the temperature will be 41 degrees fahrenheit
ADVISORY: Its cold as fuuuck!
------------------------------------------------------------
On 2025/12/19 the temperature will be 47 degrees fahrenheit
ADVISORY: Its cold as fuuuck!
------------------------------------------------------------
On 2025/12/20 the temperature will be 31 degrees fahrenheit
ADVISORY: The current temperature can cause vulnerability to viral sickness unless your equipped with proper outer layers
------------------------------------------------------------
```

## Contributing

MIT License - feel free to use and modify as needed.
Pull requests are welcome! Open an issue and I'll ASAP.
