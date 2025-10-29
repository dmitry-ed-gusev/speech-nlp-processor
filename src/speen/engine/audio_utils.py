
from loguru import logger
from pydub import AudioSegment

# m4a_file = './audio/58-5-3 часть.m4a'
# m4a_file = './audio/Острогоржское_Каротоякское_21_5_9_4_вср_часть_4.m4a'
# wav_filename = './output/output-4.wav'


def m4a_2_wav(m4a_infile: str, wav_outfile: str) -> None:
    logger.debug(f"Converting {m4a_infile} -> {wav_outfile}")

    # sound = AudioSegment.from_file(m4a_infile, format='m4a').
    # file_handle = sound.export(wav_outfile, format='wav')
    AudioSegment.from_file(m4a_infile, format='m4a').export(wav_outfile, format='wav')
