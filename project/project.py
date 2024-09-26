import telebot
import requests
import emoji

def main():
    telegram_bot()

    
def Geocoding(name):
    API_city_name = f'http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid=51f859e5cb40c6a93228c23fb9a2d878'
    response = requests.get(API_city_name)
    if response.status_code == 200:
        data = response.json()
        data = data[0]
        lat = data['lat']
        lon = data['lon']
    else:
        lat = 'Invalid'
        lon = 'Invalid'

    return lat, lon


def API_maker(lat, lon):
    if lat != 'Invalid' and lon != 'Invalid':
        api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=51f859e5cb40c6a93228c23fb9a2d878&units=metric'
    else:
        api = 'Invalid'
    return api    


def weather_info(api):
    if api != 'Invalid':
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            
            weather = data['weather']
            weather = weather[0]
            main = data['main']

            description = weather['description']
            description = emoji.emojize(f':scroll: Description: {description}', language='alias')

            temp = main['temp']
            temp = emoji.emojize(f':thermometer: Tempreture: {temp} Celsius', language='alias')

            feels = main['feels_like']
            feels = emoji.emojize(f':hot_face::cold_face: Feels like: {feels} Celsius', language='alias')

            humidity = main['humidity']
            humidity = emoji.emojize(f':fog: Humidity: {humidity}%', language='alias')

            wind = data['wind']['speed']
            wind = emoji.emojize(f':wind_face: Wind speed: {wind} meter/sec', language='alias')

            clouds = data['clouds']['all']
            clouds = emoji.emojize(f':cloud: Clouds: {clouds}%', language='alias')
        
            weather_param = [description, temp, feels, humidity, wind, clouds]

            weather_result = ''
            for i in weather_param:
                weather_result += f'{i}\n'

            return weather_result.strip()
        
        else:
            return 'Invalid'

    else:
        return 'Invalid'


def telegram_bot():
    TOKEN = '' # Add your telegram bot TOKEN here
    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to Weather Data Bot")
        
    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, 'Send the name of any city to get it\'s current weather condition')

    @bot.message_handler(func=lambda m: True)	
    def show_weather(message):
        city = message.text.lower()
        lat, lon = Geocoding(city)
        api = API_maker(lat, lon)
        weather_result = weather_info(api)

        if weather_result == 'Invalid':
            bot.reply_to(message, 'City not found, Please try again')

        else:
            bot.reply_to(message, weather_result)

    bot.infinity_polling()
        

if __name__ == "__main__":
    main()
