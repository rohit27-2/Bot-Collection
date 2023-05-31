import pyttsx3
import speech_recognition as sr
import datetime
import requests
import pywhatkit
import pyjokes
import wikipedia
import webbrowser

user = "user"
assistant = "Lexi"

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

def output(audio):
    engine.say(audio)
    engine.runAndWait()


def inputcommand():
    r = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Understanding")
            query = r.recognize_google(audio, language="en-us")
            print("You said: ", query)
        except Exception as e:
            print(e)
            output("Say that again Please...")

    return query


def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        output(f"Good Morning {user}")
    elif (hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}")
    elif (hour >= 18) and (hour < 21):
        output(f"Good Evening {user}")
    output("How may I assist you?")



def weather():
    city = "Hyderabad"
    res = requests.get(
        f"API_KEY"
    ).json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
    print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")


greet()

while True:
    query = inputcommand().lower()

    if("time" in query):
        output("Current time is" + datetime.datetime.now().strftime("%I:%M"))
    elif('date' in query):
        output("Current date is "+ str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))
    elif("open youtube" in query):
        output("Opening Youtube.com")
        output("What do you want to search on youtube.")
        pywhatkit.playonyt(inputcommand())

        continue
    elif ("google" in query):
        output("Opening google.com")
        webbrowser.open("www.google.com")
        continue

    elif ("weather" in query):
        weather()
    elif("joke" in query):
        a = pyjokes.get_joke()
        output(a)
        print(a)
    elif("offline" in query):
        hour = datetime.datetime.now().hour
        if(hour>=21) and (hour<6):
            output(f"Good Night {user}! Have a nice Sleep")
        else:
            output(f"Bye {user}")
        quit()

