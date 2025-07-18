from PIL import Image
import unittest

try:
    from Test_Project import TestAsciiArtProject
except ImportError:
    TestAsciiArtProject = None

def load_image(filename):
    try:
        return Image.open(filename)
    except:
        print(f"Error: Could not load '{filename}'")
        return None

def build_ascii_art(pixels, width, height):
    """Build the ASCII art string from pixel data."""
    try:
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
        return ascii_str
    except Exception as e:
        print(f"Unexpected error in build_ascii_art")
        return ""

def render_ascii_image(img, width=50):
    """Render the loaded image as ASCII art."""
    # Input validation with if statements
    if img is None:
        print("Error: No image provided")
        return None
    
    if not hasattr(img, 'convert') or not hasattr(img, 'width') or not hasattr(img, 'height'):
        print("Error: Invalid image object provided")
        return None
    
    if not isinstance(width, (int, float)) or width <= 0:
        print("Error: Width must be a positive number")
        return None
    
    if img.width == 0:
        print("Error: Image has zero width")
        return None
    
    try:
        # PIL operations that could still fail in unexpected ways
        gray_img = img.convert("L") # Convert to grayscale
        aspect_ratio = gray_img.height / gray_img.width # Calculates how tall the image is compared to its width.
        new_height = int(aspect_ratio * width) # Calculates height with correct ratio
        new_height = int(new_height * 0.55) # Adjust height for font aspect ratio
        resized_img = gray_img.resize((width, new_height)) # Resize the image to the new dimensions
        pixels = resized_img.getdata() # Get pixel values as a flat list
        art_str = build_ascii_art(pixels, width, new_height) # Call function build_ascii_art()
        return art_str
    except Exception as e:
        print(f"Unexpected error rendering ASCII image")
        return None

def info(img, filename=None):
    """Print information about the loaded image."""
    if img is None or not hasattr(img, 'size'):
        print("No image loaded")
    elif not hasattr(img.size, '__getitem__') or len(img.size) < 2:
        print("Invalid image object - missing size information")
    else:
        try:
            print(f"Filename: {filename if filename else 'Unknown'}")
            print(f"Size: {img.size[0]}x{img.size[1]}")
        except (IndexError, TypeError) as e:
            print(f"Error accessing image size: {e}")

def prompt_for_image():
    """Prompt the user for an image filename and load the image."""
    while True:
        try:
            filename = input("Input filename: ")
            img = load_image(filename) # call load_image function to load the image
            # Exception handling is done in load_image function
            if img:
                print(f"Image '{filename}' loaded successfully.")
                return img, filename
            else:
                print("Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None, None
        except EOFError:
            print("\nEnd of input reached.")
            return None, None
        except Exception as e:
            print(f"Unexpected error during input: {e}")
            print("Please try again.")

def run_tests():
    """Run the unit tests for the ASCII art project."""
    if TestAsciiArtProject is not None:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestAsciiArtProject)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        print("Test class not found. Make sure test_DA2005_Projekt_Ascii.py is available.")

def main():
    """Main function to run the ASCII Art Studio."""
    try:
        # Start by running the tests
        print("\nStarting tests...\n")
        run_tests()
        print("\nTests complete. Starting ASCII Art Studio...\n")

        # Console output for user interaction
        print("Welcome to ASCII Art Studio!\n")
        print("1. Load image")
        print("2. Render ASCII art")
        print("3. Show image info")
        print("4. Show menu")
        print("5. Quit\n")

        # Initialize variables
        action_input = ""
        filename = ""
        img = None
        
        # Which conversion function to execute based on user input
        while True:
            try:
                action_input = input("Type a number 1-5 according to what you want to do: ")
                if action_input == "1": # call prompt_for_image function to load the image
                    result = prompt_for_image()
                    if result[0] is not None:  # Check if image was loaded successfully
                        img, filename = result
                elif action_input == "2": # call render_ascii_image function to render the ASCII art
                    if img is None:
                        print("No image loaded. Please load an image first (option 1).")
                    else:
                        ascii_art = render_ascii_image(img)
                        if ascii_art:
                            print(ascii_art)
                        else:
                            print("Failed to render ASCII art.")
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
                else:
                    print("Invalid option. Please choose 1-5.")
            except KeyboardInterrupt:
                print("\nOperation cancelled. Goodbye!")
                break
            except EOFError:
                print("\nEnd of input reached. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.")
                
    except Exception as e:
        print(f"Fatal error in main program: {e}")
        print("Program will exit.")
    
if __name__ == "__main__":
    main()
