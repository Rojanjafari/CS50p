from project import Geocoding, API_maker, weather_info

def test_Geocoding():
    assert Geocoding('tehran') == (35.6892523, 51.3896004)

def test_API_maker():
    assert API_maker(35.6892523, 51.3896004) == 'https://api.openweathermap.org/data/2.5/weather?lat=35.6892523&lon=51.3896004&appid=51f859e5cb40c6a93228c23fb9a2d878&units=metric'

def test_weather_info():
    assert weather_info('https://api.openweathermap.org/data/2.5/weather?lat=35.6892523&lon=51.3896004&appid=51f859e5cb40c6a93228c23fb9a2d878&units=metric') == '📜 Description: broken clouds\n🌡️ Tempreture: 32.73 Celsius\n🥵🥶 Feels like: 31.19 Celsius\n🌫️ Humidity: 26%\n🌬️ Wind speed: 6.17 meter/sec\n☁️ Clouds: 75%'