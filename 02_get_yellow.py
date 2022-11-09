yellow = input("What letters are in the wrong place?  eg: T---E means the T and E are in the word but in the wrong place.  Press <enter> if you don't have any yellow letter, ").lower()

yellow_indices = []

yellow_index = 0
for letter in yellow:
    
    yellow_row = []
    if letter != "-":
        
        yellow_row.append(yellow_index)
        yellow_row.append(letter)
        
        # add entry to indices
        yellow_indices.append(yellow_row)
    
    yellow_index += 1   

    
print(yellow_indices)