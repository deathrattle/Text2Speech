import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say")
    audio=r.listen(source)

try:
    text=r.recognize_google(audio)
    print("Say"+text)
except:
    print("Translation fail")
