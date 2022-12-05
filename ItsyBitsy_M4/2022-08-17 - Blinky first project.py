
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

on_seconds = .5
off_seconds = 5.5
cycle_count = -1
str_cycle_count = ""
TenCycleSeconds = on_seconds * 10 + off_seconds * 10
TenCycleMessage = "Cycle count is 10 counts every " + str(TenCycleSeconds) + "seconds"
# print(TenCycleMessage)

while True:
    cycle_count = cycle_count + 1
    if cycle_count % 10 == 0:#
        print(TenCycleMessage)
    print()

    str_cycle_count = str(cycle_count)
    led.value = True
    line1 = "cycle "+ str_cycle_count +": on:  " + str(on_seconds) + " seconds"
    print(line1)
    time.sleep(on_seconds)
    led.value = False
    line2 = "cycle "+ str_cycle_count +": off: " + str(off_seconds) + " seconds."
    print(line2)
    time.sleep(off_seconds)
