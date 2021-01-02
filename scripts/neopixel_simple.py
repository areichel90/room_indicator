import board, neopixel

pixels = neopixel.NeoPixel(board.D18, 8)

if __name__ == '__main__':
    pixels[0] = (255, 0, 0)