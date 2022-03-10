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
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data, language= 'en-IN')
        print(text)
        
# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    # listen()
    speak('Hi, How may i help you?')
    listen()

# } Driver Code ends