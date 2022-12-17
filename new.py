import speech_recognition as sr
import datetime
import os
import time
import gtts
from playsound import playsound

f=open('new.txt','r')

def speak(audio):
    tts=gtts.gTTS(audio)
    tts.save("helloo.mp3")
    playsound("helloo.mp3")
    os.remove('helloo.mp3')
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")   
    else:
        speak("Good Evening!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")  
def voiceinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.energy_threshold=200
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query
def txt(a):
  i=1
  while i<=a:
    c=f.readline()
    i=i+1
  m=f.readline()
  print(m)
  speak(m)
  f.seek(0)
if __name__ == "__main__":
    wishMe()
    while True:
        query = voiceinput().lower()
        if "location" in query or "about kannauj" in query:
            print(f.readline())
            f.seek(0)
            speak(f.readline())
            f.seek(0)
        elif "many branches" in query or "number of branch" in query :
            txt(3)
        elif "many seats" in query or "number of seats" in query:
            txt(6)
        elif "average placement" in query:
            txt(9)
        elif "hod of cs" in query or "hod of computer science" in query:
            txt(12)
        elif "hod of electronic" in query:
            txt(15)
        elif "hod of civil" in query:
            txt(18)
        elif "hod of electrical" in query:
            txt(21)
        elif "director of" in query:
            txt(24)
        elif "infrastructure" in query:
            txt(27)
        elif "how many hostels " in query or "number of hostel" in query:
            txt(30)
        elif "distance from bus station" in query or  "distance from railway" in query or "How far it is from Railway" in query:
            txt(33)
        elif "canteen" in query:
            txt(36)
        elif "how many sports facilities" in query or "what are the sports facilities" in query:
            txt(39)
        elif "tuition fee" in query or "fee structure" in query:
            txt(42)
        elif "College is owned" in query or "type of college" in query:
            txt(45)
        elif "established" in query:
            txt(48)
        elif "campus size" in query:
            txt(51)
        elif "total fee" in query:
            txt(54)
        elif "academic" in query:
            txt(57)