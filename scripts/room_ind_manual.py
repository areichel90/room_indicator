import time, neopixel, board, argparse
import neopixel_tmp as neopixels

# global variables
busy_pixels = [0,7]
free_pixels = [8,15]

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true')
    parser.add_argument("-m", "--in_meeting", help='boolean "in meeting" status', action='store_true', required=False)
    parser.add_argument("-f", "--free", help='boolean status for "not in meeting"', action='store_true', required=False)
    args = parser.parse_args()

    if args.verbose:print(f'\nin meeting: {args.in_meeting}\tfree: {args.free}')

    # initialize neopixel setup
    if verbose: print(f'\nInitializing Neopixels...')
    pixels = neopixels.initialize_neopixels()

    # generate random color
    color = neopixels.generate_random_color()
    # flash all elements
    neopixels.pixel_flash(pixels=pixels, rgbw = color, verbose=args.verbose)

    pixels[0] = (0,0,0,255)
    pixles.show()

