import time, neopixel, board
import neopixel_tmp as neopixels

if __name__ == '__main__':
    # initialize neopixel setup
    neopixels.initialize_neopixels()

    # flash all elements
    neopixels.pixel_flash()