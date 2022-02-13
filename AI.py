
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
import wolframalpha
hlw=["hello","hi","hello there","hey","hey wassup","baby","hi honey","babu","sona","pakhi"]
hru=["how are you","how are you doing","whats going on","whats up","wassup","hru","what about you",""]
try:
    app=wolframalpha.Client("6RHU88-P9LTQV83WW")
except Exception:
    print("error") 

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[1].id)
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

def main():
    wishMe()   
    while True:
         query=takecommand().lower()
         if "wikipedia" in query:
             speak("searching wikipedia....")
             query= query.replace("wikipedia", "")
             results=wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia ")
             speak(results)
             break
         elif "bye" in query:
             speak("see you soon sir!")
             break             
         elif "open youtube" in query:
             speak("opening youtube sir, what you want to seach on youtube") 
             s=takecommand()
             webbrowser.open("www.youtube.com/results?search_query=" + s + "")
             break
         elif "are you" in query:
             speak("I am Prox version 1.0 Sir." )   
         elif "open google" in query:
             speak("opening sir") 
             webbrowser.open("https://www.google.com/")
             break
         elif "search" in query:
             speak("what should i search sir? ")
             s=takecommand()
             pyautogui.write(s)
             time.sleep(3)
             pyautogui.press("enter") 
             break   
         elif "open my facebook profile" in query:
             speak("opening facebook sir") 
             webbrowser.open("https://www.facebook.com/ogotumikgo")
                  
         elif "open stackoverflow" in query:
             speak("opening sir")
             webbrowser.open("stackoverflow.com")
             break
         elif "play music" in query:
             speak("playing  sir")
             music_dir= "E:\\new\\MY CHOICE"
             music= os.listdir(music_dir)
             songs=random.choice(music)
             print(songs)
             break
             os.startfile(os.path.join(music_dir,songs))
         elif "volume up" in query:
             speak("volume up sir")    
             pyautogui.hotkey("volumeup")
         elif "volume down" in query:
             speak("volume down sir")    
             pyautogui.hotkey("volumedown") 
             break            
         elif "stop music " in query :
             speak("ok sir")     
             pyautogui.press("space")
             break
         elif " the time" in query:
             strTime=datetime.datetime.now().strftime("%H : %M: %S")
             speak(f"sir, the time is{strTime}")
             break
         elif "open vs code" in query:
             vs="C:\\Users\\PROLOY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             speak("opening sir")
             os.startfile(vs)  
             break
         elif "who is sadu"in query:
             speak(" your girlfriend ")
             break
         elif "open github" in query:
             speak("opening sir")  
             webbrowser.open("https://github.com/proloypoddar?tab=repositories")

         elif "study time" in query:
             speak("should i open bux sir ?")
             time.sleep(3)
             s= takecommand().lower()
             print(s)
             s=str(s)
             if s =="yes":
                 speak("study time , opening BUX sir!")
                 webbrowser.open_new_tab("https://bux.bracu.ac.bd/dashboard")
                 time.sleep(3)
             elif s=="no":
                 speak("ok sir! but you need to study")
             else:
                 print(None)       
         elif "joke" in query:
             My_joke = pyjokes.get_joke(language="en", category="all")
             speak(My_joke)
             break
         elif "tempature"or "weather" in query:
             try:
                 res= app.query(query)
                 print(next(res.results).text)
                 speak(next(res.results).text)
             except:
                print("net error")
         else:
             try:
                 res= app.query(query)
                 print(next(res.results).text)
                 speak(next(res.results).text)
                 break
             except:
                 print("net error")  
                 break  
                        
    proloy() 
def proloy():
    while True:
        query=takecommand().lower()
        if "prox"in query:
            print(query)
            break
    main() 
if __name__=="__main__":
    proloy()