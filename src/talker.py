import pyttsx3

def speech(content):
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 0.7)
    converter.say(content)
    converter.runAndWait()
    return

