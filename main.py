import pyttsx3 #pip install pyttsx3 txt-2-speech lib
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2 #used to give interface
import random
from requests import get
import pywhatkit as kit #whatsapp
import sys 

engine = pyttsx3.init('sapi5')#voices for jarvis
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")  
    
# to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('ansh.cs.cs@gmail.com','gohannaruto')
    server.sendmail('ansh.cs.cs@gmail.com',to ,content)
    server.close()     


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "open cmd" in query:
            npath = "C:\\Users\\vibha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.system("start cmd")
        
            
        elif "play music" in query:
            npath = "C:\\Users\\vibha\\songs\\Arjan Vailly - Animal_320-(PagalWorld.Com.IN).mp3"
            music_dir = "C:\\Users\\vibha\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
           # os.startfile(npath)
           
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print(ip)
                
            
        elif 'open notepad' in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2310.13.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)
        
        elif "open wps" in query:
            npath = "C:\\Users\\vibha\\AppData\\Local\\Kingsoft\\WPS Office\\12.2.0.13359\\office6\\wps.exe"
            os.startfile(npath)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        
        elif 'open google' in query:
            speak("what should i search for")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'play song on youtube' in query:
            kit.playonyt('295')
            
        elif "open camera" in query:
            cap  = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f/im notepad.exe")
            
            
        elif 'send email to ansh' in query:
            try:
                speak('what sould i say?')
                content = takeCommand().lower()
                to = "ansh.as.as100@gmail.com"
                sendEmail(to,content)
                speak('email has been sent to ansh')
            
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email to ansh")
        elif 'chhotu exit'in query:
            speak("thanks for using me, have a good day")
            sys.exit()
            
            