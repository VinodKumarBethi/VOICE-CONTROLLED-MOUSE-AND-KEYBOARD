import pyautogui
import speech_recognition
import gui_cntrl
import pyttsx3
from playsound import playsound
import time
tts_engine=pyttsx3.init()
# The gui instance will be used to call GUI functions defined by us in 'gui_cntrl.py'
gui = gui_cntrl.gui_control()
recognizer = speech_recognition.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

with speech_recognition.Microphone() as src:
    
    while True:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            playsound('D:/VS Code Projects/Major_project/2yT.wav')
            print("\n\nThreshold Value After calibration:" + str(recognizer.energy_threshold))
            print("\nSpeak now:")
            audio = recognizer.listen(src)
            playsound('D:/VS Code Projects/Major_project/3kp.wav')
            speech_to_txt = recognizer.recognize_google(audio,language="en-in").lower()
            #speech_to_txt = recognizer.recognize_google_cloud(audio)
            #speech_recognition.WavFile("file.wav") as src:
        except Exception as ex:
            print("Sorry. I Could not understand.\n\n")
            tts_engine.say("Sorry! I Could not understand.")
            tts_engine.runAndWait()
            time.sleep(0.3)
            continue

        print("I heard : " + speech_to_txt)

        #---------------------------------------------------------------------
        # The following if-else block is for the commands I have chosen and 
        # call their respective GUI action
        #---------------------------------------------------------------------
        if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
            tts_engine.say("Okay, I'm Quitting now")
            tts_engine.runAndWait()
            break
        elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
            tts_engine.say("moving up")
            tts_engine.runAndWait()
            gui.mouse_up(recognizer, src)
        elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
            tts_engine.say("moving down")
            tts_engine.runAndWait()
            gui.mouse_down(recognizer, src)
        elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
            tts_engine.say("moving left")
            tts_engine.runAndWait()
            gui.mouse_left(recognizer,src)
        elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
            tts_engine.say("moving right")
            tts_engine.runAndWait()
            gui.mouse_right(recognizer,src)
        elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
            tts_engine.say("left clicking")
            tts_engine.runAndWait()
            gui.left_click()
        elif speech_to_txt == "right click" or speech_to_txt == "right-click":
            tts_engine.say("right clicking")
            tts_engine.runAndWait()
            gui.right_click()
        elif speech_to_txt == "double click" or speech_to_txt == "double-click":
            tts_engine.say("double clicking")
            tts_engine.runAndWait()
            gui.double_click()
        elif speech_to_txt == "open chrome":
            tts_engine.say("opening chrome")
            tts_engine.runAndWait()
            gui.open_chrome()
        #elif speech_to_txt == "open start menu":
        #    gui.start_menu()
        elif speech_to_txt == "mute" or speech_to_txt=="unmute":
            gui.mute_unmute()
        elif speech_to_txt == "play" or speech_to_txt=="pause":
            gui.play_pause()
        elif speech_to_txt == "volume up" or speech_to_txt=="sound up":
            tts_engine.say("turning volume up")
            tts_engine.runAndWait()
            gui.volume_up()
        elif speech_to_txt == "volume down" or speech_to_txt=="sound down":
            tts_engine.say("turning volume down")
            tts_engine.runAndWait()
            gui.volume_down()
        elif speech_to_txt =="voice input":
            tts_engine.say("Activating Windows Voice recognition")
            tts_engine.runAndWait()
            gui.voice_recognition()
        elif speech_to_txt == "refresh" or speech_to_txt == "f5":
            tts_engine.say("refreshing")
            tts_engine.runAndWait()
            gui.f5()
        elif speech_to_txt == "press enter" or speech_to_txt == "enter":
            tts_engine.say("pressing enter key")
            tts_engine.runAndWait()
            gui.enter()
        elif speech_to_txt =="press backspace" or speech_to_txt == "press back space":
            tts_engine.say("pressing backspace key")
            tts_engine.runAndWait()
            gui.backspace()
        elif speech_to_txt =="press escape":
            tts_engine.say("pressing escape key")
            tts_engine.runAndWait()
            gui.esc()
        elif speech_to_txt =="press delete":
            tts_engine.say("pressing delete key")
            tts_engine.runAndWait()
            gui.delete()
        elif speech_to_txt =="press windows":
            tts_engine.say("pressing windows key")
            tts_engine.runAndWait()
            gui.windows()
        elif speech_to_txt=="press left arrow":
            tts_engine.say('pressing left arrow key')
            tts_engine.runAndWait()
            gui.left_arrow()
        elif speech_to_txt=="press right arrow":
            tts_engine.say('pressing right arrow key')
            tts_engine.runAndWait()
            gui.right_arrow()
        elif speech_to_txt=="press up arrow":
            tts_engine.say('pressing up arrow key')
            tts_engine.runAndWait()
            gui.up_arrow()
        elif speech_to_txt=="press down arrow":
            tts_engine.say('pressing down arrow key')
            tts_engine.runAndWait()
            gui.down_arrow()
        elif speech_to_txt== "take a screenshot" or speech_to_txt=="take a screen shot" or speech_to_txt=="screenshot":
            tts_engine.say("Okay, I wiil take a screenshot for you.")
            tts_engine.runAndWait()
            gui.screenshot()
        elif speech_to_txt =="press page down" or speech_to_txt=="press pagedown":
            tts_engine.say("pressing page-down key")
            tts_engine.runAndWait()
            gui.page_down()
        elif speech_to_txt=="press page up" or speech_to_txt=="press pageup":
            tts_engine.say("pressing page-up key")
            tts_engine.runAndWait()
            gui.page_up()
        elif speech_to_txt=="press caps lock":
            tts_engine.say("pressing capslock key")
            tts_engine.runAndWait()
            gui.caps_lock()
        elif speech_to_txt =="press numlock":
            tts_engine.say("pressing numlock key")
            tts_engine.runAndWait()
            gui.num_lock()
        elif speech_to_txt =="press 1":
            tts_engine.say("pressing 1")
            tts_engine.runAndWait()
            gui.num1()
        elif speech_to_txt =="press 2":
            tts_engine.say("pressing 2")
            tts_engine.runAndWait()
            gui.num2()
        elif speech_to_txt =="press 3":
            tts_engine.say("pressing 3")
            tts_engine.runAndWait()
            gui.num3()
        elif speech_to_txt =="press 4":
            tts_engine.say("pressing 4")
            tts_engine.runAndWait()
            gui.num4()
        elif speech_to_txt =="press 5":
            tts_engine.say("pressing 5")
            tts_engine.runAndWait()
            gui.num5()
        elif speech_to_txt =="press 6":
            tts_engine.say("pressing 6")
            tts_engine.runAndWait()
            gui.num6()
        elif speech_to_txt =="press 7":
            tts_engine.say("pressing 7")
            tts_engine.runAndWait()
            gui.num7()
        elif speech_to_txt =="press 8":
            tts_engine.say("pressing 8")
            tts_engine.runAndWait()
            gui.num8()
        elif speech_to_txt =="press 9":
            tts_engine.say("pressing 9")
            tts_engine.runAndWait()
            gui.num9()
        elif speech_to_txt =="press 0":
            tts_engine.say("pressing 0")
            tts_engine.runAndWait()
            gui.num0()
        elif speech_to_txt=="plus":
            tts_engine.say("pressing plus key")
            tts_engine.runAndWait()
            gui.plus()
        elif speech_to_txt=="divide":
            tts_engine.say("pressing divide key")
            tts_engine.runAndWait()
            gui.divide()
        elif speech_to_txt=="multiply":
            tts_engine.say("pressing multiply key")
            tts_engine.runAndWait()
            gui.multiply()
        elif speech_to_txt=="minus":
            tts_engine.say("pressing minus key")
            tts_engine.runAndWait()
            gui.minus()
        elif speech_to_txt =="shutdown pc":
            print("\nDo you really want to shutdown your pc? ")
            tts_engine.say("Do you really want to shutdown your pc?")
            tts_engine.runAndWait()
            try:
                audio = recognizer.adjust_for_ambient_noise(src)
                playsound('D:/VS Code Projects/Major_project/2yT.wav')
                audio = recognizer.listen(src)
                playsound('D:/VS Code Projects/Major_project/3kp.wav')
                speech_to_txt = recognizer.recognize_google(audio,language="en-in").lower()
            except:
                print("Sorry! I didn't get you")
                tts_engine.say("Sorry! I didn't get you")
                tts_engine.runAndWait()
            if speech_to_txt=="yes":
                tts_engine.say("Shutting down your pc")
                tts_engine.runAndWait()
                gui.shutdown()
tts_engine.stop()