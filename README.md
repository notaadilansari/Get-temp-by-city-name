# Get-temp-by-city-name
Weather Fetcher CLI
This is a simple Python script that retrieves the current temperature for any city using the OpenWeatherMap API. It demonstrates basic API interaction, JSON parsing, and the use of the requests library.
🚀 Features
Real-time Data: Fetches live weather information from OpenWeatherMap.
User Input: Allows users to specify any city globally.
Metric Units: Automatically converts and displays temperature in Celsius.

🔍 How it Works
The script follows a straightforward process to bridge the gap between your terminal and the weather server:
Input: Takes a city_name from the user.
Request: Constructs a URL including the city name, your unique API key, and the unit preference (metric).
GET: Sends a GET request to the OpenWeatherMap server.
Parse: Converts the raw JSON response into a Python dictionary.
Output: Extracts the temp value from the main section of the data and prints it.
