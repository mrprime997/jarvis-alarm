import pyttsx3, speech_recognition as sr, time
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (720, 1600)

engine = pyttsx3.init()

def speak(text):
    engine.say(text); engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try: return r.recognize_google(audio).lower()
        except: return ""

def jarvis_alarm(alarm_time, label):
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            speak(f"Good morning sir, it's {alarm_time}")
            label.text = f"Alarm! {alarm_time}"  # show on app
            while True:
                command = listen()
                if "no" in command:
                    speak("Snoozing 1 minute"); time.sleep(60)
                    speak("Sir, it's time now."); label.text = "Wake up!"
                elif "ok" in command:
                    speak("Have a great day sir."); return
        time.sleep(1)

class AlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.input = TextInput(hint_text="Set alarm (HH:MM)", font_size=6) # (1)
        self.label = Label(text="No alarm set", font_size=6)                # (2)
        btn = Button(text="Start Alarm", font_size=6)                       # (3)
        btn.bind(on_press=lambda x: jarvis_alarm(self.input.text, self.label)) # (4)
        layout.add_widget(self.input); layout.add_widget(btn); layout.add_widget(self.label)
        return layout

AlarmApp().run()