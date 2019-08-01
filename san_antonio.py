# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_item_in(my_list):
  # get a random number
  item = my_list[1]
  return item

# user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

# while user_answer != "B":
  # print(get_random_item_in(quotes))
  # user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


for character in characters:
    p_character = character.capitalize()
    print(p_character)

for quote in quotes:
    p_quote = quote.capitalize()
    print(p_quote)

pass

