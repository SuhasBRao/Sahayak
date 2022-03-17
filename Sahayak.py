# Use ctrl + shift + i for auto alignment on ubuntu
# https://vitux.com/test-your-internet-speed-through-ubuntu-command-line/
# above link shows how to test internet speed using ubuntu terminal
# Speed test function in this script works only after installing
# the functionality shown in the above link

# import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import subprocess
import gtts
import playsound
import os

r = sr.Recognizer()

engine = pyttsx3.init()


def speak(text):
    tts = gtts.gTTS(text, lang = 'en')
    tts.save('audio.mp3')
    playsound.playsound('audio.mp3')
    os.remove('audio.mp3')


def listen():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        # audio_data = r.record(source, duration=5)

        r.adjust_for_ambient_noise(source, duration=0.2)
        r.energy_threshold = 100
        try:
            print('listening.......')
            audio_data = r.listen(source, phrase_time_limit=10 ,timeout=5)
            print("Recognizing...")
            text = r.recognize_google(audio_data, language='en-IN')
            return text.lower()

        except sr.UnknownValueError:
            print('Not able to recognise')

        except sr.WaitTimeoutError:
            return 0


def thank_you_response():
    speak('Your welcome Master')


def getdate():

    now = datetime.now()
    date = now.strftime("%d")
    # month = now.strftime("%m")

    month_name = now.strftime('%B')

    year = now.strftime("%y")
    # print(f'{date}/{month}/{year}')
    # print(month_name)

    speak("Today's date is {0} of {1} {2} ".format(date, month_name, year))


def getTime():

    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")

    speak(f'Current time is {cur_time}')


def searchWIKI():
    global text
    query = text[:]
    query = query.split(' ')
    query = " ".join(query[0:])

    speak("I am searching for " + query)
    print(wikipedia.summary(query, sentences=3))
    speak(wikipedia.summary(query,
                            sentences=3))

def speedtest():
    speak('Testing the internet Speed, This will take long Please wait')
    # below line converts the output from bytes to string format
    ret_Val = subprocess.run('speedtest-cli', capture_output= True)
    print(ret_Val)
    string = str(ret_Val.stdout)
    download_speed_data = string.partition('Download:')[2].split()
    download_speed = download_speed_data[0]
    
    upload_speed_data = string.partition('Upload:')[2].split()
    upload_speed = upload_speed_data[0]
    
    speak(f'Download speed is {download_speed} Mega bits per second')
    speak(f'Upload speed is {upload_speed} Mega bits per second')
    
    
    
def main():
    global text
    while(1):
        text = listen()
        print(text)

        if text == 0 or text == None:
            continue

        else:

            # text = text.replace('sahayak', "")

            # list of keys to check in text
            key_words_list = ["today's date", 'thank you', 'current time',
                              'what', 'search', 'thankyou', 'internet speed', 'net speed']

            # create a list to map the True values for keys in
            # above list
            # TRUE values are those which exists in the user input.
            res = list(map(lambda x: x in text, key_words_list))

            # get the index where the value is True
            res = [i for i, val in enumerate(res) if val]

            # find the key to respond
            key = key_words_list[res[0]]

            # print(res)
            print(key)

            # {'hello sahayak': speak('Hello master, how can i help you'),
            {"today's date": getdate,
             "thankyou": thank_you_response,
             "thank you": thank_you_response,
             'current time': getTime,
             'search': searchWIKI,
             'what': searchWIKI,
             'net speed': speedtest,
             'internet speed': speedtest
             }[key]()


# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here

    # speak('Hi, How may i help you?')
    speak('Sahayak is listening')
    # allows the program to run
    try:
        main()
    except Exception as e:
        speak(f'Sahayak crashed due to {e}')


# } Driver Code ends
