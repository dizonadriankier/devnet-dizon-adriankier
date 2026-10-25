
import requests
import random

pokemon_list = [
    "mewtwo",
    "rayquaza",
    "arceus",
    "giratina",
    "lugia"
]

answer = random.choice(pokemon_list)
url = f"https://pokeapi.co/api/v2/pokemon/{answer}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        abilities = []
        for item in data["abilities"]:
            abilities.append(item["ability"]["name"])

        print("=== WHO'S THAT POKEMON? ===")
        print("Guess the Pokemon!")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Abilities: {', '.join(abilities)}")
        print("You have 3 attempts.")

        for attempt in range(3):
            guess = input("Enter Pokemon name: ").strip().lower()

            if guess not in pokemon_list:
                print("Invalid Pokemon name! Try again.")
                continue

            if guess == name:
                print("Correct! You guessed the Pokemon!")
                break
            else:
                print("Wrong guess! Try again.")
        else:
            print(f"Game over! The Pokemon was {name.title()}.")

    else:
        print("Could not get Pokemon data. Try again later.")

except requests.exceptions.RequestException:
    print("Network error! Check your internet connection.")
