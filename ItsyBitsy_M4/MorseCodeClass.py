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



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', 
                    '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
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
        elif(c=='-'):
            pulse(True, dash_length)
        if i < code_len - 1:
            pulse(False, in_letter_space)

""" Validation code, takes a dot and a dash"""
def getCodeDuration(code):
    duration = 0
    code_len = len(code)
    for i in range(0, code_len):
        c = code[i]
        if c == '.' :
            duration += dot_length
        elif c == '-':
            duration += dash_length
        else:
            raise ValueError("getCodeDuration only accepts dots '.' or dashes '-'")
        if i < code_len - 1:
            duration += in_letter_space
    return duration

""" Validation code to insure that between letter and between words are correct"""
def durationOfMessage(word):
    unitCount = 0
    word_len = len(word)
    for i in range(0, word_len):
        c = word[i]
        if c == " ":
            print(between_word_space)
        else:
            code = MORSE_CODE_DICT[c.upper()]
            print(getCodeDuration(code))
            if i == word_len - 1:
                break
            elif i < word_len - 1 and word[i + 1] != " ":
                print(between_letter_space)
    return unitCount

""" Should be called mMessage"""
def mWord(word):
    print(word)
    word_len = len(word)
    for i in range(0, word_len):
        c = word[i]
        if c == " ":
            pulse(False, between_word_space)
        else:
            mLetter(MORSE_CODE_DICT[c.upper()])
            if i == word_len - 1:
                break
            elif i < word_len - 1 and word[i+1] != " ":
                pulse(False, between_letter_space)

#mWord("I love you")
# pulse(False, 3)
print(f"totaltime = {totaltime}")
# code_dur = getCodeDuration("...")
# print(code_dur)
print(durationOfMessage("eee e"))
mWord("eee e")
print(f"totaltime = {totaltime}")
