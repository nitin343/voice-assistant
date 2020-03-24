import pyttsx3 #pip install pyttsx3==2.6
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am friday Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your eamil', 'password')
    server.sendmail('your email', to, content)
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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

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

        elif 'pycharm' in query:
            codePath = "(paste pychram url path here) "
            os.startfile(codePath)

        elif 'email to team9' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nitinphulekar33@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry team9. I am not able to send this email") 
                
        elif 'how are you' in query:
			speak("I am fine, Thank you") 
			speak("How are you, Sir")
            
        elif "what's your name" in query or "What is your name" in query: 
			speak("My friends call me") 
			speak("friday") 
			print("My friends call me friday")   `      
          
        elif 'exit' in query: 
			speak("Thanks for giving me your time") 
			exit() 
            
        elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Team 9") 
			    
        elif 'lock window' in query: 
			speak("locking the device") 
			ctypes.windll.user32.LockWorkStation() 

	elif 'shutdown system' in query: 
			speak("Hold On a Sec ! Your system is on its way to shut down") 
			subprocess.call('shutdown / p /f') 
				
	elif 'empty recycle bin' in query: 
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
			speak("Recycle Bin Recycled") 
            
        elif "don't listen" in query or "stop listening" in query: 
			speak("for how much time you want to stop jarvis from listening commands") 
			a = int(takeCommand()) 
			time.sleep(a) 
			print(a)   
            
            
        elif "write a note" in query: 
			speak("What should i write, sir") 
			note = takeCommand() 
			file = open('jarvis.txt', 'w') 
			speak("Sir, Should i include date and time") 
			snfm = takeCommand() 
			if 'yes' in snfm or 'sure' in snfm: 
				strTime = datetime.datetime.now().strftime("%H:%M:%S") 
				file.write(strTime) 
				file.write(" :- ") 
				file.write(note) 
			else: 
				file.write(note) 
		        
	elif "show note" in query: 
			speak("Showing Notes") 
			file = open("jarvis.txt", "r") 
			print(file.read()) 
			speak(file.read(6)) 
    
            
