# DA2005-Labb2-polynom.py
# Author: Max Nerdal
# Date: 2025-06-23
# AI: Github Copilot integrated to Visual Studio Code


def split_polynomial(poly_str):
    # Function that splits a polynomial string (input) into a list of multiple strings, one for each term (output)
    # Input example:   '2 + x^2'    Output example:  ['2','x^2']
    terms_list = []
    term = ''
    poly_str = poly_str.replace(' ', '')    # Remove spaces for easier processing
    for i,char in enumerate(poly_str):      # Loop through the full input string with index
        if char in '+-' and i != 0:         # when this statement is true the term is finished
            terms_list.append(term)         # term added to list
            term = char                     # new term is initiated
        else:                               # as long as the above if statement remains untrue the loop keep on adding to the term string. 
            term += char
    terms_list.append(term)
    return terms_list

def polynomial_to_string(p_list):
    # Function that takes a polynomial in list form (input) and returns a polynominal string (output). Provided by the course.
    # Input example:   [-2, 1, 0, 0, 1]     Output example:  '2 + 0x + 1x^2'
    terms = []
    degree = 0
    for coeff in p_list:                                        # itterate through the list
        if coeff == 0:                                          # if the coeff is 0 then skip this term
            pass
        elif degree == 0:                                       # if degree is 0 then this is a constant term
            terms.append(str(coeff))
        elif degree == 1:                                       # if degree is 1 then this is a linear term
            if coeff == 1:                                      # if coeff is 1 then add only 'x' to the list
                terms.append('x')
            elif coeff == -1:                                   # if coeff is -1 then add '-x' to the list
                terms.append('-x')
            else:                                               # if coeff is not 1 or -1 then add coeff + 'x' to the list
                terms.append(str(coeff) + 'x')
        elif degree > 1:                                        # if degree is higher than 1 then this is a polynomial term
            if coeff == 1:                                      # if coeff is 1 then add 'x^' + degree to the list
                terms.append('x^' + str(degree))
            elif coeff == -1:                                   # if coeff is -1 then add '-x^' + degree to the list
                terms.append('-x^' + str(degree))
            else:                                               # if coeff is not 1 or -1 then add coeff + 'x^' + degree to the list
                terms.append(str(coeff) + 'x^' + str(degree))
        degree += 1
    final_string = ' + '.join(terms)                            # The string ' + ' is used as "glue" between the elements in the string
    if final_string.strip() == '': 
        final_string = '0'                                      # If the final string is empty then return '0'
    return final_string


def polynomial_to_list(terms_list):
    # Function that takes a polynomial as a list of term strings and returns a polynomial in list form.
    # Input example:    ['2','x^2'])    Output example:   [2, 0, 1])
    # Declaring objects
    poly_dict = {}
    poly_list = []
    coefficient = 0
    degree = 0
    varible = False
    i = 0
    
    for term in terms_list:                 # start a for loop to itterate through all terms in the input list
        # Assigning objects for each itteration of the for loop
        i = 0
        coefficient = 0
        degree = 0
        varible = False  
        
        while i < len(term):                                        # For each term in terms_list itterate through all letters 
                                                                    # Code is not handling a coefficient that is bigger than one didgit.
            if term[i].isdigit() and (i == 0 or term[i-1] in '+-'): #coefficient is always found first in each term or after + or -
                if term[i-1] == '-':                                # if previous caracter is minus then add minus to the coefficient
                    coefficient = -int(term[i])
                else:
                    coefficient = term[i]
            elif term[i] == 'x':
                degree = 1                                          # If there is a higher degree found this is going to be overwritten.
                if coefficient == 0: coefficient = 1                # If coefficient isn't assign then a single x is coefficient 1
            
                                                                    # Code is not handling a degree that is bigger than one didgit.
            elif term[i] == '^':                                    # If '^' then the next char is set as degree
                degree = term[i+1]
            else:
                pass
            i += 1
        
        # Assign dictionary with degree as key and coefficient as value
        poly_dict[int(degree)] = int(coefficient)
    
    #Create a list from dictionary
    i=0                                     # set counter to 0 for new itteration
    while i <= max(poly_dict.keys()):       # itterate from 0 to the highest key in dict
        if i in poly_dict.keys():           # if the key is in dict then append that coeff 
            poly_list.append(poly_dict[i])
        else:
            poly_list.append(0)             # else append 0
        i += 1
    return poly_list


def drop_zeroes(p_list):
    # Function that takes a polynomial in list form (input) and returns a polynomial in list form without zeros in the end (output)
    # Input example:   [2,0,1,0]    Output example:  [2,0,1]
    new_list = p_list
    while new_list and new_list[-1] == 0:
        new_list.pop(-1)
    return new_list


def eq_poly(p_list,q_list):
    # Function that takes 2 polynomial in list form (input) and returns True/False (output)
    # Input example:   [2,0,1], [2,0,1]    Output example:  True
    return drop_zeroes(p_list) == drop_zeroes(q_list)

def eval_poly(p,x):
    # Function that takes 1 polynomial in list form and a value for x (input) and returns the value for that x position (output)
    # Input example:   [-2, 1, 0, 0, 1], -2     Output example:  12
    output = 0
    for i, coeff in enumerate(p):       # itterate through the list with index
        if i == 0: 
            output = coeff              # only the first instance in list that shouldn't get multipied with degree.
        else: 
            output += coeff * x ** i    # algorithm to calculate this polynomial in list form
    return output


