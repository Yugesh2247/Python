import pyautogui 
import time
time.sleep(4)
#input=input("enter how many time to send")
count=0
while count<=50:

    pyautogui.typewrite("phone tesava Basha?")
    pyautogui.press('enter')
    count+=1
    
    

