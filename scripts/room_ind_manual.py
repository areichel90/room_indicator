import time, neopixel, board
import neopixel_tmp as neopixels

if __name__ == '__main__':
    # initialize neopixel setup
    pixels = neopixels.initialize_neopixels()

    # generate random color
    color = neopixels.generate_random_color()

    # flash all elements
    neopixels.pixel_flash(pixels=pixels, rgbw = color, verbose=True)

