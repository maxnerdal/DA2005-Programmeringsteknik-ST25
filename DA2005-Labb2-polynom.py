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
'2 + 0x + 1xˆ2'
>>> polynomial_to_string(q)
'-2 + 1x + 0xˆ2 + 0xˆ3 + 1xˆ4'
"""