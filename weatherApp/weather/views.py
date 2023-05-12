

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=77da2ce15a3de0c53796b242ac436e10'

    city = 'Las Vegas'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    # city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    cities = City.objects.all() #return all the cities in the database
    print(cities)
    weather_data = []
    count=0
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        count=count+1
        if(count>4):
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }

            weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data,'form':form}
    


   

    return render(request,'index.html',context)#returns the index.html template
