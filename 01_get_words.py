# empty list to read list from a file
all_words = []
must_have = []

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

# display list
while True:
    
    not_in = input("What letters are NOT in the word? ").lower()
    
    # remove letters that are not in the word
    for letter in not_in:

        for item in all_words.copy():
            if letter in item:
                all_words.remove(item)
                
    # remove letters that are in the wrong place (yellow)
    yellow = input("What letters are in the wrong place?  eg: T---E means the T and E are in the word but in the wrong place.  Press <enter> if you don't have any yellow letters")
    
    green = input("Which letters are in the right place. eg: T---- means the T is in the right place Press <enter> if you don't have any green letters.  ")
    
    # only execute this code if we have yellow letters!
    if yellow != "":
        
        # get indices
        yellow_indices = []

        yellow_index = 0
        for letter in yellow:
            
            yellow_row = []
            if letter != "-":
                
                # add to must have list!
                must_have.append(letter)
                
                # add to index row
                yellow_row.append(yellow_index)
                yellow_row.append(letter)
                
                # add entry to indices
                yellow_indices.append(yellow_row)
            
            yellow_index += 1   

        # Remove words with letters in the wrong place                        
        count = 0
        for i in yellow_indices:
            yellow_row = i[0]
            yellow_letter = i[1]
            
            for item in all_words.copy():
                # remove items in wrong place
                if item[yellow_row] == yellow_letter:
                    all_words.remove(item)
                    
                # also remove word if it does not include 'must have' letters
                else:
                    for letter in must_have:
                        if letter not in item:
                            
                            # sometimes it tries to remove a word that is not in the list anymore.  In that case we want to just keep going instead of crashing.
                            try:
                                all_words.remove(item)  
                            except ValueError:
                                pass      
                
        print(all_words)
    
    # remove words which don't have letters in the right place (green)    
    
    keep_going = input("Do you need to put in another word? Yes / No ").lower()           
    if keep_going == "no":
        break       
        
        
print(all_words)
print("Intial list: ", initial_length)
print("Final length: ", len(all_words))