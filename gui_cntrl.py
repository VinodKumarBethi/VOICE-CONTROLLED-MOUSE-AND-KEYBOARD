from time import sleep
import pyautogui
import os
from playsound import playsound
# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER=200
SLOWER=20

class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer UPWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------
    def mouse_up(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            try:
                playsound('D:/VS Code Projects/Major_project/2yT.wav')
                audio = recognizer.listen(src)
                playsound('D:/VS Code Projects/Major_project/3kp.wav')
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse up :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer DOWNWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------        
    def mouse_down(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
            try:
                playsound('D:/VS Code Projects/Major_project/2yT.wav')
                audio = recognizer.listen(src)
                playsound('D:/VS Code Projects/Major_project/3kp.wav')
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse down :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer LEFTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_left(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
            try:
                playsound('D:/VS Code Projects/Major_project/2yT.wav')
                audio = recognizer.listen(src)
                playsound('D:/VS Code Projects/Major_project/3kp.wav')
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse left :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer RIGHTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_right(self,recognizer, src):
        #print("Move mouse right")
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
            try:
                playsound('D:/VS Code Projects/Major_project/2yT.wav')
                audio = recognizer.listen(src)
                playsound('D:/VS Code Projects/Major_project/3kp.wav')
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse right :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
    #------------------------------------------------------------------------------------
    # CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------    
    def left_click(self):
        pyautogui.click()
    #------------------------------------------------------------------------------------
    # CLICKS the RIGHT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def right_click(self):
        print("Right Clicking")
        pyautogui.click(button='right', clicks=2, interval=0.25)
    #------------------------------------------------------------------------------------
    # DOUBLE CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def double_click(self):
        print("Double Clicking")
        pyautogui.click(button='left', clicks=2, interval=0.25)
    #------------------------------------------------------------------------------------
    # CLICKS the CHROME icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the 
    # program is run.
    #------------------------------------------------------------------------------------       
    def open_chrome(self):
        print("Opening Chrome")
        icon_location = pyautogui.locateOnScreen(r'D:/VS Code Projects/Major_project/chrome-icon.png', confidence=0.9)
        #print(type(icon_location))
        if icon_location is not None:
            if len(icon_location) == 4:
                #Box(left=446, top=1023, width=74, height=52)
                #Calculate point x,y position to click based on above location
                #pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate Chrome Icon on screen")

    #------------------------------------------------------------------------------------
    # CLICKS the NOTEPAD icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the 
    # program is run.
    #------------------------------------------------------------------------------------           
    def start_menu(self):
        print("Opening Start Menu")
        icon_location = pyautogui.locateOnScreen(r'D:/VS Code Projects/Major_project/Start.png')
        if icon_location is not None:
            if len(icon_location) == 4:
                #Box(left=446, top=1023, width=74, height=52)
                #Calculate point x,y position to click based on above location
                #pyautogui.moveTo(icon_location.left, icon_location.top, duration=0.25)
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
        else:
            print("Could not locate START MENU Icon on screen")
    #------------------------------------------------------------------------------------
    # Simulates the MUTE/UNMUTE key press
    #------------------------------------------------------------------------------------ 
    def mute_unmute(self):
        print("Pressing Mute/Unmute Key")
        pyautogui.typewrite(['volumemute'])
    #------------------------------------------------------------------------------------
    # Simulates the SPACE key press
    #------------------------------------------------------------------------------------ 
    def play_pause(self):
        print("Pressing SPACE Key")
        pyautogui.typewrite(['space'])
    #------------------------------------------------------------------------------------
    # Simulates the VOLUME UP key press
    #------------------------------------------------------------------------------------       
    def volume_up(self):
        pyautogui.typewrite(['volumeup'])
    #------------------------------------------------------------------------------------
    # Simulates the VOLUME DOWN key press
    #------------------------------------------------------------------------------------ 
    def volume_down(self):
        pyautogui.typewrite(['volumedown'])
    #------------------------------------------------------------------------------------
    # Simulates the KEYBOARD keys press
    #------------------------------------------------------------------------------------ 
    def voice_recognition(self):
        pyautogui.hotkey('win','h')
        sleep(20)
        pyautogui.hotkey('win','h')
    def shutdown(self):
        os.system("shutdown /s /t 1")
    def enter(self):
        pyautogui.typewrite(['enter'])
        print("Pressed ENTER key\n")
    def delete(self):
        pyautogui.typewrite(['delete'])
        print("Pressed DELETE key\n")
    def f5(self):
        pyautogui.typewrite(['f5'])
        print("Pressed F5 key\n")
    def esc(self):
        pyautogui.typewrite(['esc'])
        print("Pressed Esc key\n")
    def backspace(self):
        pyautogui.typewrite(['backspace'])
    def windows(self):
        pyautogui.typewrite(['win'])
    def screenshot(self):
        pyautogui.hotkey('win','prtscr')
    def page_up(self):
        pyautogui.press('pgup')
    def page_down(self):
        pyautogui.press('pgdn')
    def caps_lock(self):
        pyautogui.press('capslock')
    def num_lock(self):
        pyautogui.press('numlock')
    def num1(self):
        pyautogui.press('num1')
    def num2(self):
        pyautogui.press('num2')
    def num3(self):
        pyautogui.press('num3')
    def num4(self):
        pyautogui.press('num4')
    def num5(self):
        pyautogui.press('num5')
    def num6(self):
        pyautogui.press('num6')
    def num7(self):
        pyautogui.press('num7')
    def num8(self):
        pyautogui.press('num8')
    def num9(self):
        pyautogui.press('num9')
    def num0(self):
        pyautogui.press('num0')
    def plus(self):
        pyautogui.press('+')
    def divide(self):
        pyautogui.press('/')
    def multiply(self):
        pyautogui.press('*')
    def minus(self):
        pyautogui.press('-')
    def left_arrow(self):
        pyautogui.press('left')
    def down_arrow(self):
        pyautogui.press('down')
    def right_arrow(self):
        pyautogui.press('right')
    def up_arrow(self):
        pyautogui.press('up')
    def sleep(self):
        pyautogui.press('sleep')