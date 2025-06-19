def polynomial_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0
    
    # First collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

"""
2.4.1 Uppgift 1
Antag att polynomen p och q är definierade matematisk som nedan.
p := 2 + x^2
q := -2 + x + x^4
Skriv kod för att lagra listrepresentationen för dessa två polynom i variablerna p och q i Python. Det vill
säga,
p = [...]
q = [...]
där innehållet i listorna ska fyllas i. Testa att du skrivit rätt på följande sätt:
>>> polynomial_to_string(p)
'2 + 0x + 1x^2'
>>> polynomial_to_string(q)
'-2 + 1x + 0x^2 + 0x^3 + 1x^4'

Polynom Python-representation
3x^2 - 2x + 1           --> [1, -2, 3]
x^4                     --> [0, 0, 0, 0, 1]
4x^2 + 5x^3             --> [0, 0, 4, 5]
5 + 4x + 3x2 + 2x3 + x4 --> [5, 4, 3, 2, 1]
"""

def polynomial_to_list(p_string):
    #Convert a polynomial string to a list representation.
    p_string = p_string.replace(' ', '')  # Remove spaces for easier processing
    #3x^2-2x+1 
    
    #variable
    #constant
    #coefficient

    i = 0

    while i < len(p_string):
        if p_string[i].isdigit() and (i == 0 or p_string[i-1] in '+-'):
            
            constant = p_string[i]
        elif p_string[i] == 'x':
            variable = p_string[i]
        elif p_string[i] == '^':
            coefficient = p_string[i]
        
        i += 1

    for letter in p_string:
        if letter.isdigit(): constant = letter
        elif letter == 'x': variable = letter
        elif letter == '^': coefficient = letter

            p_string = p_string.replace(letter, 'x^')
    
# Declare varibles with
p = "2 + x^2"
q = "2 + x + x^4"

# Convert the polynomial strings to list representation
#p = [2, 0, 1]§
#q = [-2, 1, 0, 0, 1]   

print(polynomial_to_list(p))  # Should print: '2 + 0x + 1x^2'
#print(polynomial_to_string(q))  # Should print: '-2 + 1x + 0x^2 + 0x^3 + 1x^4'