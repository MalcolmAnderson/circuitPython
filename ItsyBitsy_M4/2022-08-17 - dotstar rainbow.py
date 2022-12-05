import board
import time
from rainbowio import colorwheel
import adafruit_dotstar
pixel = adafruit_dotstar.DotStar(board.DOTSTAR_CLOCK, board.DOTSTAR_DATA, 1, brightness=1)
while True:
    pixel.fill(colorwheel(time.monotonic() * 100))# Write your code here :-)
