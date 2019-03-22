import requests
import re
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_city_code():
    name = input('输入要查询的天气地点:')
    url = 'http://toy1.weather.com.cn/search?cityname={}'.format(name)
    res = requests.get(url,headers=headers)
    data = res.text.strip('()[]')
    code = re.findall('{"ref":"(.*?)~',data,re.S)[0]
    return code

def get_weather():
    code = get_city_code()
    url = 'http://t.weather.sojson.com/api/weather/city/{}'.format(code)
    res = requests.get(url,headers=headers)
    json_data = json.loads(res.text)
    cityInfo = json_data.get('cityInfo')
    wdata = json_data.get('data')
    data = {
        '地点':cityInfo.get('city'),
        '湿度':wdata.get('shidu'),
        '空气质量':wdata.get('quality'),
        '温度':wdata.get('wendu'),
        '温馨提示':wdata.get('ganmao')
    }
    print(data)
    forecast =wdata.get('forecast')
    for i in range(0,15):
        print(forecast[i])


if __name__ == '__main__':
    get_weather()




