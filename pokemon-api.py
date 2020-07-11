import requests
import json

# 1. Make a GET request to https://pokeapi.co/api/v2/pokemon?limit=151
#   This page has the first 151 pokemon
#   Take some time to explore the website
#   Think about how you can get the data
request = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
# 2. Make your response readable
request_json = request.json()
#print(request_json)
# 3. Create an empty list that you will put your data into
data_list = []
#print(request_json)
# 4. Loop through all of the 151 pokemon
for r in request_json["results"]:
    # 5. Get the name of the pokemon
  name = (r["name"])
    # 6. Get the link to the additional info
  URL = (r["url"])
    # 7. Make a GET request to the link
  link = requests.get(URL)
    # 8. Make your response readable
  link_json = link.json()
    # 9. Get the ability of the pokemon
    #    Hint: If you are having trouble finding the
    #          ability, explore the data in your browser.
    #          Trial and error is your friend.
  pokemon_ability = (link_json["abilities"])
  list_of_abilities = []  
  for x in pokemon_ability:
    dict1 = (x["ability"])
    #print(dict1)
    ability = (dict1["name"])
    #print(ability)
    list_of_abilities.append(ability)
  pokemon_dict = {name: list_of_abilities}
    # 10. Append a dictionary to the list with the name
    #     and the ability of the pokemon
  data_list.append(pokemon_dict)
#print(data_list)
# 11. Loop through your list and print the name of the
#     pokemon and their ability
for y in data_list:
  print(y)


