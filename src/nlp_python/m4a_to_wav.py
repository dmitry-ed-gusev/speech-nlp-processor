from pydub import AudioSegment


# m4a_file = './audio/58-5-3 часть.m4a'
m4a_file = './audio/Острогоржское_Каротоякское_21_5_9_4_вср_часть_4.m4a'
wav_filename = './output/output-4.wav'

sound = AudioSegment.from_file(m4a_file, format='m4a')
file_handle = sound.export(wav_filename, format='wav')
