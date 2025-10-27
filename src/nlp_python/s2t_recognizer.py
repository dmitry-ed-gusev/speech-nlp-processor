"""
S2T - Speech-To-Text Recognizer Module.

Created:  Dmitrii Gusev, 10.08.2025
Modified: Dmitrii Gusev, 27.10.2025
"""

import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой

from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)

# MODEL = "./models/vosk-model-small-ru-0.22"  # small model
MODEL = "./models/vosk-model-ru-0.42"  # big model


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
