import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    

def hear():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def welcome():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning sir!")

    elif 12 <= hour < 18:
        speak("Good afternoon sir!")

    else:
        speak("Good evening sir!")

    speak("How can I assist you?")


def execute_comd(command):
    if "hello bot" in command:
        speak("Yes sir iam here!")
   
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        search_web(search_query)

    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")

    elif 'play music' in command:
        webbrowser.open("https://www.spotify.com")

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif 'date' in command:
        now = datetime.datetime.now().strftime("%D-%m-%Y")
        speak(f"The date is {now}")

    elif "repeat with me" in command:
        text=command.replace("repeat with me","").strip()
        speak(f"iam repeating{text}")


    elif 'exit' in command:
        speak("Thank you sir,Goodbye")
        exit()

    else:
        speak("I'm sorry, I couldn't understand your command.")



def search_web(query):
    speak(f"Searching for {query} on the web...")
    encoded_query = urllib.parse.quote_plus(query)
    url = "https://www.google.com/search?q=" + encoded_query
    webbrowser.get().open(url)


if __name__ == "__main__":
    welcome()
    while True:
        command = hear().lower()
        if command:
            execute_comd(command)
