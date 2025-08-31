from django.shortcuts import render
import requests


API_KEY = "97fd2a9d39d37a5cbb880b32dfb18a41"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def index(request):
    weather_data = None
    error = None

    city = request.GET.get('city')

    if city:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
       
    
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            error = "⚠️ Please enter a correct city name."

    return render(request, "index.html", {"weather": weather_data, "error": error})
