# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality and then prints out the
# corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API
# documentation. You must register for the service to receive the API key required for making API requests. Furthermore,
# find out how you can convert Kelvin degrees into Celsius.
#key=0ed541848a79ebc81ee98bea04f8942b

import requests
nameCity=input("Enter name of city:")

request =f"http://api.openweathermap.org/data/2.5/weather?q={nameCity} &APPID=eff5e9c47b8263be7ff04d2e7f7b8105"
response =requests.get(request).json()

kelvin= response["main"]["temp"]

celsius= kelvin - 273.15
print(f" temperture in{nameCity} is {celsius}degrees")