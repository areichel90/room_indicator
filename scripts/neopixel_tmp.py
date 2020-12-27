import board, neopixel, time

# global variables
digital_pin = board.D18  # digital pin on rpi
pixel_count = 8
order = neopixel.RGB

def main(pixels = pixels):
    # flash all elements 
    i = 0
    dwell = 0.25
    while i <= 3:
        # turn led's on
        solid_color(rgbw=[0,0,0,255], sustain=dwell)
        # turn led's off
        solid_color(sustain=dwell)
        i += 1


def solid_color(rgbw=[0,0,0,0], sustain=None, pixels = pixels, verbose=True):
    '''
    Function to write RGBW values to neopixel given 4 value array and sustain time (in seconds)
    '''
    # set values
    if sustain == None:
        sustain = 10 * 60  # n * 60sec = n minutes

    # write values to LEDs
    pixels.fill(rgbw[0], rgbw[1], rgbw[2], rgbw[3])
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