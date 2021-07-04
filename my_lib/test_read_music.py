import unittest
import read_music
from io import StringIO
import sys
import os
import signal

class ReadMusicTest(unittest.TestCase):
    def test_change_path(self):
        """
        Change the directory in the system terminal
        """
        sys.stdin = StringIO('music\n')
        read_music.change_path()
        current_directory = os.system('ls')
        self.assertEqual(current_directory, "Potato.html  css  index.html  js  music  music.html  my_lib  temp.html")

    def test_read_from_file(self):
        """
        read from a file_name
        """
        read_music.read_from_file("aha-take_on_me.html")