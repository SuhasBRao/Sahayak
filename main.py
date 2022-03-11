import pyttsx3 
import speech_recognition as sr

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
            print('Say something.......')
            audio_data = r.listen(source, timeout= 10)
            print("Recognizing...")
            text = r.recognize_google(audio_data, language= 'en-IN')
            text = text.lower()
            return text
        # except sr.UnknownValueError:
        #     print('Not able to recognise')
        except sr.WaitTimeoutError :
            return 0
        # convert speech to text
        
        # print(text)
# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    # listen()
    speak('Hi, How may i help you?')
    # text = listen()
    while(1):
        text = listen()
        if text == 0 or None:
            continue
        else:
            print(text)
    print('no audio')

# } Driver Code ends