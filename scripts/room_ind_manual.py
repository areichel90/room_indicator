import numpy as np
import time, neopixel, board, argparse
import neopixel_tmp as neopixels

# global variables
max_brightness = 10  # percent
fade_in_speed = 0.5  # second
fade_out_speed = 0.5  # second

# pixel assignment
leftPanel_elements = ((0,7), (16,23), (23,39), (48,55))
left_panel = neopixels.create_panel_list(leftPanel_elements)
rightPanel_elements = ((8,15), (24,31), (40,47), (56, 63))
right_panel = neopixels.create_panel_list(rightPanel_elements)

def calc_dwell(speed, smoothness):
    requested = 1/(speed * smoothness)
    #if requested < 0.0025
    return requested

def fade_in(pixels, speed=1.0, fade_smoothness=200, sustain=None):
    # calculate dwell from speed
    dwell = calc_dwell(speed=speed, smoothness=fade_smoothness)

    for b in np.linspace(0, max_brightness, fade_smoothness):
        #print(b)
        pixels.brightness = b/100
        pixels.show()
        time.sleep(dwell)


def fade_out(pixels, speed=1.0, fade_smoothness=200, sustain=None):
    # calculate dwell from speed
    dwell = calc_dwell(speed=speed, smoothness=fade_smoothness)
    print(pixels)
    for b in np.linspace(max_brightness, 0, fade_smoothness):
        #print(b)
        pixels.brightness = b/100
        pixels.show()
        time.sleep(dwell)


def show_as(pixles, color=(0,0,0,255), fade_time=0.5, use_pixels=left_panel):
    fade_out(pixels)

    #pixels.fill((0,0,0,0))

    for i in use_pixels:
        pixels[i]=color
    fade_in(pixels, speed=fade_time, fade_smoothness=100)
    #pixels.show()
    #print(pixels)

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
        show_as(pixels, color=color, use_pixels=left_panel)
    elif args.free:
        color=(0,0,0,255)
        rand_color = neopixels.generate_random_color()
        show_as(pixels, color=color,  use_pixels=right_panel)
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
