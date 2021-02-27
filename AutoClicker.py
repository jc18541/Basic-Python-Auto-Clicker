import keyboard
import mouse
import sys

#Goes through 2 loops
##First helps to turn the program on and off
##Second is the actual clicker
while(True):
    #Turn the clicker on
    if keyboard.is_pressed('w'):
        while(True):
            mouse.click("left")
            #Quit the clicker
            if keyboard.is_pressed('q'):
                print("Exited Program")
                break
                break
                sys.exit()
            #Pause the clicker
            elif keyboard.is_pressed('e'):
                print("Clicker paused")
                break
#Go through while loop and 