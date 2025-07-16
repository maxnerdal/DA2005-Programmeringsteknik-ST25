import unittest
import os
import tempfile
import io
import sys
from PIL import Image
from unittest.mock import patch
import DA2005_Projekt_Ascii as ascii_proj

class TestAsciiArtProject(unittest.TestCase):
    

    def setUp(self):
        """Create a temporary test image and setup stdout capture"""
        
        # Create temporary test image
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            test_img = Image.new('RGB', (50, 30), color='blue')
            test_img.save(tmp.name)
            self.temp_filename = tmp.name
        
        # Setup stdout capture for testing print statements
        self.captured_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output

    
    def tearDown(self):
        """Delete the temporary test image and restore stdout"""
       
        # Delete temporary test image
        if os.path.exists(self.temp_filename):
            os.unlink(self.temp_filename)

        # Restore stdout first
        sys.stdout = self.original_stdout


    def test_load_image_success(self):
        """Test that load_image successfully loads an existing image file"""
        img = ascii_proj.load_image(self.temp_filename)
        self.assertIsNotNone(img, "load_image should return an image object for a valid file")
        self.assertIsInstance(img, Image.Image)

    
    @patch('PIL.Image.open')
    def test_load_image_file_not_found_exception(self, mock_open):
        """Test that load_image properly handles FileNotFoundError - returns None and prints correct message"""
        # Mock Image.open to raise FileNotFoundError
        mock_open.side_effect = FileNotFoundError("No such file or directory")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("test_file.jpg")
        
        # Verify the function returns None when FileNotFoundError occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("test_file.jpg")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: File 'test_file.jpg' not found.\n"
        self.assertEqual(output, expected_message)


    @patch('PIL.Image.open')
    def test_load_image_is_directory_error_exception(self, mock_open):
        """Test that load_image properly handles IsADirectoryError - returns None and prints correct message"""
        # Mock Image.open to raise IsADirectoryError
        mock_open.side_effect = IsADirectoryError("Is a directory")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("some_directory")
        
        # Verify the function returns None when IsADirectoryError occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("some_directory")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: 'some_directory' is a directory, not a file.\n"
        self.assertEqual(output, expected_message)


    @patch('PIL.Image.open')
    def test_load_image_permission_error_exception(self, mock_open):
        """Test that load_image properly handles PermissionError - returns None and prints correct message"""
        # Mock Image.open to raise PermissionError
        mock_open.side_effect = PermissionError("Permission denied")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("restricted_file.jpg")
        
        # Verify the function returns None when PermissionError occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("restricted_file.jpg")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: No permission to read 'restricted_file.jpg'.\n"
        self.assertEqual(output, expected_message)


    @patch('PIL.Image.open')
    def test_load_image_unidentified_image_error_exception(self, mock_open):
        """Test that load_image properly handles UnidentifiedImageError - returns None and prints correct message"""
        # Mock Image.open to raise UnidentifiedImageError
        mock_open.side_effect = Image.UnidentifiedImageError("cannot identify image file")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("invalid_image.jpg")
        
        # Verify the function returns None when UnidentifiedImageError occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("invalid_image.jpg")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: 'invalid_image.jpg' is not a valid image file or has an unsupported format.\n"
        self.assertEqual(output, expected_message)


    @patch('PIL.Image.open')
    def test_load_image_os_error_exception(self, mock_open):
        """Test that load_image properly handles OSError - returns None and prints correct message"""
        # Mock Image.open to raise OSError
        mock_open.side_effect = OSError("OS level error")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("problematic_file.jpg")
        
        # Verify the function returns None when OSError occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("problematic_file.jpg")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: 'problematic_file.jpg' is not a valid image file or has an unsupported format.\n"
        self.assertEqual(output, expected_message)


    @patch('PIL.Image.open')
    def test_load_image_generic_exception(self, mock_open):
        """Test that load_image properly handles generic Exception - returns None and prints correct message"""
        # Mock Image.open to raise a generic exception
        mock_open.side_effect = ValueError("Unexpected error occurred")
        
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.load_image("some_file.jpg")
        
        # Verify the function returns None when generic Exception occurs
        self.assertIsNone(result)
        
        # Verify Image.open was called with the correct filename
        mock_open.assert_called_once_with("some_file.jpg")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error loading image 'some_file.jpg': Unexpected error occurred\n"
        self.assertEqual(output, expected_message)



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

