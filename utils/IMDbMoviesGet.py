from time import sleep
import requests
import json
from utils.TopRatedMovies import Data

url = "https://imdb8.p.rapidapi.com/title/get-meta-data"

All_Codes = []
All_info_Movies = {}
All_Movies = []

headers = {
    "X-RapidAPI-Key": "90c0054ba0msh2ab56bfa58a6e3dp183099jsn0815b0115688",
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

for i in Data:
    keys, values = zip(*i.items())
    single_value = values[0]
    List_s = single_value.split("/")
    Final_code = List_s[2]
    All_Codes.append(str(Final_code))


for code in All_Codes:
    with open('./utils/AllTopMovies.json', 'a+', encoding="utf-8") as f:
        querystring = {"ids": f"{code}", "region": "US"}
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        All_info_Movies = json.loads(response.text)
        for key in All_info_Movies.keys():
            Movie = All_info_Movies[key]['title']['title']
            All_Movies.append(Movie)
