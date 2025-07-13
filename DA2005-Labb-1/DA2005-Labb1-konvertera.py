# DA2005-Labb1-konvertera.py
# Author: Max Nerdal
# Date: 2025-06-17
# AI: Github Copilot integrated to Visual Studio Code
# Kommentarer på svenska: 
# Jag antar att Else längst ner i If-satsen inte är någon avancerad Särfallshantering (exception handling) i den bemärkelsen ni förbjuder.
# Vore ett plus om det finns exempel i listan på ej accepterade tekniker.

"""
Uppgift

1. √ Ladda ned, provkör och studera konvertera.py programmet från kurshemsidan (se mappen “Kod
för laborationer”). Fungerar det som det ska?
2. √ Skriv om funktionen fahrenheit_to_celsius så att den räknar rätt.
3. √ Utöka programmet med en funktion som konverterar från Celsius till Fahrenheit.
4. √ Utöka programmet med funktioner så att det också kan konvertera till och från Kelvin från både
Celsius och Fahrenheit.
5. √ Utöka programmet så att det frågar efter vilken konvertering du vill göra. Exemplet här nedanför
visar hur det bör se ut (ungefär) när man kör sitt program.
6. √ Lämna in din lösning i inlämningsmodulen på kurshemsidan.

√ Ej tillåtna tekniker kontrollerade
"""
# Conversion functions for temperature between Fahrenheit, Celsius och Kelvin
def fahrenheit_to_celsius(temp):
    temp_celsius = (temp - 32) * 5 / 9
    return temp_celsius

def celsius_to_fahrenheit(temp):
    temp_fahrenheit = (temp * 9 / 5) + 32
    return temp_fahrenheit

def celsius_to_kelvin(temp):
    temp_kelvin = temp + 273.15
    return temp_kelvin

def kelvin_to_celsius(temp):
    temp_celsius = temp - 273.15
    return temp_celsius

def fahrenheit_to_kelvin(temp):
    temp_celsius = fahrenheit_to_celsius(temp)
    temp_kelvin = celsius_to_kelvin(temp_celsius)
    return temp_kelvin

def kelvin_to_fahrenheit(temp):
    temp_celsius = kelvin_to_celsius(temp)
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    return temp_fahrenheit

def main():

    # Console output for user interaction
    print("Välj konvertering:")
    print("1. Fahrenheit till Celsius")
    print("2. Celsius till Fahrenheit")
    print("3. Celsius till Kelvin")
    print("4. Kelvin till Celsius")
    print("5. Fahrenheit till Kelvin")
    print("6. Kelvin till Fahrenheit")
    val = input("Mata in en siffra 1-6 för den konvertering du vill göra: ")

    # Wich conversion fuction to execute based on user input
    if val == "1":
        temp = float(input("Ange temperatur i Fahrenheit (0.00): "))
        print("Celsius:", fahrenheit_to_celsius(temp))
    elif val == "2":
        temp = float(input("Ange temperatur i Celsius (0.00): "))
        print("Fahrenheit:", celsius_to_fahrenheit(temp))
    elif val == "3":
        temp = float(input("Ange temperatur i Celsius (0.00): "))
        print("Kelvin:", celsius_to_kelvin(temp))
    elif val == "4":
        temp = float(input("Ange temperatur i Kelvin (0.00): "))
        print("Celsius:", kelvin_to_celsius(temp))
    elif val == "5":
        temp = float(input("Ange temperatur i Fahrenheit (0.00): "))
        print("Kelvin:", fahrenheit_to_kelvin(temp))
    elif val == "6":
        temp = float(input("Ange temperatur i Kelvin (0.00): "))
        print("Fahrenheit:", kelvin_to_fahrenheit(temp))
    else:
        print("Ogiltigt val.")

# Main function to run the program
if __name__ == "__main__":
    main()