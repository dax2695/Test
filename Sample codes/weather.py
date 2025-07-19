import requests
import json # Import the json module for parsing JSON responses

def get_weather_data_json(location):
    """
    Fetches weather information from wttr.in in JSON format.
    """
    url = f"https://wttr.in/{location}?format=j1" # Request JSON format
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response.json() # Parse JSON response directly
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

if __name__ == "__main__":
    location = input("Enter the Location: ")
    weather_data = get_weather_data_json(location=location)

    if weather_data:
        # Example of how to access data from the JSON
        current_condition = weather_data['current_condition'][0]
        print(f"Weather for {location.title()}:")
        print(f"  Description: {current_condition['weatherDesc'][0]['value']}")
        print(f"  Temperature: {current_condition['temp_C']}°C")
        print(f"  Feels like: {current_condition['FeelsLikeC']}°C")
        print(f"  Humidity: {current_condition['humidity']}%")
        print(f"  Wind Speed: {current_condition['windspeedKmph']} km/h ({current_condition['winddir16Point']})")

        # You can explore other parts of the weather_data dictionary for forecast etc.
        # print("\nForecast for next 3 days:")
        # for day in weather_data['weather']:
        #     print(f"  Date: {day['date']}")
        #     print(f"    Max Temp: {day['maxtempC']}°C")
        #     print(f"    Min Temp: {day['mintempC']}°C")
        #     print(f"    Condition: {day['hourly'][0]['weatherDesc'][0]['value']}") # Example for first hour
        #     print("-" * 20)
    else:
        print("Could not retrieve weather data.")
