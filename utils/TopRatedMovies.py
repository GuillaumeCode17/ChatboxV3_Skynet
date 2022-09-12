import requests
import json

# url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
# headers = {
#     "X-RapidAPI-Key": "90c0054ba0msh2ab56bfa58a6e3dp183099jsn0815b0115688",
#     "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
# }

url = "https://netflix-weekly-top-10.p.rapidapi.com/api/movie"
headers = {
	"X-RapidAPI-Key": "90c0054ba0msh2ab56bfa58a6e3dp183099jsn0815b0115688",
	"X-RapidAPI-Host": "netflix-weekly-top-10.p.rapidapi.com"
}

try:
    List_of_Movies = open("utils\AllMoviesCodes.json", 'r')
    Data = json.load(List_of_Movies)
except:
    Data = requests.request("GET", url, headers=headers)
    with open('./utils/AllMoviesCodes.json', 'w', encoding="utf-8") as f:
        f.write(str(Data.text))



