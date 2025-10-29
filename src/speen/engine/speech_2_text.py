"""
Speech-2-Text Recognizer Module.

Created:  Dmitrii Gusev, 10.08.2025
Modified: Dmitrii Gusev, 28.10.2025
"""

import wave  # создание и чтение аудио файлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой

from loguru import logger
from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
# import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)

# MODEL = "./models/vosk-model-small-ru-0.22"  # small model
MODEL = "./models/vosk-model-ru-0.42"  # big model


def s2t_process(wav_infile: str, model_path: str) -> str:
    """ Process speech from audio file to text string. """

    logger.debug(f"Speech-2-text file: {wav_infile}, model {model_path}.")

    recognized_data: str = ""

    try:

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        # wave_audio_file = wave.open("./output/output-4.wav", "rb")
        wave_audio_file = wave.open(wav_infile, "rb")
        # model = Model("models/vosk-model-small-ru-0.4")
        model = Model(model_path)
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        logger.debug('Start processing for the file specified...')

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки
                # (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]

    except:
        logger.error("Sorry, speech service is unavailable. Try again later")

    return recognized_data


def use_offline_recognition():
    """
    Переключение на оффлайн-распознавание речи
    :return: распознанная фраза
    """

    recognized_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        # if not os.path.exists("models/vosk-model-small-ru-0.4"):
        if not os.path.exists(MODEL):
            print("Please download the model from:\n"
                  "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
            exit(1)

        print('Model path is OK...')

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        wave_audio_file = wave.open("./output/output-4.wav", "rb")
        # model = Model("models/vosk-model-small-ru-0.4")
        model = Model(MODEL)
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        print('Processing...')

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки
                # (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data


if __name__ == '__main__':
    result = use_offline_recognition()
    print("\nresult ===>\n", result)
