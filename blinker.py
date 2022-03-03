import RPi.GPIO as GPIO

import time

from tkinter import *

CODES = { 'A':'.-', 'B':'-...','C':'-.-.',
          'D':'-..', 'E':'.','F':'..-.',
          'G':'--.', 'H':'....','I':'..',
          'J':'.---', 'K':'-.-','L':'.-..',
          'M':'--', 'N':'-.','O':'---',
          'P':'.--.', 'Q':'--.-','R':'.-.',
          'S':'...', 'T':'-','U':'..-',
          'V':'...-', 'W':'.--','X':'-..-',
          'Y':'-.--', 'Z':'--..'}



master = Tk()
master.geometry("175x175")


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)

v = StringVar(master, "1")

def flash(inputMorse):
    for char in inputMorse:
        if(char == '.'):
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(12, GPIO.LOW)
            time.sleep(0.25)
        elif(char == '-'):
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.75)
            GPIO.output(12, GPIO.LOW)
            time.sleep(0.25)
        elif(char == ' '):
            GPIO.output(12, GPIO.LOW)
            time.sleep(0.75)
            
def convertToMorse(inputString):
    output = ''
    for char in inputString:
        output += CODES[char.upper()]
        output += ' '
    return output

def end():
    master.quit()
    master.destroy
    GPIO.cleanup()
    exit()
    

def morse():
    if (len(entry.get()) > 12):
        print("Please only enter 12 Characters, you have entered: " + str(len(entry.get())))
    else:
        morseCode = convertToMorse(entry.get())
        print(morseCode)
        flash(morseCode)


Label(master, text="Enter a string \n(up to 12 char):",
         justify = LEFT,
         padx = 20).pack()
entry = Entry(master)
entry.pack()

Button(master, text="Send Command", command = morse).pack()
Button(master, text="Exit Program", command = end).pack()


mainloop()
