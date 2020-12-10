import json
import requests


class Main:
    def __init__(self):
        city_name = input('Введите название города латиницей: ')
        api_key = 'c8d80bb2d6812039f5871a9eb8bae694'
        response = requests.get('https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'.format(city_name, api_key))
        text = json.loads(response.text)
        self.info = text['list']
        self.temp, self.pres = [], []
        self.sum_temp, self.sum_pres = 0, 0
        self.temperature()
        self.pressure()

    def temperature(self):
        for i in self.info:
            main = i['main']
            self.temp.append(main['feels_like'])
        for i in self.temp:
            self.sum_temp += i
        print('Средняя ощущаемая температура: ' + str(int(self.sum_temp / len(self.temp))))

    def pressure(self):
        for i in self.info:
            main = i['main']
            self.pres.append(main['pressure'])
        print('Минимальное давление: ' + str(min(self.pres)))


if __name__ == '__main__':
    Main()
