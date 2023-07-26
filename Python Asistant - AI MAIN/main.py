"""Module"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
"""import pyaudio"""
import os.path
"""Akhir Module"""
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
"""from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request"""
"""End"""

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Mendengarkan......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hexa' in command:
                command = command.replace('hexa', '')
                print(command)
    except:
        pass
    return command



def run_hexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('search, found, Have for listening')
        pywhatkit.playonyt(song)
    elif 'open youtube' in command:
        talk('searching, found, opening youtube')
        webbrowser.open('https://www.youtube.com/')
    elif 'open youtube music' in command:
        talk('searching, found, opening youtube')
        print(talk)
        webbrowser.open('https://music.youtube.com/')
    elif 'open facebook' in command:
        talk('searching, found, opening facebook')
        webbrowser.open('https://www.facebook.com/')
    elif 'open chrome' in command:
        talk('opening, chrome')
        subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif 'my favorite song' in command:
        talk('searching, found, opening facebook')
        webbrowser.open('https://music.youtube.com/watch?v=XQGJ6GEhsUM&list=RDAMVMXQGJ6GEhsUM')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'up the volume' or 'increase volume':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Get current volume
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 9.0, None)
    elif 'down the volume' or 'turn it down the volume':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Get current volume
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 9.0, None)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_hexa()


"""wake_word = "Wake up"

while True:
    print("Listening")
    text = take_command()

    if text.count(wake_word) > 0:
        talk("I am ready")
        run_hexa()
"""