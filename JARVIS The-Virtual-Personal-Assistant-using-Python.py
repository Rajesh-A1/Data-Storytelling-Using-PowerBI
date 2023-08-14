import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
MASTER = "Sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("i am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajeshalagupandiyan@gmail.com', 'password')
    server.sendmail("rajeshpandiyan1110@gmail.com", to, content)
    server.close()

    



#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

#main program starting
def main():
    speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open YouTube' in query.lower():
        browser = webbrowser.get('google-chrome')
        browser = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
        browser.open('codespeedy.com')
        browser.open_new('codespeedy.com')

    elif 'show today news' in query.lower():
        #webbrowser.open('youtube.com')
        url = "https://google.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.open_new_tab(chrome_path).open("https://google.com/")

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\RAJESH\\Music\\songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'what time now' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open vscode' in query.lower():
        codePath = "C:\\Users\\RAJESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'email to rj' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "rajeshalagupandiyan@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to raj")
        except Exception as e:
            print(e)


main()