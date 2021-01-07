import time, neopixel, board, argparse
import neopixel_tmp as neopixels

# global variables
busy_range = (0,8)
busy_pixels = list(range(busy_range[0],busy_range[1]))
free_range = (8,16)
free_pixels = range(free_range[0], free_range[1])

def show_as(pixles, color=(0,0,0,255), use_pixels=busy_pixels):
    #turn off all pixels
    pixels.fill((0,0,0,0))
    for i in use_pixels:
        pixels[i]=color
    pixels.show()

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true')
    parser.add_argument("-m", "--in_meeting", help='boolean "in meeting" status', action='store_true', required=False)
    parser.add_argument("-f", "--free", help='boolean status for "not in meeting"', action='store_true', required=False)
    args = parser.parse_args()

    if args.verbose:print(f'\nin meeting: {args.in_meeting}\tfree: {args.free}')

    # initialize neopixel setup
    if args.verbose: print(f'\nInitializing Neopixels...')
    pixels = neopixels.initialize_neopixels()
    # turn off pixels
    #neopixels.solid_color(pixels)


    # generate random color
    color = neopixels.generate_random_color()
    # flash all elements
    #neopixels.pixel_flash(pixels=pixels, rgbw = color, 
    #                      rate=5, verbose=args.verbose)
    if args.in_meeting:
        color = (0,0,0,255)
        rand_color = neopixels.generate_random_color()
        show_as(pixels, color=color, use_pixels=busy_pixels)
    elif args.free:
        color=(0,0,0,255)
        rand_color = neopixels.generate_random_color()
        show_as(pixels, color=color, use_pixels=free_pixels)
    else:
        # light one panel at a time
        dwell = 1/2
        while True:
            # show as busy
            color = neopixels.generate_random_color()
            show_as(pixels, color=color, use_pixels=busy_pixels)
            time.sleep(dwell)
            pixels.fill((0,0,0,0))
            # show as free
            color = neopixels.generate_random_color()
            show_as(pixels, color=color, use_pixels=free_pixels)
            time.sleep(dwell)
            pixels.fill((0,0,0,0))
