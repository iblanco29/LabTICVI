from multiprocessing import Pool, freeze_support
import requests
import pandas as pd
import multiprocessing as mp

cities = pd.read_json("reduced_cities.json")

city_ids = list(cities['id'])
temp = []
humidity = []
api_key = "8a9819d14d8b76825fc6ca3e7dc30a8f"


def prepare_df(city_id):

    url = "https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(city_id, api_key)
    response = requests.get(url).json()
    temp.append(response['main']['temp'])
    humidity.append(response['main']['humidity'])


def main():

    pool = Pool(processes=mp.cpu_count())
    pool.map(prepare_df, city_ids)


if __name__ == "__main__":
    main()
    boolean = True
    while boolean:
        if len(city_ids) == len(temp) and len(city_ids) == len(humidity):
            data_frame = pd.DataFrame({'id': city_ids, 'temp': temp, 'hum': humidity})
            final_table = data_frame.join(cities.set_index('id'), on='id', how='inner')
            print final_table
            boolean = False
