from email.mime import audio
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()

def speakText(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()


with sr.Microphone() as sourceM:

    print("Calibrating the file...")
    r.adjust_for_ambient_noise(sourceM, duration=2)
    print("Done")

    audioL = r.listen(sourceM)

    text = r.recognize_google(audioL)
    textL = text.lower()

    print("Did u say? " + textL)
    




# try:
#     print("Transcription: " + r.recognize_google(audio))
# except LookupError:
#     print("Could not understand.")
