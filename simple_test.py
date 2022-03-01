from os import sep, getcwd
from sys import argv
from pathlib import Path

print(getcwd())
argv.append("C:\\Users\\owner\\Desktop\\test")

from hardlink_dir import __main__
