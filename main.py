# 1 is for female
# 0 is for male

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1],id)
engine.setProperty('voice',voices[1].id)

# We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run
# when the modules are imported. When the Python interpreter reads a file, the __name__
# variable is set as __main__ if the module being run, or as the module's name if it is imported.

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning")
    elif hour>12 and hour <18:
        speak("good afternoon")
    else :
        speak("good evening")
    speak("Hii ,I am Jarvis,How may I help you now.")

def takecommand():
    #it takes microphone input from the user and gives string output
    r=sr.Recognizer()#a class named recognizer helps to recognize audio
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold=1#second of non speaking audio before a phrase gets completed
        audio=r.listen(source)

    try:
        print("recognizing......")
        query=r.recognize_google(audio,language='en-in')
        #english-india and a query is been asked through class recognizer
        print(f"user said: {query}\n ")
    except Exception as e:
        print(e)
        print("say that again please.....")
        return "none" # here none is a string and not python command
    return query

# def sendEmail(to,content) :
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login('youremail@gmail.com', 'your-password')
#         server.sendmail('youremail@gmail.com', to, content)
#         server.close()

if __name__=="__main__" :
    speak("Hi Geetika")
    wishMe() #calling wishMe function
    while True:
        # takecommand()
        query=takecommand().lower()
        #logic for executing tasks  based on query
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia"," ") #the wikipedia in the query is replaced by a blank here
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\Admin\\PycharmProjects\\AIVoiceAssistant\\LOFI Songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            #The time in 24-hour notation (%H:%M:%S)
            #The strftime() function is used to convert date and time objects to their string representation
            speak(f"babe the time is {strTime}")
        elif 'open vscode' in query:
            codePath="C:\\Users\\Admin\\PycharmProjects\\AIVoiceAssistant\\VSCodeSetup-x64-1.64.0.exe"
            os.startfile(codePath)
#         elif 'email to geetika' in query:
#             try:
#                 speak("what should I say")
#                 content=takecommand()
#                 to = "geetikayourEmail@gmail.com"
#                 sendEmail(to,content)
#                 speak("email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("sorry the email could not be sent")
# f=open("info.txt")
# content=f.read()
# print (content)
# f.close()
