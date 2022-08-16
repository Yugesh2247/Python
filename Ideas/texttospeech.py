import pyttsx3
talk=pyttsx3.init()
tell=input("type what to speech")
talk.say(tell)
talk.runAndWait()