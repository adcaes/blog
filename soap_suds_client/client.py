from suds.client import Client


def get_client_from_uri():
    WDSL = 'http://localhost:8080/weather?wsdl'
    return Client(WDSL)


def get_client_from_file():
    WDSL = 'file:///Users/adria/blog/soap_suds_client/weather.wsdl'
    return Client(WDSL)


def get_weather(city, country):
    client = get_client_from_file()

    request_data = client.factory.create('s1:CityWeatherRequest')
    request_data.City = city
    request_data.Country = country

    result = client.service.getCityWeather(request_data)
    return result


def print_weather(city, country, weather):
    msg = "It is {weather} in {city} ({country}) with {temperature} degrees Celcius at {time}."
    data = dict(weather=weather.Weather, city=city, country=country, temperature=weather.Temperature, time=weather.UpdateTime)
    print msg.format(**data)


def main():
    city, country = 'Stockholm', 'Sweden'
    weather = get_weather(city, country)
    print_weather(city, country, weather)


if __name__ == '__main__':
    main()
