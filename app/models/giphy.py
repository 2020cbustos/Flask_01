import json, requests

def api_call(meme):
    #get api key
    api_key = '0y6HdJ4xRYkLog45YMsiYfX4CF1XyYi6'
    url = 'https://api.giphy.com/v1/gifs/search?api_key='+api_key+'&q='+meme+'&limit=25&offset=3&rating=PG-13&lang=en'
    print(url)
    data = requests.get(url).json()
    data = data["data"]
    return data
