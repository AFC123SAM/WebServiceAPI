import urllib.parse, requests


def main():
    print('Country Code (UK/US/FR/DE/etc.)')
    country = input('(If Unknown enter any 3 digits): ')  # ASKS USER TO INPUT COUNTRY
    location = input('Location: ')  # ASKS USER TO INPUT LOCATION
    weather_api_1 = 'http://api.openweathermap.org/data/2.5/weather?'  # 1st PART OF THE API URL
    weather_api_2 = '&appid=d34a8345d4e8a9ab70ee7f36fcef491f'  # 2nd PART OF THE API URL
    url = weather_api_1 + urllib.parse.urlencode({'q': location}) + "," + country + weather_api_2  # URL BUILDER

    # print("URL: " + url)
    print("╔═════════════════╦══════════════════")
    json_data = requests.get(url).json()  # WEATHER URL REQUEST

    json_name = json_data['name']  # LOCATION NAME
    json_coord_lon = str(json_data['coord']['lon'])  # LOCATION LONGITUDE FROM 1st API
    json_coord_lat = str(json_data['coord']['lat'])  # LOCATION LATITUDE FROM 1st API

    # print("Latitude: " + json_coord_lat)
    # print("Longitude: " + json_coord_lon)

    timestamp_url = "http://api.geonames.org/timezoneJSON?lat="  # 1st PART OF THE API URL
    timestamp_url_u = "&username=afc123sam"  # 2nd PART OF THE API URL
    url3 = str(timestamp_url + json_coord_lat + "&lng=" + json_coord_lon + timestamp_url_u)  # URL BUILDER
    json_data3 = requests.get(url3).json()  # CALLS THE API

    json_country = (json_data3['countryName'])  # FINDS COUNTRY NAME OUT OF JSON LIST
    print('║        Location ║ ' + json_name + ", " + json_country)  # PRINTS LOCATION NAME AND COUNTRY
    json_local_time = (json_data3['time'])  # FINDS TIME OUT OF JSON LIST
    print("║ Local Date/Time ║ " + json_local_time)  # PRINTS TIME

    json_sunrise = (json_data3['sunrise'])  # FINDS SUNRISE TIME FROM JSON LIST
    print("║         Sunrise ║ " + json_sunrise)  # PRINTS SUNRISE TIME
    json_sunset = (json_data3['sunset'])  # FINDS SUNSET TIME FROM JSON LIST
    print("║          Sunset ║ " + json_sunset)  # PRINTS SUNRISE TIME

    temp_k = float(json_data['main']['temp'])  # FINDS TEMPERATURE FROM JSON LIST
    temp_c = round(temp_k - 273.15)  # CALCULATES KELVINS INTO CELSIUS
    print(str('║     Temperature ║ ') + str(temp_c) + str("°C"))  # PRINTS TEMPERATURE

    json_weather_calc = json_data['weather'][0]['description']  # FINDS WEATHER DESCRIPTION FROM JSON LIST
    json_current_weather = json_weather_calc.title()
    print("║         Weather ║ " + json_current_weather)  # PRINTS WEATHER

    json_humidity = json_data['main']['humidity']  # FINDS HUMIDITY FROM JSON LIST
    print('║        Humidity ║ ' + str(json_humidity) + '%')  # PRINTS HUMIDITY

    uv_url = 'http://api.openweathermap.org/data/2.5/uvi?'  # 1st PART OF THE API URL
    url2 = str(uv_url + "&lat=" + json_coord_lat + "&lon=" + json_coord_lon + weather_api_2)  # URL BUILDER
    json_data2 = requests.get(url2).json()  # CALLS THE API

    uv_index = (json_data2['value'])  # FINDS UV INDEX FROM JSON LIST
    print("║        UV Index ║ " + str(uv_index))  # PRINTS UV INDEX FROM JSON LIST

    if uv_index < 2.9:  # CALCULATES THE UV INDEX AND SHOW WHAT IT...
        print("║         UV Risk ║ Low")  # ...MEANS IN REALITY
    elif uv_index < 5.9:
        print("║         UV Risk ║ Moderate")
    elif uv_index < 7.9:
        print("║         UV Risk ║ High")
    elif uv_index < 10.9:
        print("║         UV Risk ║ Very High")
    else:
        print("║         UV Risk ║ Extreme")

    print("╚═════════════════╩══════════════════")
    exit_app = input("Exit Application?(Y/N): ")
    print("═════════════════════════════════════")
    if exit_app.lower() == "y":
        exit()
    else:
        main()


main()
