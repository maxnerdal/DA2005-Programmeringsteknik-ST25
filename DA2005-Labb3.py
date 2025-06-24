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
    """  """
    word_dict = {} # declare dictionary
    try: # using try to catch eventual errors
        with open(filename, 'r') as infile:
            for i, line in enumerate(infile.readlines()):
                word_list = line.lower().strip().split(' ')
                for word in word_list:
                    if word:
                        if word in word_dict:
                            if i not in word_dict[word]:
                                word_dict[word].append(i)
                        else:
                            word_dict[word] = [i]
                    else:
                        pass
        return word_dict
    except:
        print("Could not open file " + filename + " for reading.")
        return None  # Return None if there was an error

def important_words(an_index, stop_words):
    output_word_list = []       # new list that will hold the important words for the output
    important_words_dict = {}   # new dict that will keep track on the importance of every word 
    count_word_list = []        # new list that only will hold the value for the importance
    # delete stop words
    for key in stop_words:
        if key in an_index:
            del an_index[key]
    
    # itterate through all lists in the dictionary an_index
    for key,value in an_index.items():
        # create a new dictionary that only holds a word as key and a value for the importance
        important_words_dict[key] = len(value)
        # Add to list that only holds a value for the importance
        count_word_list.append(len(value))

    #for key, value in important_words_dict.items(): print(key,value)

    # sort list with our defined functions
    count_word_list = insertion_sort(count_word_list)
    count_word_list.reverse()
    #print(count_word_list)

    new_dict = {} # only for testing

    for i in range(min(5, len(count_word_list))):
       for key, value in important_words_dict.items():
        if value == count_word_list[i]:
            important_value = important_words_dict.pop(key) # only for testing
            new_dict[key] = important_value # only for testing
            output_word_list.append(key)
            break
    
    for key,value in new_dict.items(): print(key,value)
    print(output_word_list)

    return output_word_list

def main():
    print('======== 3.4.1 Uppgift 1 ========')
    print(insert_in_sorted(2, []))                # [2]
    print(insert_in_sorted(5, [0,1,3,4]))         # [0, 1, 3, 4, 5]
    print(insert_in_sorted(2, [0,1,2,3,4]))       # [0, 1, 2, 2, 3, 4]
    print(insert_in_sorted(2, [2,2]))             # [2, 2, 2]
    print(insertion_sort([12,4,3,-1]))            # [-1, 3, 4, 12]
    print(insertion_sort([]))                     # []
    
    print('======== 3.4.2 Uppgift 2 ========')
    file_poem = 'poeem.txt'
    file = number_lines(file_poem)
    #file = 'hej.txt'
    try:
        with open(file, 'r') as f:
            for line in f:
                print(line, end='')
    except: #FileNotFoundError:
        print("Could not open file " + file_poem + " for reading.")
        return None  # Return None if there was an error
    print('')

    print('======== 3.4.3 Uppgift 3 ========')
    file_sommar = 'sommar.txt'
    print(index_text(file_sommar))
    print(index_text(file_poem))

    file_idas = 'idas.txt'
    Stopwords_list = ['och', 'jag', 'som', 'det', 'för']
    index_dict = index_text(file_idas)
    important_words_list = important_words(index_dict, Stopwords_list)
    #for key, value in index_text(file_idas).items(): print(key,value)
    #print(important_words_list)

# Main function to run the program
if __name__ == "__main__":
    main()