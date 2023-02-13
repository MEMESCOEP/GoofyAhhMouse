### [== GoofyAhhMouse ==] ###
## ANSI Color codes: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007 ##
# Print init message
print("Initializing...")

# IMPORTS #
from screeninfo import get_monitors
from datetime import datetime
import pyautogui
import keyboard
import random
import psutil
import time
import sys
import os

# VARIABLES #
MonitorNumber = 0
MouseIncrement = 20
ScreenWidth = get_monitors()[MonitorNumber].width
ScreenHeight = get_monitors()[MonitorNumber].height
InIdle = ('idlelib.run' in sys.modules)
UpdateFreq = 3
UpdateCount = 0
Update = True

# FUCNTIONS #
# Clear the console
def ClearConsole():
    command = 'clear'

    # Check if the OS is Windows and change the command accordingly
    if os.name in ('nt', 'dos'):
        command = 'cls'

    # Run the console clear command
    os.system(command)

# Print program and usage information
def DisplayInformation():
    # Clear the console
    ClearConsole()

    # Print the program title
    print("\033[0;36m[== Goofy Ahh Mouse ==]\033[0;37m")

    # Display the help text
    print("- Press CTRL+ALT+F2 to \033[1;32;40mMOVE\033[0;37m the mouse to a random position")
    print("- Press CTRL+ALT+F3 to \033[1;32;40mDRAG\033[0;37m the mouse to a random position")
    print("- Press CTRL+ALT+F4 to \033[1;32;40mMOVE\033[0;37m the mouse to a random relative position")
    print("- Press CTRL+ALT+F5 to \033[1;32;40mDRAG\033[0;37m the mouse to a random relative position")
    print("- Press CTRL+ALT+F6 to \033[1;32;40mLEFT CLICK\033[0;37m")
    print("- Press CTRL+ALT+F7 to \033[1;32;40mRIGHT CLICK\033[0;37m")
    print("- Press CTRL+ALT+F8 to \033[1;32;40mTOGGLE\033[0;37m the update status")
    print("- Press CTRL+ALT+<ARROW KEY> to \033[1;32;40mMOVE\033[0;37m the mouse")
    print("- Press <SHIFT+ESC> to exit.\033[0;37m")

    # Print mouse and time information
    print("\n\033[0;36m[== INFORMATION ==]\033[0;37m")
    print("- Screen resolution (Monitor {0}): {1}x{2}".format(MonitorNumber, ScreenWidth, ScreenHeight))

# Toggle the update variable
def ToggleUpdate():
    global Update
    Update = not Update

# MAIN CODE #
# Disable pyautogui failsafes because they might interfere with the
# functionality of this script
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

# Add a hotkey for toggling the update variable
keyboard.add_hotkey("ctrl+alt+f8", ToggleUpdate)

# Check if we're running in the IDLE Shell
if InIdle:
    print("[WARNING] >> Do not use this program with the IDLE Shell.\nThe ANSI escape codes DO NOT WORK! They break colors and print garbage!")
    inp = input("Do you want to continue? (Y/N) >> ")
    if inp != "Y" and inp != "y":
        sys.exit(-3)

    else:
        print("\n\n\n")

# Print program and usage information
DisplayInformation()

# Do teh funni 🗿💀
while True:
    try:
        # Handle input                
        # Move (F2)
        if keyboard.is_pressed("ctrl+alt+f2"):
                pyautogui.moveTo(random.randint(0, ScreenWidth), random.randint(0, ScreenHeight))

        # Move relative (F3)
        if keyboard.is_pressed("ctrl+alt+f3"):
                pyautogui.dragTo(random.randint(0, ScreenWidth), random.randint(0, ScreenHeight))

        # Drag (F4)
        if keyboard.is_pressed("ctrl+alt+f4"):
                pyautogui.move(random.randint(-MouseIncrement, MouseIncrement), random.randint(-MouseIncrement, MouseIncrement))

        # Drag relative (F5)
        if keyboard.is_pressed("ctrl+alt+f5"):
                pyautogui.drag(random.randint(-MouseIncrement, MouseIncrement), random.randint(-MouseIncrement, MouseIncrement))

        # Click (F6)
        if keyboard.is_pressed("ctrl+alt+f6"):
                pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

        # Right click (F7)
        if keyboard.is_pressed("ctrl+alt+f7"):
                pyautogui.click(pyautogui.position()[0], pyautogui.position()[1], button='right')
                
        # Arrow key mouse movement
        if MouseIncrement != 0:
            if keyboard.is_pressed("ctrl+alt+up"):
                    pyautogui.move(0, -MouseIncrement)

            if keyboard.is_pressed("ctrl+alt+down"):
                    pyautogui.move(0, MouseIncrement)

            if keyboard.is_pressed("ctrl+alt+left"):
                    pyautogui.move(-MouseIncrement, 0)

            if keyboard.is_pressed("ctrl+alt+right"):
                    pyautogui.move(MouseIncrement, 0)

        # If the exit key combo is pressed, quit
        if(keyboard.is_pressed("shift+esc")):
                ClearConsole()
                sys.exit(295) # Exit with code 295 in case some program wants to know if the user manually closed the program

        # Print information if we're not in the IDLE shell
        # Use '\033[<N>A' to move the cursor up one line if printing more information, where <N> is the number of lines
        # '\033[A' can be used for moving the cursor up one line
        if not InIdle and UpdateCount >= UpdateFreq and Update:
            print("- Mouse position: [X=\033[1;33m{0}\033[0;37m Y=\033[1;33m{1}\033[0;37m]     ".format(pyautogui.position()[0], pyautogui.position()[1]), end='\r')
            UpdateCount = 0

        elif not Update and UpdateCount % 5 == 0:
            print("- Mouse position: \033[0;31m[NOT UPDATING]\033[0;37m                                 ", end='\r')

        # Pause for 1 millisecond to prevent high CPU usage
        time.sleep(0.01)

        # Increment the update count variable
        UpdateCount = UpdateCount + 1
        
    except Exception as ex:
        ErrCode = ex.args
        print("\n\n\n\n[ERROR] >> {0}".format(ex))
        sys.exit(-1)
