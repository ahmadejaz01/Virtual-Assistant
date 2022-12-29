import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour >=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")  
    speak("I am Jarvis. please tell me how may I help you sir")     

def takeCommand():
    # it takes microphone input from user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query )

    except Exception as e:
        # print(e)
        print("say that again please")
        return "None"  
    return query          
if __name__ =="__main__":
    # speak("ejaz you are a very good programmer I know")
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com") 
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com") 
        elif 'play music' in query:
            music_dir='G:\\EJAZ\\Songs\\Music\\Jagjit Singh'
            songs=os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif 'the time' in query:
            timestr=datetime.datetime.now().strftime("%H:%M:%S")
            print(timestr)
            speak(f"Sir, the time is {timestr}")
        elif 'open eclipse' in query:
            path = "C:\\Users\\Lenovo\\Downloads\\eclipse-jee-neon-3-win32-x86_64\\eclipse\\eclipse.exe"
            os.startfile(path)
        elif 'what is my name' in query:
            speak("you are Mr. Ejaz Ahmad sir")
        elif 'who are you' in query:
            speak("I am a virtual assistant and my name is Jarvis, and my task is to assist you sir")
        elif 'quit' in query:
            speak("good bye sir")
            exit()
        
