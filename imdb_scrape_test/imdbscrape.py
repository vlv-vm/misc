import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

def main():
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, "html.parser")
    movietags = soup.select("td.titleColumn")
    
    inner_movietags = soup.select("td.titleColumn a")
    
    movie_dict = {"names":[],"people":[],"years":[]}
    
    for i in range (len(movietags)):
        movie_dict["names"].append(inner_movietags[i].string)
        movie_dict["people"].append(inner_movietags[i]["title"])
        movie_dict["years"].append(movietags[i].span.string)
    
    for i in range (len(movie_dict["names"])):
        title = movie_dict["names"][i]
        people = movie_dict["people"][i]
        years = movie_dict["years"][i]
        print(f"*************************\n{i+1}. Title: {title} | People: {people} | Year: {years}\n")

    rand = random.randrange(0,len(movie_dict["names"]))
    title = movie_dict["names"][rand]
    people = movie_dict["people"][rand]
    years = movie_dict["years"][rand]
    print(f"*************************\n[Random Choice] Title: {title} | People: {people} | Year: {years}\n")
    
if __name__ == "__main__":
    try:
        main()
    except:
        print("Error")
