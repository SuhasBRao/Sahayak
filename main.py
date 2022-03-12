from calendar import month
import pyttsx3
from datetime import datetime 
import speech_recognition as sr
from webob import year

r = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 190)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        # audio_data = r.record(source, duration=5)
        
        r.adjust_for_ambient_noise(source, duration= 0.2)
        
        try:
            print('listening.......')
            audio_data = r.listen(source, timeout= 10)
            print("Recognizing...")
            text = r.recognize_google(audio_data, language= 'en-IN')
            # text = text.lower()
            return text.lower()
        except sr.UnknownValueError:
            print('Not able to recognise')
        except sr.WaitTimeoutError :
            return 0
        
        # print(text)

def getdate():
    now = datetime.now()
    date = now.strftime("%d")
    month = now.strftime("%m")
    
    month_name = now.strftime('%B')
    
    year = now.strftime("%y")
    print(f'{date}/{month}/{year}')
    print(month_name)
    
    return date, month_name, year

def getTime():
    now = datetime.now()
    dt_time = now.strftime("%H:%M:%S")
    return dt_time
    
    
# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    # listen()
    speak('Hi, How may i help you?')
    # text = listen()
    # allows the program to run continously
    while(1):
        text = listen()
        print(text)
        if text == 0 or text == None:
            continue
        if text != None or text != 0:
            if 'date' in text:
                date,month, year = getdate()
                speak("Today's date is {0} of {1} {2} ".format(date, month, year))
            if 'time' in text:
                pass
            if 'thank'
        else:
            print(text)
    print('no audio')

# } Driver Code ends