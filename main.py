import pyautogui as py
import time


print  ("█████╗ ██╗   ██╗████████╗ ██████╗  ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ ")
print ("██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
print ("███████║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝")
print ("██╔══██║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
print ("██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║")
print ("╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
print ("")                                                                                
print ("")
print ("1. start autoclicker")
print ("2. show help")
print ("3. exit")
op=int(input("choose an option: "))
if op==2:
    print ("This is a simple Python-based autoclicker.")
    print ("")
    print ("Features:")
    print ("1. Automatically clicks at the current mouse position.")
    print ("2. Easy-to-use menu for starting the autoclicker or viewing help.")
    print ("")
    print ("Instructions:")
    print ("- Run the script and choose an option from the menu.")
    print ("- To stop the autoclicker, close the programe.")
    time.sleep(10)
    exit()
elif op==3:
    exit()
elif op!=1:
    print("invalid option")
while True:
    # Get the current mouse position
    x, y = py.position()
    # Click at the current mouse position
    py.click(x, y)