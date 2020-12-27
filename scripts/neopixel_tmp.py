import board
import neopixel

# global variables
digital_pin = board.D18  # digital pin on rpi
led_count = 8

def main():
    pixels = neopixel.NeoPixel(digital_pin, led_count)


if __name__ == '__main__':
    main()