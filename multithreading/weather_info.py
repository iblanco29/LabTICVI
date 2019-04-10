import requests
import pandas as pd

cities = pd.read_json("reduced_cities.json")

response = []
city_id = []
temp = []
humidity = []
api_key = "8a9819d14d8b76825fc6ca3e7dc30a8f"

for index, i in enumerate(cities['id']):
    url = "https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(i, api_key)
    response.append(requests.get(url).json())
    city_id.append(i)
    temp.append(response[index]['main']['temp'])
    humidity.append(response[index]['main']['humidity'])

data_frame = pd.DataFrame({'id': city_id, 'temp': temp, 'hum': humidity})

final_table = data_frame.join(cities.set_index('id'), on='id', how='inner')

print final_table
