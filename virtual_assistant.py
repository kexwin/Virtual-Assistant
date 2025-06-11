import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyautogui
import requests
import keyboard
import os
import pywhatkit
import random
import ecapture as ec
from tkinter import *
from tkinter import Button
from tkvideo import tkvideo
from PIL import Image, ImageTk

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

m = ['happy', 'glad', 'nice', 'great', 'good']
ad = random.choice(m)
l = ['wonderful', 'exquisite', 'joyful', 'nice', 'splendid', 'great', 'lovely', 'marvellous', 'fantastic']
adj = random.choice(l)
def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print('this is the query that was made: ', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)
            speak('sorry i could not understand')
            activate_va()

def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time

def speak(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def make_request(url):
  response = requests.get(url)
  return response.text

def activate_va():
    user_query = input_query()
    print('you said: ', user_query)

    if 'wikipedia' in user_query:
        speak("Searching on Wikipedia")
        user_query = user_query.replace('wikipedia', ' ')
        result = wikipedia.summary(user_query, sentences=4)
        print(result)
        speak(result)
    elif 'yourself' in user_query:
        speak('I am your virtual assistant. I am here to simplify various chores of yours like automating chrome, youtube or even send whatsapp messages. How can I help you today?')

    elif 'time' in user_query:
        current_time = report_time()
        print(f"the current time is {current_time}")
        speak(f"the current time is {current_time}")

    elif 'youtube' in user_query:
        speak('Initiating your request')
        webbrowser.open('www.youtube.com')
        speak('Done')

    elif 'chrome' in user_query:
        speak('on it')
        os.system('start chrome')
        speak('done')

    elif 'google' in user_query:
        speak('initiating your request')
        webbrowser.open('www.google.com')
        speak('done')

    elif 'new tab' in user_query:
        speak('initiating your request')
        keyboard.press_and_release('ctrl + t')
        speak('done')

    elif 'new window' in user_query:
        speak('initiating your request')
        keyboard.press_and_release('ctrl + n')
        speak('done')

    elif 'close tab' in user_query:
        speak('initiating your request')
        keyboard.press_and_release('ctrl + w')
        speak('done')

    elif 'close window' in user_query:
        speak('initiating your request')
        keyboard.press_and_release('alt + F4')
        speak('done')

    elif 'stop' in user_query:
        speak('okay, have a '+adj+' day ahead')
        exit()

    elif 'joke' in user_query:
        random_joke = pyjokes.get_joke()
        print(random_joke)
        speak(random_joke)

    elif 'command prompt' in user_query:
        speak('opening command prompt')
        keyboard.press_and_release('ctrl + shift + c')
        speak('done.')

    elif 'minimise' in user_query:
        speak('minimizing all the windows')
        keyboard.press_and_release('win + m')
        speak('done.')

    elif 'open spotify' in user_query:
        speak('opening spotify')
        keyboard.press_and_release('ctrl + alt + s')

    elif 'shutdown' in user_query:
        speak('alright, shutting down your laptop')
        os.system("shutdown /s /t 0")
        keyboard('ctrl + alt + s')
        keyboard.press_and_release('ctrl + alt +s')

    elif 'screenshot' in user_query:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak('Screenshot taken.')

    elif 'capture' in user_query:
        speak('alright, captured the moment for you.')
        ec.capture(0,"eyes on you", "img.png")

    elif 'thank you' in user_query:
        speak('You are most welcome. Tell me if I could do anything else.')

    elif 'thanks' in user_query:
        speak('Anytime sir. Is there anything else i could help you with?')

    elif 'nothing' in user_query:
        speak('alright. See you around.')
        exit()

    elif 'hello' in user_query:
        speak('Hello there. How can I  help you?')

    elif 'terminate' in user_query:
        speak('Okay, signing off.')
        exit()

    elif 'how are you' in user_query:
        speak("My lawyer has stated that I should not answer that question.")

    elif 'doing good' in user_query:
        speak('well,  *cries in binary*. What about you?')
        i = input_query()
        if ad in i:
            speak(+ad+'to hear that.')
        elif 'great' in i:
            speak('I am glad to hear it!')
        elif 'not' in i:
            speak('is there anything i can do to make you feel better?')

    elif 'search' in user_query:
        speak("What do you want me to search for?")
        search_term = input_query()
        search_url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get(
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
        speak(f"here are the results for the search term: {search_term}")

    elif 'repeat' in user_query:
        speak('what would you like me to repeat?')
        repeat = input_query()
        speak(f'you said: "{repeat}"')

    elif 'message' in user_query:
        speak("what is the content of the message? \n")
        message = input_query()
        speak('whom do i send the message?')
        name = input_query()
        n1 = name.lower()
        if '{add the person\'s name}' in n1:
            pywhatkit.sendwhatmsg_instantly('{add the desired number}' , message, True)
            speak('Message sent successfully')
        else:
            speak(f'{name} does not exist in the contact list. Please update it.')


    elif '+' in user_query:
        l = str(user_query)
        L = l.split()
        sum = 0
        for i in L:
            if i.isnumeric():
                sum += int(i)
        print(sum)
        speak(sum)


    elif '-' in user_query:
        l = str(user_query)
        L = l.split()
        diff = 0
        for i in L:
            if i.isnumeric():
                diff = int(i) - diff
                diff1 = -1 * diff
        print(diff1)
        speak(diff1)

    elif 'x' in user_query:
        l = str(user_query)
        L = l.split()
        pro = 1
        for i in L:
            if i.isnumeric():
                pro *= int(i)
        print(pro)
        speak(pro)

    elif '/' in user_query:
        numbers = [int(word) for word in user_query.split() if word.isdigit()]
        if len(numbers) == 2 and numbers[1] != 0:
            result = numbers[0] / numbers[1]
            print(result)
            speak(result)
        else:
            print("Invalid division operation. Please provide two non-zero numbers.")
            speak("Invalid division operation. Please provide two non-zero numbers.")

    elif 'power' or 'raised to' in user_query:
        numbers = [int(word) for word in user_query.split() if word.isdigit()]
        if len(numbers) == 2:
            result = numbers[0] ** numbers[1]
            print(result)
            speak(result)

speak('Good afternoon. How can I help you today?')

root = Tk()
root.title('Smart Assistant')
root.geometry('500x450')
root.resizable(False, False)
root.configure(background='black')

image = Image.open("mic.jpg")
photo = ImageTk.PhotoImage(image)
b = Button(root, image = photo, command=activate_va)
b.config(width=40, height=45)
b.pack(padx=2, pady=0)

lblvideo = Label(root)
lblvideo.pack()
player = tkvideo('vid.mp4', lblvideo, loop=1, size=(500,400))
player.play()
root.mainloop()
