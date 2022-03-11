import datetime
import random
from tkinter import E
import webbrowser 
import os
import pyttsx3
import speech_recognition as sr
import wikipedia

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices)
engine.setProperty('voice',voices[0].id)


def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good morning user")
    if(hour >= 12 and hour < 18):
        speak("Good afternoon user")
    if(hour >= 18 and hour < 20):
        speak("Good evening user")
    if(hour >= 20 and hour < 24):
        speak("Good night user")
    
# def takecomm():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening...")
#         r.pause_threshold = 0.2 
#         audio=r.listen(source)

#     try:
#         print("recognising...")
#         query=r.recognize_google(audio, language="en-in")
#         print("user said",query)
#     except Exception as e:
#         print(e)
#         print("say that again pls ... ")
#         return "none"

if __name__ == "__main__":
        wishme()
        # takecomm()

while(0<10):
    speak("how may i help - ")
    wdywtd=input("how may i help - ")
    if(".com" in wdywtd):
        webbrowser.open("https://www."+wdywtd)
    if("search" == wdywtd):
        wdywtsog=input("What do you want to search - ")
        webbrowser.open("https://www.google.com/search?q="+wdywtsog)
    if("search in youtube" in wdywtd):
        wys=input("what should we search for u in youtube - ")
        webbrowser.open("www.youtube.com/results?search_query="+wys)
    if("open" == wdywtd):
        wpdywto=input("which program do you want to open - ")
        if(""!=wpdywto and "chrome" != wpdywto):
            wso=input("what should we open - ")
            os.system(wso+".exe")
        if("chrome" in wpdywto):
            webbrowser.open("www.google.com")
    if("youtube" == wdywtd or "open youtube" == wdywtd):
        ac=input("Any specific channel (pls type without space)- ")
        if("" != ac or "no" != ac):
         webbrowser.open("https://www.youtube.com/c/"+ac)
        
        if("" == ac or "no" == ac):
            print("opening ...")
            webbrowser.open("www.youtube.com")
        
    if("class" == wdywtd):
        print("opening ...")
        webbrowser.open("https://meet.google.com/dfy-mued-ibc?authuser=3")
    if("exclass" == wdywtd):
        print("opening ...")
        webbrowser.open("https://meet.google.com/wvn-hwjv-fyp?authuser=3")
    if("play a game"==wdywtd):
        gl=["Guess the word","Guess the number","quistionaire","secret diary","stone paper scissor","quistionaire 2","Odd Even"]
        glr=random.choice(gl)
        if("Guess the word" == glr):
            print("playing:",glr)
            import Guesstheword
        if("Guess the number" == glr):
            print("playing:",glr)
            import Guessthenumber
        if("quistionaire" == glr):
            print("playing:",glr)
            import quistionaire
        if("secret diary" == glr):
            print("playing:",glr)
            import secretdiary
        if("stone paper scissor" == glr):
            print("playing:",glr)
            import stone_paper_scissor
        if("quistionaire 2" == glr):
            print("playing:",glr)
            import quistionaire2
        if("Odd Even" == glr):
            print("playing:",glr)
            import oddeven
    if("vs-code" == wdywtd):
        path= "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    if("stop" in wdywtd):
        speak("Ok closing")
        print("closing...")
        print("still doing")
        print("done")
        break
    if("python projects opener" in wdywtd):
        print("Opening...")
        speak("opening")
    if("play a song" in wdywtd):
        wstp=input("Which song should we play - ")


    if("wikipedia" in wdywtd):
        speak("searching")
        wdywtd=wdywtd.replace("wikipedia","")
        results=wikipedia.summary(wdywtd , sentences=2)
        print("according to wikipedia :",results)
        speak("according to wikipedia")
        speak(results)
    if("time" in wdywtd):
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir,The time is {strtime}")
        speak(f"Sir,The time is {strtime}")

    else:
        speak("I cant do that. ")
        


    


