
import numpy as np
import board, neopixel, time
from random import randrange


# global variables
digital_pin = board.D18  # digital pin on rpi
pixel_count = 8*8
order = neopixel.GRBW

# misc
max_brightness = 30  # percent
colors = [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (0, 0, 0, 255)]

def main(pixels):
    # flash all elements 
    i = 0
    dwell = 1.0/8  # seconds

    # countdown
    start = 5
    for j in range(start):
        print(f'{start-j}...')
        time.sleep(1)

    #print('Starting Flashing Sequence')
    while i <= 2:
        # turn led's on
        solid_color(rgbw=[0,0,0,255], sustain=dwell, pixels=pixels)
        # turn led's off
        solid_color(sustain=dwell, pixels = pixels)
        i += 1

    # single element scrolling sequence
    a=0
    while a <= 3:
        for color in colors:
            scrolling_color(pixels, rgbw=color, speed = 0.5)
            a+=1

    # breathing color
    while True:
        # rgbw = (0,0,0,255)
        rand_color = generate_random_color()
        #print(f'rgbw (final): {rand_color}')
        breathing_color(pixels, rgbw=rand_color, speed=0.5, fade_smoothness=100, verbose=False)
        # clear random color value from memory
        del rand_color

def create_panel_list(panel_elements, verbose=False):
    '''
    function to create list of all elements in each display panel
    '''
    return_panel = []
    for tup in panel_elements:
        for i in np.linspace(tup[0], tup[1], 8):
            return_panel.append(int(i))
    if verbose: print(f"\npanel pixels: {return_panel}")
    return return_panel

def initialize_neopixels(digital_pin = digital_pin, pixel_count = pixel_count, 
                            brightness=max_brightness, auto_write=False, pixel_order = order):
    pixels = neopixel.NeoPixel(
        digital_pin, 
        pixel_count, 
        brightness=brightness,
        auto_write=auto_write,
        pixel_order=pixel_order)
    return pixels

def generate_random_color(verbose=False):
    # randomly determine how many rgb values to omit
    omit_count = randrange(3)
    if verbose: print(f'\nto omit: {omit_count}')

    # generate 1d array of random RGBW values
    rgbw = np.random.rand(1,4)*(255*1)
    rgbw = rgbw[0].tolist()
    rgbw = np.around(rgbw)
    rgbw = rgbw.astype(int)
    if verbose: print(f'rgbw (raw): {rgbw}')   
    # mask random values
    count = 0
    while count < omit_count:
        for c,i in enumerate(rgbw):
            mask = np.random.randint(2,size=1)
            if mask == 1 and count < omit_count:
                rgbw[c] = 0
                count += 1
            else:
                continue
    # mask W value
    rgbw[3] = 0

    return rgbw

def pixel_flash(pixels, rgbw=(0,0,0,255), count=3, rate=3, verbose=False):
    '''
    pixels: initialized neopixels
    rgbw: color to be displayed
    count: count of flashes to be displayed
    rate: rate of all flashes (cycles per second)
    '''
    if verbose: print(f'Starting Flashing Sequence:')
    # calculate dwell from 'rate'
    dwell = (1./rate)/2
    if verbose: print(f'rate: {rate}\tdwell: {dwell}') 

    i=0
    while i < count:
        # turn led's on
        solid_color(rgbw=rgbw, sustain=dwell, pixels=pixels)
        # turn led's off
        solid_color(sustain=dwell, pixels = pixels)
        i += 1

def scrolling_color(pixels, rgbw=[0,0,0,0], speed=3.0, pixel_count=pixel_count, verbose=True):
    '''
    Function to scroll color through each pixel one element at a time (no fade)
    '''
    # calculate dwell from speed
    num_elements = (pixel_count*2) - 1 
    dwell = 1/(speed * num_elements)
    if verbose: print(f'speed: {speed}\tdwell: {dwell}')

    # light up each pixel one, at a time
    print('Starting Scrolling Sequence')
    for i in range(pixel_count):
        #print(f'pixel: {i}')
        # turn pixel on
        pixels[i] = rgbw
        pixels.show()
        time.sleep(dwell)
        # turn pixel off
        pixels[i] = (0, 0, 0, 0)
        #time.sleep(dwell)
    for i in range(1,pixel_count-1):
        i = (pixel_count-1)-i
        #print(f'pixels: {i}')
        pixels[i]= rgbw
        pixels.show()
        time.sleep(dwell)
        pixels[i]=(0,0,0,0)

def breathing_color(pixels, rgbw=(0,0,0,255), speed=1.0, fade_smoothness=200, sustain=None, verbose=True):
    '''
    '''
    # calculate dwell from speed
    num_elements = (pixel_count*2) - 1 
    dwell = 1/(speed * fade_smoothness*2)
    if verbose: print(f'color: {rgbw}\tspeed: {speed}\tdwell: {dwell}')
    if verbose: print(f'color: {rgbw}\tspeed: {speed}\tdwell: {dwell}')

    for b in np.linspace(0,max_brightness,fade_smoothness):
        if verbose: print(f'brightness: {b}')
        pixels.brightness = b/100
        pixels.fill(rgbw)
        pixels.show()
        time.sleep(dwell)
    for b in np.linspace(0,max_brightness,fade_smoothness):
        b = (max_brightness-1) - b
        if verbose: print(f'brightness: {b}')
        pixels.brightness = b/100
        pixels.fill(rgbw)
        pixels.show()
        time.sleep(dwell)


def solid_color(pixels, rgbw=[0,0,0,0], sustain=None, verbose=True):
    '''
    Function to write RGBW values to neopixel given 4 value array and sustain time (in seconds)
    '''
    # set values
    if sustain == None:
        sustain = 10 * 60  # n * 60sec = n minutes

    # write values to LEDs
    pixels.fill((rgbw[0], rgbw[1], rgbw[2], rgbw[3]))
    pixels.show()
    if sustain != None:  time.sleep(sustain)

if __name__ == '__main__':
    print('Starting NeoPixel Test Script!')

    # initialize neopixel configuration
    pixels = initialize_neopixels()

    # run main function
    main(pixels=pixels)

    print('\nTest Script Completed.')

