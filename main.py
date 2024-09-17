from dotenv import load_dotenv
import os
import requests
load_dotenv()
API_KEY = os.getenv("API_KEY")

FILM_LIST_PATH = 'http://api.themoviedb.org/3/discover/movie'
CREDITS_LIST_PATH = 'http://api.themoviedb.org/3/movie'
RELEASE_DATE = "2016-01-01"

def get_film_list(actor_id):
    params = {"api_key": API_KEY, "with_people": actor_id,
              "primary_release_date.gte": RELEASE_DATE}
    r = requests.get(url = FILM_LIST_PATH, params = params)
    data = r.json()
    return data

def data_to_set(data):
    film_set = set()
    for res in data['results']:
        film_set.add(res['title'])
    return film_set

def main():
    print("\nHow to find an actor's id on 'https://www.themoviedb.org/':\n")
    print("1. Go to the link and click on the search bar in the middle of the page. Then, search any actor.\n")
    print("2. Click on the actor of your choice.\n")
    print("3. click on the URL at the top of the page, but do NOT modify it.\n")
    print("4. Find the string of numbers infront of the actor's name.\n   (not including the hyphen '-' or forward slash '/')\n")
    print("5. The numbers are the actor's ID\n   (for example: Ryan Reynold's ID is 10859)\n")

    id1 = input("What is the first ID you'd like to compare?: ")
    id2 = input("What is the second ID you'd like to compare?: ")
    print()

    id1_data = get_film_list(id1)
    id2_data = get_film_list(id2)
    id1_films = data_to_set(id1_data)
    id2_films = data_to_set(id2_data)

    common = set(id1_films & id2_films)
    print("Movies in common: \n", common)
    
    if not common:
        print("No current films in common.")

if __name__ == '__main__':
    main()