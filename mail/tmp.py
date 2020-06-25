import speech_recognition as sr
import os
import pygame
import time
import gtts
def read_and_wait():
    r = sr.Recognizer()
    m = sr.Microphone()
    ret=""
    try:
        print("Calibrating...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            pygame.mixer.init()
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                if(value=="stop" or value=="Stop" or value=="STOP"):
                    break
                obj  = gtts.gTTS(text=value,lang='en-in')
                obj.save('tmp.mp3')
                print("Calling Back")
                '''
                pygame.mixer.music.load('tmp.mp3')
                pygame.mixer.music.play()


                busy=True
                while busy==True:
                    if pygame.mixer.music.get_busy()==False:
                        busy=False
                pygame.quit()
                os.remove('tmp.mp3')
                '''
                os.system("lame --decode tmp.mp3 - | play -")
                os.remove("tmp.mp3")
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(value))
                
                
                confirmation = input("Proceed??")
                if(confirmation=="N" or confirmation=="No"):
                    continue
                ret += value
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
    return ret
