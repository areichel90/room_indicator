import board, neopixel, time

pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.2, auto_write=True, pixel_order=neopixel.RGBW)

if __name__ == '__main__':
    pixels[0] = (0,0,0,0)
    exit()
