import requests
import json

url = "https://netflix-weekly-top-10.p.rapidapi.com/api/movie"
headers = {
    "X-RapidAPI-Key": "90c0054ba0msh2ab56bfa58a6e3dp183099jsn0815b0115688",
    "X-RapidAPI-Host": "netflix-weekly-top-10.p.rapidapi.com"
}


All_Movies = []

try:
    data = open('./utils/AllTopMovies.json', 'r')
    All_Movies = json.load(data)
except:
    with open('./utils/AllTopMovies.json', 'a+', encoding="utf-8") as f:
        response = requests.request("GET", url, headers=headers)
        All_info_Movies = json.loads(response.text)
        for i in All_info_Movies:
            Number = i["list"]
            Name = i["name"]
            Views = i["hoursviewed"]
            All_Movies.append({"List": Number, "Name": Name, "Views": Views})
        f.write(str(All_Movies))


