from os import getcwd
from pathlib import Path
from argparse import ArgumentParser
from logging import getLogger, INFO

from . import make_links

logger = getLogger(__name__)
logger.setLevel(INFO)

parser = ArgumentParser(description="Makes hard-links for all files of the specified directory to current directory.")
parser.add_argument("path", help="Path of original sources.")
parser.add_argument("-r", "--no-recursive", action="store_true",
                    help="Hard-links to the objects of child dir in default. Stop it if this is given.")
parser.add_argument("--stops_if_exists", action="store_true", default=False,
                    help="Raise exception if same name object exists.")
parsed_args = parser.parse_args()
sources_path = Path(parsed_args.path)
destination_path = Path(getcwd())

is_recursive = not parsed_args.no_recursive
exists_ok = not parsed_args.stops_if_exists
make_links(sources_path, destination_path, exists_ok=exists_ok, is_recursive=is_recursive)
