# TODO 1. Create a dictionary in this format:

import pandas
import os

os.system('clear')

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phon_dict = {row.letter: row.code for (index, row) in data.iterrows()}


while True:
    word = input('Enter word: ').upper()
    try:
        output = [phon_dict[letter] for letter in word]
        print(output)
        break
    except KeyError:
        print('Only proper letters please.')


## or teacher version:

# def generate_phonetic():
#     word = input('Enter word: ').upper()
#     try:
#         output = [phon_dict[letter] for letter in word]
#     except KeyError:
#         print('Only proper letters please.')
#         generate_phonetic()
#     else:
#         print(output)

# generate_phonetic()

