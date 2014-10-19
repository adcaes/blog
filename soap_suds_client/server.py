from flask import Flask
from flaskext.enterprise import Enterprise
from gevent.wsgi import WSGIServer
import datetime

app = Flask(__name__)
enterprise = Enterprise(app)


String = enterprise._sp.String
Float = enterprise._sp.Float
DateTime = enterprise._sp.DateTime


class CityWeatherRequest(enterprise._scls.ClassModel):

    __namespace__ = "CityWeatherRequest"

    City = String
    Country = String


class CityWeatherResponse(enterprise._scls.ClassModel):

    __namespace__ = "CityWeatherResponse"

    UpdateTime = DateTime
    Temperature = Float
    Weather = String


class WeatherService(enterprise.SOAPService):

    __soap_server_address__ = '/weather'

    @enterprise.soap(CityWeatherRequest, _returns=CityWeatherResponse)
    def getCityWeather(self, request):
        weather = CityWeatherResponse(City=request.City, Country=request.Country)
        weather.UpdateTime = datetime.datetime.utcnow()
        weather.Temperature = 25.4
        weather.Weather = 'Sunny'

        return weather


def main():
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()


if __name__ == '__main__':
    main()
