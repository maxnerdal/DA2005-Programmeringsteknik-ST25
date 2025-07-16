from PIL import Image

class Ascii_image:
    def __init__(self, filename=None):
        self.filename = filename
        #self.width = None
        #self.height = None
        #self.pixels = None  # 2D list or similar

    def load(self):
        # Load image, handle errors, set width, height, pixels
        try:
            with Image.open(self.filename) as img:
                img.load()
                #self.width, self.height = img.size
                #self.pixels = [img.getpixel((x, y)) for y in range(self.height) for x in range(self.width)]
        except Exception as e:
            print(f"Error loading image: {e}")

    def render(self):
        # Print ASCII art (width 50, keep proportions)
        pass

    def info(self):
        # Print filename and size, or "No image loaded"
        pass