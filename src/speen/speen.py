"""
    Main (entry) file for the SPEEN processor.

    Created:  Dmitrii Gusev, 28.10.2025
    Modified: Dmitrii Gusev, 28.10.2025
"""

from loguru import logger

from engine.utils import list_files_by_ext
from engine.audio_utils import m4a_2_wav
from engine.speech_2_text import s2t_process

# some useful defaults
# -- input folders
DEFAULT_INPUT_FOLDER = "./audio/"
DEFAULT_INPUT_EXTENSION = ".m4a"  # input format/file extension
# -- output folders
DEFAULT_OUTPUT_FOLDER = "./output/"
DEFAULT_OUTPUT_EXTENSION = ".wav"  # output format/file extension
# -- voice recognition models
VOICE_SMALL_MODEL_PATH = "./models/vosk-model-small-ru-0.22"  # path to the small speech recognition model
VOICE_BIG_MODEL_PATH = "./models/vosk-model-ru-0.42"  # path to the big speech recognition model


# -- starting the SPEEN processor
logger.info("Starting the SPEEN processor...")
logger.debug(f"Using voice recognition model: {VOICE_BIG_MODEL_PATH}")

# -- 1. Search for all input files
input_files_list: list[str] = list_files_by_ext(DEFAULT_INPUT_FOLDER, DEFAULT_INPUT_EXTENSION)
# logger.info(f"Found input files:\n{"\n".join(input_files_list)}")
logger.info("Found all input files.")

# -- 2. Convert all found files m4a -> wav
for input_file in input_files_list:
    # logger.debug(f"Converting file {input_file} -> {input_file + DEFAULT_OUTPUT_EXTENSION}.")
    m4a_2_wav(DEFAULT_INPUT_FOLDER + input_file,
              DEFAULT_OUTPUT_FOLDER + input_file + DEFAULT_OUTPUT_EXTENSION)
logger.info("Input files were converted to the WAV format.")

# -- 3. Process audio files speech -> text and write to files
result: str = ""
for input_file in input_files_list:
    result = s2t_process(DEFAULT_OUTPUT_FOLDER + input_file + DEFAULT_OUTPUT_EXTENSION,
                         VOICE_BIG_MODEL_PATH)
    # write recognized content to a file
    with open(DEFAULT_OUTPUT_FOLDER + input_file + ".txt", "w", encoding="utf-8") as f:
        f.write(result)
logger.info("Processed all input files: speech -> text.")

logger.info("SPEEN processor done.")
