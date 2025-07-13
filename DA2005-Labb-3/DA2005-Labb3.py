# DA2005-Labb3.py
# Author: Max Nerdal
# Date: 2025-06-24
# AI: Github Copilot integrated to Visual Studio Code

def insert_in_sorted(x,sorted_list):
    """ inserts x into sorted_list and returns sorted_list """
    i=0 # declare counter
    if not sorted_list: # if list is empty
        sorted_list.append(x) # insert at the end of the list
    elif x >= max(sorted_list): # if x is bigger or equal than the max value in list
        sorted_list.append(x) # insert at the end of the list
    else: # if x is in the range of list values
        while i < len(sorted_list.copy()): # itterate through the list with an index
            if x < sorted_list[i]:  # when x is smaller then curent index value  
                sorted_list.insert(i,x) # insert x at that index
                break # exit while loop
            i+=1 # add to index
    return sorted_list

def insertion_sort(my_list):
    """ sorts my_list and returns a new sorted list """
    out = [] # declare new list out
    for x in my_list: # itterate through list
        out = insert_in_sorted(x, out) # each itteration call on insert_in_sorted with x and list out and return a sorted list
    return out

def number_lines(f):
    """ creates a copy of the input file with all rows numbered """
    try: # using try to catch eventual errors
        with open(f, 'r') as infile, open('numbered_' + f, 'w') as outfile: # open infile and outfile
            for i, line in enumerate(infile.readlines()): # read infile
                outfile.write(f"{i} {line}") # write in outfile
        return 'numbered_' + f  # Only return filename if successful
    except:
        print("Could not open file " + f + " for reading.")
        return None  # Return None if there was an error

def index_text(filename):
    """ creates an index of the words in the text file and returns a dictionary with words as keys and line numbers as values """
    word_dict = {} # declare dictionary
    try: # using try to catch eventual errors
        with open(filename, 'r') as infile: # open file for reading
            for i, line in enumerate(infile.readlines()):   # read file line by line
                word_list = line.lower().strip().split(' ') # split each line into words, lower case and remove leading/trailing spaces
                for word in word_list:  # itterate through each word in the line
                    if word:    # if word is not empty
                        if word in word_dict:   # if word is already in the dictionary
                            if i not in word_dict[word]:    # check if the line number is already in the list
                                word_dict[word].append(i)   # if not, append the line number to the list
                        else:
                            word_dict[word] = [i]   # if word is not in the dictionary, create a new entry with the line number as a list   
                    else:
                        pass    # if word is empty, do nothing
        return word_dict    # Return the dictionary if successful
    except: # If there is an error, print a message and return None
        print("Could not open file " + filename + " for reading.")
        return None  # Return None if there was an error

def important_words(an_index, stop_words):
    """ takes a dictionary created from function index_text(filename) and a list of stop words and returns a list of the most important words in the text, excluding the stop words """
    if not an_index:  # If the index is empty, return an empty list
        return []

    output_word_list = [] # new list that will hold the important words for the output
    important_words_dict = {} # new dict that will keep track on the importance of every word
    count_word_list = [] # new list that only will hold the value for the importance
    
    for key in stop_words: # delete stop words in the dictionary an_index
        if key in an_index:
            del an_index[key]
    
    for key,value in an_index.items(): # itterate through keys and lists in dictionary an_index
        important_words_dict[key] = len(value) # add the key and the length of the list as value to the new dictionary important_words_dict
        count_word_list.append(len(value)) # Add to list that only holds values for the importance

    count_word_list = insertion_sort(count_word_list)  # sort list with our defined functions
    count_word_list.reverse() # reverse the list so the most important words are first
    
    new_dict = {} # only for testing

    for i in range(min(5, len(count_word_list))): # itterate through the first 5 values in the sorted list
       for key, value in important_words_dict.items(): # itterate through the keys and values in the dictionary important_words_dict
        if value == count_word_list[i]: # if the value in the dictionary is equal to the value in the sorted list
            important_value = important_words_dict.pop(key) # remove the key from the dictionary and save the value
            new_dict[key] = important_value # add the key and value to the new dictionary
            output_word_list.append(key) # add the key to the output list
            break
    
    #for key,value in new_dict.items(): print(key,value)

    return output_word_list

def main():
    print('\n')
    print('======== 3.4.1 Uppgift 1 ========')
    print('\n')
    print(insert_in_sorted(2, []))                # [2]
    print(insert_in_sorted(5, [0,1,3,4]))         # [0, 1, 3, 4, 5]
    print(insert_in_sorted(2, [0,1,2,3,4]))       # [0, 1, 2, 2, 3, 4]
    print(insert_in_sorted(2, [2,2]))             # [2, 2, 2]
    print(insertion_sort([12,4,3,-1]))            # [-1, 3, 4, 12]
    print(insertion_sort([]))                     # []
    print('\n')

    print('======== 3.4.2 Uppgift 2 ========')
    print('\n')
    file_poem = 'poem.txt'
    file = number_lines(file_poem)
    #file = 'hej.txt'
    try:
        with open(file, 'r') as f:
            for line in f:
                print(line, end='')
    except: #FileNotFoundError:
        print("Could not open file " + file_poem + " for reading.")
        return None  # Return None if there was an error
    print('\n')

    print('======== 3.4.3 Uppgift 3 ========')
    print('\n')
    file_sommar = 'sommar.txt'
    print("{")
    for key, value in index_text(file_sommar).items(): print(f"    '{key}': {value},")
    print("}")
    print('\n')
    file_idas = 'idas.txt'
    Stopwords_list = ['och', 'jag', 'som', 'det', 'för']
    index_dict = index_text(file_idas)
    important_words_list = important_words(index_dict, Stopwords_list)
    print(important_words_list)
    print('\n')

# Main function to run the program
if __name__ == "__main__":
    main()