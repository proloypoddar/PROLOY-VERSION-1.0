from typing import MutableSequence
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyautogui
import time
import pyjokes
# import wolframalpha
# try:
#     app=wolframalpha.client("6RHU88-P9LTQV83WW")
# except Exception:
#     print("some feature are not work")    

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING !  ")   
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON ! ")  
    else:
        speak("GOOD EVENING !")    
    speak(" please tell me how can i help you")    
def takecommand():
    #it take microphone input from user and return  outpur
             
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing") 
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")      
    except Exception as e:
    
        # print(e)
        print("Say that again please....")   
        return "None"  
    return query    
  
    
if __name__=="__main__":
    wishMe()   
    while True:
         query=takecommand().lower()
         if "wikipedia" in query:
             speak("searching wikipedia....")
             query= query.replace("wikipedia", "")
             results=wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia ")
             speak(results)
         elif "open youtube" in query:
             speak("opening youtube sir") 
             webbrowser.open("https://www.youtube.com/")
         elif "who are you?" in query:
             speak("I am Prox version 1.0 Sir." )   
         elif "open Google" in query:
             speak("opening sir") 
             webbrowser.open("https://www.google.com/")
             
         elif "open my facebook profile" in query:
             speak("opening facebook sir") 
             webbrowser.open("https://www.facebook.com/ogotumikgo")
                  
         elif "open stackoverflow" in query:
             speak("opening sir")
             webbrowser.open("stackoverflow.com")
         elif "play music" in query:
             speak("playing  sir")
             music_dir="F:\\audios"
             music= os.listdir(music_dir)
             songs=random.choice(music)
             print(songs)
             os.startfile(os.path.join(music_dir,songs))
         elif "volume up" in query:
             speak("volume up sir")    
             pyautogui.hotkey("volumeup")
         elif "volume down" in query:
             speak("volume down sir")    
             pyautogui.hotkey("volumedown")             
         elif "stop music " in query :
             speak("ok sir")     
             pyautogui.press("space")
         elif " the time" in query:
             strTime=datetime.datetime.now().strftime("%H : %M: %S")
             speak(f"sir, the time is{strTime}")
         elif "open vs code" in query:
             vs="C:\\Users\\PROLOY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             speak("opening sir")
             os.startfile(vs)  
         elif "who is sadu"in query:
             speak(" your girlfriend ")
         elif "open github" in query:
             speak("opening sir")  
             webbrowser.open("https://github.com/proloypoddar?tab=repositories")
        #  elif "University name " or "study" in query:
        #      speak(" BRAC UNIVERSITY SIR..!")    
         elif " study time" in query:
             speak("should i open bux sir ?")
             time.sleep(100)
             
             if "yes" in query:
                 speak("study time , opening BUX sir!")
                 webbrowser.open_new_tab("https://bux.bracu.ac.bd/dashboard")

             else:
                 print(None)       
         elif " joke " in query:
             My_joke = pyjokes.get_joke(language="en", category="all")
             speak(My_joke)

