import board, neopixel, time

# global variables
digital_pin = board.D18  # digital pin on rpi
pixel_count = 8
order = neopixel.RGBW

# misc
colors = [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (0, 0, 0, 255)]

def main(pixels):
    # flash all elements 
    i = 0
    dwell = 1.0/8  # seconds

    '''# countdown
    for j in range(5):
        print(f'{5-j}...')
        time.sleep(1)'''

    print('Starting Flashing Sequence')
    while i <= 2:
        # turn led's on
        solid_color(rgbw=[0,0,0,255], sustain=dwell, pixels=pixels)
        # turn led's off
        solid_color(sustain=dwell, pixels = pixels)
        i += 1

    for color in colors:
        scrolling_color(pixels, rgbw=color, speed = 0.5)


def scrolling_color(pixels, rgbw=[0,0,0,0], speed=1.0, pixel_count=pixel_count, verbose=True):
    '''
    Function to scroll color through each pixel one element at a time (no fade)
    '''
    # calculate dwell from speed
    num_elements = (pixel_count*2) - 1 
    dwell = 1/(speed * num_elements)
    if verbose: print(f'speed: {speed}\tdwell: {dwell}')

    # light up each pixel one, at a time
    print('Starting Scrolling Sequence')
    while True:
        for i in range(pixel_count):
            #print(f'pixel: {i}')
            # turn pixel on
            pixels[i] = rgbw
            pixels.show()
            time.sleep(dwell)
            # turn pixel off
            pixels[i] = (0, 0, 0, 0)
            #time.sleep(dwell)
        for i in range(1,7):
            i = (pixel_count-1)-i
            #print(f'pixels: {i}')
            pixels[i]= rgbw
            pixels.show()
            time.sleep(dwell)
            pixels[i]=(0,0,0,0)

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
    time.sleep(sustain)

if __name__ == '__main__':
    print('Starting NeoPixel Test Script!')

    # setup neopixels
    pixels = neopixel.NeoPixel(
        digital_pin, 
        pixel_count, 
        brightness=0.2,
        auto_write=False,
        pixel_order=order)

    # run main function
    main(pixels=pixels)

    print('\nTest Script Completed.')
