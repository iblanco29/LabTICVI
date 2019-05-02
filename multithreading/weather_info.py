import requests
import pandas as pd
import boto3

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

print(final_table)

access_key_id = 'ASIAQ5J57O3OLZ7BDHIL'
secret_access_key = 'ArA4VqYMEYiGSwaj8Jd3brTjdIaHWofO1k21tc2h'

resource = boto3.resource('dynamodb', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name='us-east-1')

table = resource.Table('tabla1')

for data in final_table:
    table.put_item(Item=data)

