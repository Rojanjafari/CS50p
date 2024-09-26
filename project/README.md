# Weather Forecast Announcement
## [Video Demo](https://youtu.be/g3VZQYP8zW4)
## Definition:
This project gives the user the weather condition of the desired city by means of a telegram bot.\
This information includes description of the weather condition, tempreture, feels_like, humidity, wind speed and cloud percentage.\
The program responds to any input language.

The project consists of folowing files:\
`project.py` : includes the project codes\
`test_project.py` : includes test functions\
`reqiurements.txt` : includes required libraries\
`README.md` : includes description of the project

## Required libraries:
1. [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
2. [requests](https://pypi.org/project/requests/)
3. [emoji](https://pypi.org/project/emoji/)

Click on the library name to read more about it.
The required libraries are also mentioned in the `reqiurements.txt` file which can be used to install them by the command below:
>pip install -r requirements.txt

## How the program works:
First of all a telegram bot was created with `@BotFather` and an API TOKEN have been obtained.\
The weather condition of the desired city is obtained from [openweathermap](https://openweathermap.org/api).\
The program contains four additional functions which their operation is described below:
1. The `Geocoding` function, takes the name of the city as input and returns the latitude(lat) and longitude(lon) of the location using a specific API.
The latitude and longitude are used in an API that returns the weather condition.
2. The `API_maker` function takes the latitude(lat) and longitude(lon) of the desired city which are obtianed the `Geocoding` function, place them in the API and returns the complete API.
3. The `weather_info` function takes the API which is provided by the `API_maker` function as input.
Then the weather condition of the desired city is gotten using the function `get` from the `requests` library.
The information are organized as a python dictionary using `json` method. Then the reqiered data is extracted from the dictionary and the texts are provided to return to the user in a list.
4. The `pyTelegramBotAPI` library has a class named `telebot` which provides several ways to listen for incoming messages.
In the `telegram_bot` function, an instance of the telebot class is created using the obtained TOKEN.
Then the incoming commands(start and help) are handled with fuctions which are decorated by a message handler and have only one parameter (the message).
The last handler, handles the incoming messages that are expected to a city name. If the it's not, the bot will notifies the user using `reply_to` method.
Else if the city name is valid, the weather condition, which is obtained using weather_info function, is returned.
At last the command  below will start the bot:
    >bot.infinity_polling()

### Author : Rojan Jafari