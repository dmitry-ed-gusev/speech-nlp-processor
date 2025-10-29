import os

from loguru import logger


def list_files_by_ext(directory_path, extension):
    """
    Lists files in a given directory with a specific extension.
    """

    logger.debug(f"Searching in {directory_path} for files with the extension {extension}.")

    files_with_extension: list[str] = []

    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(extension) and os.path.isfile(os.path.join(directory_path, filename)):
                files_with_extension.append(filename)
    except FileNotFoundError:
        logger.error(f"Error: Directory not found at {directory_path}!")

    logger.debug(f"Found in {directory_path} files:\n{"\n".join(files_with_extension)}")

    return files_with_extension
