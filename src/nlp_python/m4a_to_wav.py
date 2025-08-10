from pydub import AudioSegment


m4a_file = './audio/58-5-3 часть.m4a'
wav_filename = './audio/output.wav'

sound = AudioSegment.from_file(m4a_file, format='m4a')
file_handle = sound.export(wav_filename, format='wav')
