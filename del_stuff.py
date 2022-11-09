my_list = [
    "apple", "cheese", "cream", "mayo", "pear", "juice", "noop", "milk"
]

not_in = "ecm"

for letter in not_in:

    for item in my_list.copy():
        if letter in item:
            my_list.remove(item)
            
print(my_list)