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
            return text.lower()
        
        except sr.UnknownValueError:
            print('Not able to recognise')
            
        except sr.WaitTimeoutError :
            return 0

          
def thank_you_response():
    speak('Your Welocme, Master!!')
    
def getdate():
    now = datetime.now()
    date = now.strftime("%d")
    month = now.strftime("%m")
    
    month_name = now.strftime('%B')
    
    year = now.strftime("%y")
    print(f'{date}/{month}/{year}')
    # print(month_name)
    
    speak("Today's date is {0} of {1} {2} ".format(date, month_name, year))
            
def getTime():
    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    
    speak(f'Current time is {cur_time}')
                


# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    
    # speak('Hi, How may i help you?')
    
    # allows the program to run continously
    while(1):
        text = listen()
        print(text)
        
        if text == 0 or text == None:
            continue
        
        if 'sahayak' in text:

            text = text.replace('sahayak', "")
            
            # list of keys to check in text
            key_words_list = ["today's date", 'thankyou']
            
            # create a list to map the True values for keys in 
            # above list
            
            res = list(map(lambda x: x in text, key_words_list))
            
            # get the index where the value is True
            res = [i for i,val in enumerate(res) if val]
            
            # find the key to respond
            key = key_words_list[res[0]]
            
            print(res)
            print(key)
            
            # {'hello sahayak': speak('Hello master, how can i help you'),
            {"today's date": getdate,
             ("thank you", 'thankyou'): thank_you_response,
             'current time': getTime}[key]()
            
            # func
             
       
       
    print('no audio')

# } Driver Code ends