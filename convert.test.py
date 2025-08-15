import os
import unittest
import tempfile
import shutil

from convert import list_mp3_files, get_duration

class TestConvertFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing.
        self.test_dir = tempfile.mkdtemp()
        # Create a dummy MP3 file.
        self.mp3_file = os.path.join(self.test_dir, 'test1.mp3')
        with open(self.mp3_file, 'w') as f:
            f.write("dummy content")
        # Create a non-MP3 file.
        self.txt_file = os.path.join(self.test_dir, 'notes.txt')
        with open(self.txt_file, 'w') as f:
            f.write("just some text")
    
    def tearDown(self):
        # Remove the temporary directory.
        shutil.rmtree(self.test_dir)
    
    def test_list_mp3_files(self):
        # Only files ending with .mp3 should be returned.
        files = list_mp3_files(self.test_dir)
        self.assertIn('test1.mp3', files)
        self.assertNotIn('notes.txt', files)
    
    def test_get_duration_invalid_mp3(self):
        # The dummy file is not a valid MP3, so get_duration should return "00:00".
        duration = get_duration(self.mp3_file)
        self.assertEqual(duration, "00:00")
    
    def test_list_mp3_files_nonexistent_directory(self):
        # Passing a non-existing directory should return an empty list.
        files = list_mp3_files("non_existing_directory")
        self.assertEqual(files, [])

if __name__ == '__main__':
    unittest.main()