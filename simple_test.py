from os import sep, getcwd
from sys import argv
from pathlib import Path

YOUR_TEST_SOURCE = "C:\\Users\\owner\\Desktop\\test"  # replace this to test
argv.append(YOUR_TEST_SOURCE)

from hardlink_dir import __main__
