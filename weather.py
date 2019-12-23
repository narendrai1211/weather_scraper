import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
weather_page_url = 'https://weather.com/en-IN/weather/today/l/18.49,73.93?par=google&temp=c'
weather_url = requests.get(weather_page_url)
if weather_url.status_code == 200:
    weather_text = weather_url.text
    soup = BeautifulSoup(weather_text, 'lxml')


def get_today_weather():
    list_day = []
    list_behavior = []
    list_temp = []
    looking_ahead = soup.find_all('div', class_='looking-ahead')
    tomorow_weather = soup.find_all('div', class_='today-daypart-top')
    for i in tomorow_weather:
        day = i.find('span', class_='today-daypart-title').text
        behavior = i.find('span', class_='today-daypart-wxphrase').text
        list_day.append(day)
        list_behavior.append(behavior)
    print(list_day)
    print(list_behavior)
    for i in looking_ahead:
        temprature_str = i.find_all('div', class_='today-daypart-temp')
        for j in temprature_str:
            degree_c = j.find('span').text
            list_temp.append(degree_c.split('°')[0])
    print(list_temp)
    return list_day, list_behavior, list_temp


int_temp_list = []


def plot_weather(list_day_x, list_temp_y):
    for i in list_temp_y:
        int_temp_list.append(int(i))
    plt.plot(list_day_x, int_temp_list)
    plt.show()
    plt.close()


list_day_each, list_behave_each, list_temp_each = get_today_weather()
plot_weather(list_day_each, list_temp_each)
