
import requests
wea_url = 'https://weather.cma.cn/api/now/58238'

def weather_get():
    data = requests.get(url = wea_url).json()
    city = str(data['data']['location']['name'])
    temper = str(data['data']['now']['temperature']) + '°C'
    presure = str(data['data']['now']['pressure']) + 'Pa'
    hum = str(data['data']['now']['humidity']) + '%'
    winddir = str(data['data']['now']['windDirection'])
    winddgr = str(data['data']['now']['windDirectionDegree']) + '度'
    windspeed = str(data['data']['now']['windSpeed']) + 'm/s'
    windlevel = str(data['data']['now']['windScale'])
    time = str(data['data']['lastUpdate'])
    wea_result = ('城市: %s\n气温: %s\n气压: %s\n湿度: %s\n风向: %s\n风向角: %s\n风速: %s\n风力: %s\n时间: %s'%(city,temper,presure,hum,winddir,winddgr,windspeed,windlevel,time))
    return wea_result

final = weather_get()
