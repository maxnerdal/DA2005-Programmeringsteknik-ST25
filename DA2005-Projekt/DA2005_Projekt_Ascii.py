# DA2005_Projekt_Ascii.py
from PIL import Image
import sys
import unittest

# Try to import test class
try:
    from Test_Project import TestAsciiArtProject  # Import the class from file
except ImportError as e:
    print(f"ImportError while importing Test_Project: {e}")
    TestAsciiArt = None

def load_image(filename):
    """Load an image from the given filename."""
    try:
        img = Image.open(filename)
        img.load()
        # Return the loaded image
        return img
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except (Image.UnidentifiedImageError, OSError):
        print(f"Error: '{filename}' is not a valid image file or has an unsupported format.")
    except Exception as e:
        print(f"Error loading image '{filename}': {e}")
    # Return None if loading fails
    return None

def build_ascii_art(pixels, width, height):
    """Build the ASCII art string from pixel data."""
    ascii_chars = "@%#*+=-:. " # ASCII characters from dark to light
    ascii_str = ""
    for y in range(height):
        row = ""
        for x in range(width):
            # list pixels is a flat list of pixel values (0-255).
            # y * width gives the index of the first pixel in row y.
            # x finds the pixel within that row.
            pixel = pixels[y * width + x]
            char = ascii_chars[pixel * (len(ascii_chars) - 1) // 255]
            row += char
        # Add the finished row to the ASCII art string, with a newline
        ascii_str += row + "\n"
    return (ascii_str)

def render_ascii_image(img, width=50):
    """Render the loaded image as ASCII art."""
    gray_img = img.convert("L") # Convert to grayscale
    aspect_ratio = gray_img.height / gray_img.width # Calculates how tall the image is compared to its width.
    new_height = int(aspect_ratio * width) # Calculates height with correct ratio
    new_height = int(new_height * 0.55) # Adjust height for font aspect ratio
    resized_img = gray_img.resize((width, new_height)) # Resize the image to the new dimensions
    pixels = resized_img.getdata() # Get pixel values as a flat list
    art_str = build_ascii_art(pixels, width, new_height) # Call function build_ascii_art()
    return art_str

def info(img, filename=None):
    """Print information about the loaded image."""
    if img is None or not hasattr(img, 'size'):
        print("No image loaded")
    else:
        print(f"Filename: {filename if filename else 'Unknown'}")
        print(f"Size: {img.size[0]}x{img.size[1]}")

def prompt_for_image():
    """Prompt the user for an image filename and load the image."""
    while True:
        filename = input("Input filename: ")
        img = load_image(filename) # call load_image function to load the image
        # Exception handling is done in load_image function
        if img:
            print(f"Image '{filename}' loaded successfully.")
            return img, filename
        else:
            print("Please try again.")

def run_tests():
    if TestAsciiArtProject is not None:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestAsciiArtProject)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        print("Test class not found. Make sure test_DA2005_Projekt_Ascii.py is available.")

def main():

    print("Starting tests...")
    run_tests()
    print("Tests complete. Starting ASCII Art Studio...")

    # Console output for user interaction
    print("Welcome to ASCII Art Studio!")
    print("1. Load image")
    print("2. Render ASCII art")
    print("3. Show image info")
    print("4. Show menu")
    print("5. Quit")

    # Initialize variables
    action_input = ""
    filename = ""
    # Wich conversion fuction to execute based on user input
    while True:
        action_input = input("Type a number 1-5 according to what you want to do: ")
        if action_input == "1": # call prompt_for_image function to load the image
            img, filename = prompt_for_image()
        elif action_input == "2": # call render_ascii_image function to render the ASCII art
            ascii_art = render_ascii_image(img)
            print(ascii_art)
        elif action_input == "3": # call info function to print image info
            info(img, filename) 
        elif action_input == "4": # Show the menu again
            print("Welcome to ASCII Art Studio!")
            print("1. Load image")
            print("2. Render ASCII art")
            print("3. Show image info")
            print("4. Show menu")
            print("5. Quit")
        elif action_input == "5":
            print("Bye!")
            break
    
if __name__ == "__main__":
    main()
