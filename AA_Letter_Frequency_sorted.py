import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import matplotlib

def count_all(user_string):
    ignore_letters = [",", " ", "'", "[", "]"]
    all_letters = {}

    to_ignore = input("Which letters should be excluded? ")
    for item in to_ignore:
        ignore_letters.append(item)

    for letter in user_string:

        # add letter to dictionary if it does not exist

        # ignore commas, speech marks and spaces
        if letter in ignore_letters:
            continue

        elif letter not in all_letters:
            all_letters[letter] = 1

        # increase number of letters
        else:
            all_letters[letter] = all_letters.get(letter, 0) + 1

    return all_letters


word = input("Enter a word / sentence: ")

word_dict = count_all(word)

# Convert dictionary to lists based on keys and values
word_letters = list(word_dict.keys())
word_numbers = list(word_dict.values())

frequency_dict = {
    "letters": word_letters,
    "frequency": word_numbers
}

df = pd.DataFrame(frequency_dict)

frequency_sorted = df.sort_values('frequency', ascending=False)

plt.bar('letters', 'frequency', data=frequency_sorted, color='orange')
plt.show()