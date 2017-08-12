import coordinates
import requests
import datetime

def get_weather():
    #if coordinates.get_coordinates() in coordinates:
    lat,lng=(coordinates.get_coordinates())
    
    api_key="e0a60102f41a97b05ea6fe58b5b5fbd0"
    
    host="https://api.darksky.net/forecast/"
    
    url=host+api_key+"/"+str(lat)+","+str(lng)
    
    response=requests.get(url)
    
    utc_time=(response.json()["currently"]["time"])
    current_time=datetime.datetime.fromtimestamp(utc_time)
    print("Current Time: ",current_time)
    
    weather_summary=response.json()["currently"]["summary"]
    print("Current Weather: ",weather_summary)
    
    current_temp=response.json()["currently"]["temperature"]
    print("Current Temperature: ",current_temp)
    
    future_hourly=response.json()["hourly"]["data"]
    print("Hourly future updates")
    for i in future_hourly:
        time=datetime.datetime.fromtimestamp(i['time'])
        summary=i['summary']
        print("{0} : {1}".format(str(time),summary))
