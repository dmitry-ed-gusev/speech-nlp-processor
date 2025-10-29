
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for background noise
    audio = recognizer.listen(source)

audio_file = "path/to/your/audio_file.wav"  # Replace with the path to your audio file
with sr.AudioFile(audio_file) as source:
    audio = recognizer.listen(source)

try:
    print("Converting speech to text...")
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
