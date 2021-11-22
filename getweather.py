# importing requests and json
import requests, json, math, datetime
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name
CITY = "bangalore"
# API key
API_KEY = "2d076255db659af3c6d3bc562c9a4d15"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
# HTTP request
response = requests.get(URL)
# print(response.status_code)

# checking the status code of the request
if response.status_code == 200:
   data = response.json()
   print(data)
   main = data['main']
   temperature = main['temp']
   feels_like = main['feels_like']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   temp_max = round((float(main['temp_max']) - 273.15), 3)
   print("Temp max K: ", main['temp_max'])
   print("Temp min K: ", main['temp_min'])
   print("Temperature in degC: {:.2f}°C".format(round((temperature-273.15), 2)))
   print(f"Feels like : {feels_like}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
   print("Date: ", datetime.datetime.fromtimestamp(data["dt"]).date())
   print("Sunrise: ", datetime.datetime.fromtimestamp((data['sys'])['sunrise']).time())
   print("Sunset: ", datetime.datetime.fromtimestamp((data['sys'])['sunset']).time())
   print("cloud percentage: "+ str(data['clouds']['all'])+ "%")
   print("timezone: ", datetime.datetime.utcfromtimestamp(data['timezone']).time())
else:
   # showing the error message
   print("Error in the HTTP request")
