import board, neopixel, time

# pixel assignment
leftPanel_elements = ((0,7), (24,31), (32,39), (56,63))
#left_panel = neopixels.create_panel_list(leftPanel_elements)
rightPanel_elements = ((8,15), (16,23), (40,47), (48,55))
#right_panel = neopixels.create_panel_list(rightPanel_elements)

pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.2, auto_write=True, pixel_order=neopixel.RGBW)

if __name__ == '__main__':
    pixels[leftPanel_elements] = (255, 0,0,0)

    time.sleep(30)

