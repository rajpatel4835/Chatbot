# Importing necessary libraries/modules
import speech_recognition as sr
import datetime
import gtts
from playsound import playsound
from transformers import BertForQuestionAnswering, pipeline, AutoTokenizer

# Loading BERT-based model and tokenizer for question answering
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')

# Loading context from a file
with open("data.txt", "r") as file:
    context = file.read()

# Setting up BERT-based question-answering pipeline
nlp=pipeline('question-answering',model=model, tokenizer=tokenizer, truncation=True,padding=True )

# Function to convert text to speech and play the audio
def speak(audio):
    tts=gtts.gTTS(audio)
    tts.save("helloo.mp3")
    playsound("C:/Users/91879/Desktop/Project/Chatbot/helloo.mp3")
    
# Function to greet the user based on the time of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")
        speak("Good Morning!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")
    elif hour>=12 and hour<18:
        print("Good Afternoon!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")   
        speak("Good Afternoon!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")   
    else:
        print("Good Evening!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")
        speak("Good Evening!,i am Sofia,  Your virtual assistant for rajkiya engineering college kannauj, Please tell me how may I help you sir?")  

# Function to listen to the user's voice input using a microphone
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
        return "No"
    return query

# Main execution starts here
if __name__ == "__main__":
    wishMe()
    while True:
        query = voiceinput().lower()
        if query!="no":
            result=nlp({
                        'question' : query,
                        'context' : context
                    })
            print(result['answer'])
            speak(result['answer'])