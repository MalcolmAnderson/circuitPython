# neXt Actions (XA) Integrate code changes from MorseCodeClass.py

# URL of circuit
# Combination of https://learn.adafruit.com/micropython-hardware-analog-i-o/pulse-width-modulation
# and https://wokwi.com/projects/309474946192507458

# Circuit Description on Itsy Bitsy M4 Express
# Wire from ground to resistor
# resistor to short side of LED
# long side of LED to D5

# Morse Code Wiki - https://en.wikipedia.org/wiki/Morse_code
# CircuitPython Blink Example

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT

handicap = 1
unit = .1 * handicap
dot_length = unit
dash_length = 3 * unit
in_letter_space = unit
between_letter_space = 3 * unit
between_word_space = 7 * unit



def pulse(state, seconds):
    #if state:
    #    print("on")
    #else:
    #    print("off")
    led.value = state
    time.sleep(seconds)

def pause(seconds):
    pulse(False, seconds)

def blink(times, on, off):
    for i in range(0, times):
        pulse(True, on)
        pulse(False, off)

def mLetter(code):
    for c in code:
        #print(c)
        if(c=='.'):
            pulse(True, dot_length)
            pulse(False, in_letter_space)
        if(c=='-'):
            pulse(True, dash_length)
            pulse(False, in_letter_space)
    pulse(False, between_letter_space)

def mWord(word):
    for c in word:
        print(c)
        if c == 'i' or c == 'I':
            mLetter("..")
        if c == " ":
            pulse(False, 2)
        if c == 'l' or c == 'L':
            mLetter(".-..")
        if c == 'o' or c == 'O':
            mLetter("---")
        if c == 'v' or c == 'V':
            mLetter("...-")
        if c == 'e' or c == 'E':
            mLetter(".")
        if c == 'y' or c == 'Y':
            mLetter("-.--")
        if c == 'u' or c == 'U':
            mLetter("..-")
        if c == 's' or c == 'S':
            mLetter("...")
    pulse(False, between_word_space)

while True:
    #pulse(True, .1)
    #pulse(False, 1.9)
#    for i in range(0, 13):
 # print(i)

#  blink(i, .1, .5)
 #       pause(3)
    mWord("I love you")
#    mLetter("...")
#    mLetter("---")
#    mLetter("...")
    pulse(False, 3)
