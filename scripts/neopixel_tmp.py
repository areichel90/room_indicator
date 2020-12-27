#import board
import neopixel

# global variables
digital_pin = 18
led_count = 8

def main():
    pixels = neopixel.NeoPixel(f"board.D{digital_pin}", led_count)
    

if __name__ == '__main__':
    main()