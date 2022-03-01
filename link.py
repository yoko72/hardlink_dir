from os import link
from pathlib import Path
from logging import getLogger

logger = getLogger(__name__)
depth_of_start_path = None

def make_links(source: Path, destination: Path, exists_ok=True, is_recursive=True):
    global depth_of_start_path
    if depth_of_start_path is None:
        depth_of_start_path = len(source.parents)
    destination_dir = (destination / source.name)
    destination_dir.mkdir(exist_ok=exists_ok)
    for child in source.iterdir():
        if child.is_dir():
            if is_recursive:
                make_links(child, destination_dir)
        elif child.is_file():
            destination_file = destination_dir / child.name
            child_dir = destination_file.parents[depth_of_start_path:][0]
            try:
                link(str(child), destination_file)
            except FileExistsError as e:
                if not exists_ok:
                    raise e
                else:
                    logger.warn(f"Skipped {child_dir / destination_file.name} since file with same name already exists.")
            else:
                logger.info(f"Hardlink: {child_dir / destination_file.name} is successfully created.")
