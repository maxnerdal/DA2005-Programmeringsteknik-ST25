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
        expected_message = "Error: Could not load 'test_file.jpg'\n"
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
        expected_message = "Error: Could not load 'some_directory'\n"
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
        expected_message = "Error: Could not load 'restricted_file.jpg'\n"
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
        expected_message = "Error: Could not load 'invalid_image.jpg'\n"
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
        expected_message = "Error: Could not load 'problematic_file.jpg'\n"
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
        expected_message = "Error: Could not load 'some_file.jpg'\n"
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

    def test_render_ascii_image_none_input(self):
        """Test render_ascii_image with None input (first if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        result = ascii_proj.render_ascii_image(None)
        
        # Verify function returns None when img is None
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: No image provided\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_invalid_object(self):
        """Test render_ascii_image with invalid image object (second if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Create a mock object that doesn't have required image attributes
        invalid_img = object()  # Plain object without convert, width, height
        
        result = ascii_proj.render_ascii_image(invalid_img)
        
        # Verify function returns None when img is invalid
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: Invalid image object provided\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_invalid_width_negative(self):
        """Test render_ascii_image with negative width (third if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        img = ascii_proj.load_image(self.temp_filename)
        result = ascii_proj.render_ascii_image(img, width=-10)
        
        # Verify function returns None when width is negative
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: Width must be a positive number\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_invalid_width_zero(self):
        """Test render_ascii_image with zero width (third if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        img = ascii_proj.load_image(self.temp_filename)
        result = ascii_proj.render_ascii_image(img, width=0)
        
        # Verify function returns None when width is zero
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: Width must be a positive number\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_invalid_width_string(self):
        """Test render_ascii_image with string width (third if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        img = ascii_proj.load_image(self.temp_filename)
        result = ascii_proj.render_ascii_image(img, width="fifty")
        
        # Verify function returns None when width is a string
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: Width must be a positive number\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_zero_width_image(self):
        """Test render_ascii_image with image that has zero width (fourth if statement)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Create a mock image object with zero width
        from unittest.mock import Mock
        mock_img = Mock()
        mock_img.convert = Mock()
        mock_img.width = 0
        mock_img.height = 100
        
        result = ascii_proj.render_ascii_image(mock_img)
        
        # Verify function returns None when image width is zero
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Error: Image has zero width\n"
        self.assertEqual(output, expected_message)

    def test_render_ascii_image_successful_execution(self):
        """Test render_ascii_image with valid inputs (try block successful path)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        img = ascii_proj.load_image(self.temp_filename)
        result = ascii_proj.render_ascii_image(img, width=10)
        
        # Verify function returns a string when successful
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertGreater(result.count("\n"), 0)
        
        # Verify no error messages were printed
        output = self.captured_output.getvalue()
        self.assertEqual(output, "")

    @patch('DA2005_Projekt_Ascii.build_ascii_art')
    def test_render_ascii_image_try_block_exception(self, mock_build_ascii):
        """Test render_ascii_image when exception occurs in try block"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Mock build_ascii_art to raise an exception
        mock_build_ascii.side_effect = RuntimeError("Unexpected processing error")
        
        img = ascii_proj.load_image(self.temp_filename)
        result = ascii_proj.render_ascii_image(img, width=10)
        
        # Verify function returns None when exception occurs in try block
        self.assertIsNone(result)
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Unexpected error rendering ASCII image\n"
        self.assertEqual(output, expected_message)

    def test_build_ascii_art_success(self):
        """Test build_ascii_art with valid inputs (success case)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Use a simple 2x2 grayscale image data
        pixels = [0, 128, 255, 64]  # Dark, medium, light, medium-dark
        width, height = 2, 2
        
        result = ascii_proj.build_ascii_art(pixels, width, height)
        
        # Verify function returns a string
        self.assertIsInstance(result, str)
        
        # Verify correct number of newlines (one per row)
        self.assertEqual(result.count("\n"), height)
        
        # Verify result is not empty
        self.assertGreater(len(result), 0)
        
        # Verify no error messages were printed
        output = self.captured_output.getvalue()
        self.assertEqual(output, "")
        
        # Verify the result contains ASCII characters
        ascii_chars = "@%#*+=-:. "
        for char in result:
            if char != "\n":  # Skip newlines
                self.assertIn(char, ascii_chars, f"Unexpected character '{char}' in ASCII art")

    def test_build_ascii_art_edge_cases(self):
        """Test build_ascii_art with edge case inputs"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Test with single pixel
        pixels = [255]  # White pixel
        width, height = 1, 1
        
        result = ascii_proj.build_ascii_art(pixels, width, height)
        
        # Should return a single character plus newline
        self.assertEqual(len(result), 2)  # One character + newline
        self.assertEqual(result.count("\n"), 1)
        
        # Test with extreme values
        pixels = [0, 255]  # Black and white
        width, height = 2, 1
        
        result = ascii_proj.build_ascii_art(pixels, width, height)
        
        # Should contain darkest and lightest characters
        ascii_chars = "@%#*+=-:. "
        self.assertIn(ascii_chars[0], result)  # Darkest (@)
        self.assertIn(ascii_chars[-1], result)  # Lightest (space)

    @patch('builtins.range')
    def test_build_ascii_art_exception_handling(self, mock_range):
        """Test build_ascii_art exception handling when unexpected error occurs"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Mock range to raise an exception
        mock_range.side_effect = RuntimeError("Unexpected range error")
        
        pixels = [0, 128, 255, 64]
        width, height = 2, 2
        
        result = ascii_proj.build_ascii_art(pixels, width, height)
        
        # Verify function returns empty string when exception occurs
        self.assertEqual(result, "")
        
        # Verify the exact error message was printed
        output = self.captured_output.getvalue()
        expected_message = "Unexpected error in build_ascii_art\n"
        self.assertEqual(output, expected_message)

    def test_build_ascii_art_invalid_pixel_access(self):
        """Test build_ascii_art with mismatched pixels and dimensions (causes IndexError)"""
        # Reset captured output for this specific test
        self.captured_output.seek(0)
        self.captured_output.truncate(0)
        
        # Provide too few pixels for the given dimensions
        pixels = [0, 128]  # Only 2 pixels
        width, height = 3, 2  # But expecting 3x2 = 6 pixels
        
        result = ascii_proj.build_ascii_art(pixels, width, height)
        
        # Should return empty string due to IndexError being caught
        self.assertEqual(result, "")
        
        # Verify an error message was printed
        output = self.captured_output.getvalue()
        self.assertIn("Unexpected error in build_ascii_art", output)

