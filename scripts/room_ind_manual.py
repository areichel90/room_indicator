import time, neopixel, board, argparse
import neopixel_tmp as neopixels

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--in_meeting", help='boolean "in meeting" status', action='store_true', optional=True)
    parser.add_argument("-f", "--free", help='boolean status for "not in meeting"', action='store_true', optional=True)
    parser.parse_args()

    # initialize neopixel setup
    pixels = neopixels.initialize_neopixels()

    # generate random color
    color = neopixels.generate_random_color()
    # flash all elements
    neopixels.pixel_flash(pixels=pixels, rgbw = color, verbose=True)



