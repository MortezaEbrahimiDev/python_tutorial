# imports and variables
from abc import ABC, abstractmethod
import requests
# abstract class

class WeatherAbstract(ABC):
    @abstractmethod
    def get_current_wheather(self,lat, long):
        pass

# openweather class
class OpenWeatherProvider(WeatherAbstract):
    def __init__(self,api_key):
        self.api_key=api_key
    def get_current_wheather(self, lat, long):
        return

# openmeteo class
class OpenmeteoProvider(WeatherAbstract):
    base_url="https://api.open-meteo.com/v1/forecast"#?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m
    def get_current_wheather(self, lat, long):
        params={
            "latitude":lat,
            "longitude":long,
            "hourly":"temperature_2m",
            "current":"temperature_2m"
        }
        response=requests.get(self.base_url,params)
        return response.json()


# run app

provider=OpenmeteoProvider()
print(provider.get_current_wheather(52.52,13.41))