def neg_poly(p_list):
    # Function that takes 1 polynomial in list form and and returns the same list negated (output)
    # Input example:   [-2, 1, 0, 0, 1]    Output example:  [2, -1, 0, 0, -1]
    negated_list = []
    for coeff in p_list:            # itterate through the list 
        negated_list.append(-coeff) # append the negated coeff to the new list
    return negated_list


def add_poly(p_list, q_list):
    # Function that takes 2 polynomial in list form and returns a list where these are added together (output)
    # Input example:   [1, 2, 3], [4, 3, 2]     Output example:  [5, 5, 5]
    new_list = []
    max_len = max(len(p_list), len(q_list)) #makes sure that the itteration follows the longest list.
    for i in range(max_len):
        p = p_list[i] if i < len(p_list) else 0 # if the list is shorter then the itteration set 0
        q = q_list[i] if i < len(q_list) else 0 # if the list is shorter then the itteration set 0
        new_list.append(p + q)
    return new_list 


def sub_poly(p_list,q_list):
    # Function that takes 2 polynomial in list form and returns a list where the second are subtracted from the first (output)
    # Input example:   p1 = [1, 2, 3], p2 = [4, 3, 2]   Output example:  [-3, -1, 1]
    return  add_poly(p_list,neg_poly(q_list)) # adding p_list with the negated q_list


# In this Function we do all of our initial function calls
def main():
    #2.4.1 Uppgift 1 √
    print('======== 2.4.1 Uppgift 1 ========')
    p_str = "2 + x^2"
    q_str = "-2 + x + x^4"
    p = polynomial_to_list(split_polynomial(p_str))
    q = polynomial_to_list(split_polynomial(q_str))
    print(f'p as mathematic string: {polynomial_to_string(p)}')
    print(f'p as polynomial list: {p}')
    print(f'q as mathematic string: {polynomial_to_string(q)}')
    print(f'q as polynomial list: {q}')

    #2.4.2 Uppgift 2 √
    print('======== 2.4.2 Uppgift 2 ========')
    p0 = [2,0,1,0]
    q0 = [0,0,0]
    print('=============== a ===============')
    print(f'p0: {p0} dropped zeros: {drop_zeroes(p0)} ')
    print(f'p0: {q0} dropped zeros: {drop_zeroes(q0)} ')
    print('=============== b ===============')
    print(f'is {p} equal to {p0}? {eq_poly(p,p0)} ')
    print(f'is {q} equal to {p0}? {eq_poly(q,p0)} ')
    print(f'is {q0} equal to {[]}? {eq_poly(q0,[])} ')

    #2.4.3 Uppgift 3 √
    print('======== 2.4.3 Uppgift 3 ========')
    print(f'value when list:p x:0 = {eval_poly(p,0)}')
    print(f'value when list:p x:1 = {eval_poly(p,1)}')
    print(f'value when list:p x:2 = {eval_poly(p,2)}')
    print(f'value when list:q x:2 = {eval_poly(q,2)}')
    print(f'value when list:q x:-2 = {eval_poly(q,-2)}')

    #2.4.4 Uppgift 4 √
    print('======== 2.4.4 Uppgift 4 ========')
    p1 = [1, 2, 3]
    p2 = [4, 3, 2]
    p3 = [1, 1, 1, 1, 1]
    p4 = [-1, -1, -1, -1, -1]
    print('=============== a ===============')
    print (f'p1: {p1} p2: {p2} p3: {p3}')
    print(f'makes list: {p1} negative: {neg_poly(p1)}')
    print('=============== b ===============')
    print(f'adds list: {p1} and {p2}: {add_poly(p1,p2)}')
    print(f'adds list: {p1} and {p3}: {add_poly(p1,p3)}')
    print(f'adds list: {p3} and {p1}: {add_poly(p3,p1)}')
    print('=============== c ===============')
    print(f'subtract list {p1} with {p2}: {sub_poly(p1,p2)}')
    print(f'subtract list {p3} with {p4}: {sub_poly(p3,p4)}')
    print('============ tester =============')
    print(f'test, p + q = q + p: {eq_poly(add_poly(p,q),add_poly(q,p))}')
    print(f'test, p - p = 0: {eq_poly(sub_poly(p,p),[])}')
    print(f'test, p - (- q) = p + q: {eq_poly(sub_poly(p,neg_poly(q)),add_poly(p,q))}')
    print(f'test, p + p != 0: { not eq_poly(add_poly(p,p),[])}')
    print(f'test, p - q = 4-x+x^2-x^4: {eq_poly(sub_poly(p,q),[4, -1, 1, 0, -1])}')
    print(f'test, [23,1,4]+[1,1,1] = [24,2,5]: {eq_poly(add_poly([23,1,4],[1,1,1]),[24,2,5])}')
    print(f'test conversion, "23 + x^2" = [23,0,1]: {eq_poly(polynomial_to_list(split_polynomial("23 + x^2")),[23,0,1])}')

    #2.4.5 Uppgift 5 √
    print('======== 2.4.5 Uppgift 5 ========')
    print(f'polynomial_to_string(p): {polynomial_to_string(p)}')
    print(f'polynomial_to_string(q): {polynomial_to_string(q)}')
    print(f'polynomial_to_string([]): {polynomial_to_string([])}')
    print(f'polynomial_to_string([0,0,0]): {polynomial_to_string([0,0,0])}')
    print(f'polynomial_to_string([1,2,3]): {polynomial_to_string([1,2,3])}')
    print(f'polynomial_to_string([-1, 2, -3]): {polynomial_to_string([-1, 2, -3])}')
    print(f'polynomial_to_string([1,1,-1]): {polynomial_to_string([1,1,-1])}')

# Main function to run the program
if __name__ == "__main__":
    main()