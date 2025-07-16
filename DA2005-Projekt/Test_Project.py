import unittest
import os
import tempfile
from PIL import Image
import DA2005_Projekt_Ascii as ascii_proj

class TestAsciiArtProject(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary test image that all tests can use"""
        # Use 'with' but with delete=False to keep the file
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            test_img = Image.new('RGB', (50, 30), color='blue')
            test_img.save(tmp.name)
            self.temp_filename = tmp.name
        # File handle closed automatically, but file remains on disk
    
    def tearDown(self):
        """Delete the temporary test image"""
        if os.path.exists(self.temp_filename):
            os.unlink(self.temp_filename)

    def test_load_image_success(self):
        """Test that load_image successfully loads an existing image file"""
        img = ascii_proj.load_image(self.temp_filename)
        self.assertIsNotNone(img, "load_image should return an image object for a valid file")
        self.assertIsInstance(img, Image.Image)
    
    def test_load_image_nonexistent_file(self):
        """Test that load_image handles missing files gracefully"""
        img = ascii_proj.load_image("nonexistent_file.jpg")
        self.assertIsNone(img, "load_image should return None for missing files")

    def test_load_image_invalid_file_format(self):
        """Test that load_image handles invalid file formats gracefully"""
        # Create a temporary file with wrong content (not an image)
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False, mode='w') as tmp:
            tmp.write("This is not an image file, just text content!")
            invalid_filename = tmp.name
        try:
            # Try to load the invalid "image" file
            result = ascii_proj.load_image(invalid_filename)
            self.assertIsNone(result, "load_image should return None for invalid image files")
        finally:
            # Clean up the invalid test file
            os.unlink(invalid_filename)

    def test_load_image_directory_error(self):
        """Test that load_image handles directory instead of file gracefully"""
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Try to load a directory as if it were an image file
            result = ascii_proj.load_image(temp_dir)
            self.assertIsNone(result, "load_image should return None when given a directory")

    def test_load_image_permission_error(self):
        """Test that load_image handles permission errors gracefully"""
        import stat
        # Create a temporary file and remove read permissions
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            test_img = Image.new('RGB', (10, 10), color='red')
            test_img.save(tmp.name)
            restricted_filename = tmp.name
        
        try:
            # Remove read permissions (chmod 000)
            os.chmod(restricted_filename, 0o000)
            
            # Try to load the file without read permissions
            result = ascii_proj.load_image(restricted_filename)
            self.assertIsNone(result, "load_image should return None for files without read permission")
        finally:
            # Restore permissions so we can delete the file
            os.chmod(restricted_filename, 0o644)
            os.unlink(restricted_filename)

    def test_build_ascii_art(self):
        # Use a fake 2x2 grayscale image data
        pixels = [0, 128, 255, 64]
        width, height = 2, 2
        ascii_art = ascii_proj.build_ascii_art(pixels, width, height)
        self.assertIsInstance(ascii_art, str)
        self.assertEqual(ascii_art.count("\n"), height)

    def test_render_ascii_image(self):
        """Test that render_ascii_image produces ASCII art from an image"""
        img = ascii_proj.load_image(self.temp_filename)
        ascii_art = ascii_proj.render_ascii_image(img, width=10)
        self.assertIsInstance(ascii_art, str)
        self.assertGreater(ascii_art.count("\n"), 0)

    def test_info(self):
        """Test that info() function doesn't crash"""
        img = ascii_proj.load_image(self.temp_filename)
        try:
            ascii_proj.info(img, self.temp_filename)
        except Exception as e:
            self.fail(f"info() raised an exception: {e}")

