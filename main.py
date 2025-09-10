import pyttsx3
import speech_recognition as sr
import time
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()  # Fixed capitalization
    with sr.Microphone() as source:  # Fixed capitalization
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            return ""

def jarvis_alarm(alarm_time):
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            speak(f"Good morning sir, it's {alarm_time}, time to wake up sir.")  
            while True:  # Fixed typo from "Ture" to "True"
                command = listen()
                if "no" in command:
                    speak("Alright sir, I will wake you in 10 minutes.")
                    print("alarm snoozd 1 min")
                    time.sleep(60)
                    speak("Sir, it's time now.")
                elif "ok" in command:
                    speak("Have a great day sir.")
                    print("alarm staped")
                    return
        time.sleep(1)

# Set the alarm time here in HH:MM format
st_alarm = input("set alarm time (HH:MM):")
jarvis_alarm(st_alarm)
