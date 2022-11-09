# puts words in text file into sorted list
def get_all_words():
    
    all_words = []
    # open file and read the content in a list

    # words from https://github.com/tabatkins/wordle-list
    with open(r'words.txt', 'r') as word_list:
        for line in word_list:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            all_words.append(x)
            
    initial_length = len(all_words)

    all_words.sort()
    return all_words
    

# iterate through string and find index and letter 
# returns list of the index and letter for yellow / green letters
def get_indices(color):
    # get indices
        indices_list = []

        color_index = 0
        for letter in color:
            
            color_row = []
            if letter != "-":
                
                # add to must have list!
                must_have.append(letter)
                
                # add to index row
                color_row.append(color_index)
                color_row.append(letter)
                
                # add entry to indices
                indices_list.append(color_row)
            
            color_index += 1   
        
        return indices_list


def yellow_green_remover(color, color_index_list):
    
    # Remove words with letters in the wrong place                        
    for i in color_index_list:
        color_row = i[0]
        color_letter = i[1]
        
        for item in all_words.copy():
            # remove words where yellow letters in wrong place
            if color == "yellow" and item[color_row] == color_letter:
                all_words.remove(item)
            
            # remove words which don't have green letters in correct place
            elif color == "green" and item[color_row] != color_letter: 
                all_words.remove(item)
                
    return None

# **** Main Routine Goes Here ****

while True:
    
    # empty list to read list from a file
    must_have = []

    # get words from list...
    all_words = get_all_words()
    initial_length = len(all_words)

    # display list
    while True:
        
        not_in = input("What letters are NOT in the word? ").lower()
        
        # remove letters that are not in the word
        for letter in not_in:

            for item in all_words.copy():
                if letter in item:
                    all_words.remove(item)
                    
        # remove letters that are in the wrong place (yellow)
        yellow = input("What letters are in the wrong place?  eg: T---E means the T and E are in the word but in the wrong place.  Press <enter> if you don't have any yellow letters. ")
        
        green = input("Which letters are in the right place. eg: T---- means the T is in the right place Press <enter> if you don't have any green letters.  ")
        
        # only execute this code if we have yellow letters!
        if yellow != "":        
            # get index / letter for yellow letters
            yellow_indices = get_indices(yellow)
            
            # remove words that have yellow letters in wrong place
            yellow_green_remover("yellow", yellow_indices)
            
        if green != "":
            green_indices = get_indices(green)
            
            # remove words that don't have green letter in right place
            yellow_green_remover("green", green_indices)
        
        # remove words which don't contain yellow letters
        for item in all_words.copy():    
            for letter in must_have:
                if letter not in item:
                    
                    # sometimes it tries to remove a word that is not in the list anymore.  In that case we want to just keep going instead of crashing.
                    try:
                        all_words.remove(item)  
                    except ValueError:
                        pass  
        

        
        if len(all_words) == 0:
            print("Oops there are no words to display.  This is possibly due to you putting in conflicting data?")
        else:
            print(all_words)
        print("Intial list: ", initial_length)
        print("Final length: ", len(all_words))
        
        if len(all_words) == 0:
            break
            
        keep_going = input("Press <enter> to keep going or any key to move to the next wordle / quit")           
        if keep_going != "":
            break       
        
    new_word = input("Press <enter> to solve a new wordle or any key to quit")
    if new_word != "":
        break
            
print("We are done!")