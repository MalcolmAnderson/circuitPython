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
#import board
#import digitalio

#led = digitalio.DigitalInOut(board.D5)
#led.direction = digitalio.Direction.OUTPUT

handicap = 1
unit = .1 * handicap
dot_length = unit
dash_length = 3 * unit
in_letter_space = unit
between_letter_space = 3 * unit
between_word_space = 7 * unit

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

totaltime = 0


def pulse(state, seconds):
    global totaltime
    #if state:
    #    print("on")
    #else:
    #    print("off")
       
    #led.value = state
    #time.sleep(seconds)
    totaltime += seconds

    pass

def pause(seconds):
    pulse(False, seconds)

def blink(times, on, off):
    for i in range(0, times):
        pulse(True, on)
        pulse(False, off)

def mLetter(code):
    print(code)
    code_len = len(code)
    for i in range(0, code_len):
        #print(f"i = {i}, len(code) = {len(code)}")
        c = code[i]
        if(c=='.'):
            pulse(True, dot_length)
        if(c=='-'):
            pulse(True, dash_length)
    if i < code_len - 1:
        pulse(False, in_letter_space)

def mWord(word):
    print(word)
    word_len = len(word)
    for i in range(0, word_len):
        c = word[i].upper()
        code = MORSE_CODE_DICT[c.upper()]
        print(c)
        print(code)
        if c == 'i' or c == 'I':
            mLetter("..")
        if c == " ":
            pulse(False, between_word_space)
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
    if i < word_len - 1:
        pulse(False, between_word_space)

#mWord("I love you")
# pulse(False, 3)
print(f"totaltime = {totaltime}")
mWord("s")
print(f"totaltime = {totaltime}")
