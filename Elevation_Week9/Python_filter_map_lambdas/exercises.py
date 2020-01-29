# import json
# pokemon_data = json.load(open("pokemon.json"))


#exercise 1:


# map_pokemon_data = list(map( lambda a: {"id": a["id"], "name": a["name"], "type": a["type"],
#                "weight": a["weight"], "height": a["height"], "weaknesses": a["weaknesses"]   }, pokemon_data))
#
# print(map_pokemon_data)

# exercise 2

# pokemon_names = list(map(lambda a: a["name"], pokemon_data))
# # print(pokemon_names)

# exercise 3

# heavy_pokemon = list(filter(lambda p: p["weight"] > 100, pokemon_data))
# print(len(heavy_pokemon))

# exercise 4

# name_weak = list(map(lambda x: x["name"], (filter(lambda p: "Water" in p["weaknesses"], pokemon_data))))
# print(name_weak)


