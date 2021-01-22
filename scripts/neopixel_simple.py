import board, neopixel, time
import numpy as np 

# pixel assignment
leftPanel_elements = ((0,7), (24,31), (32,39), (56,63))
#left_panel = neopixels.create_panel_list(leftPanel_elements)
rightPanel_elements = ((8,15), (16,23), (40,47), (48,55))
#right_panel = neopixels.create_panel_list(rightPanel_elements)

def make_panel(vals_in):
    return_panel = []
    for tup in vals_in:
        for i in np.linspace(tup[0], tup[1], 8):
            return_panel.append(int(i))
    return return_panel

if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.D18, n=64, brightness=0.5, auto_write=True, pixel_order=neopixel.RGBW)
    print(make_panel(leftPanel_elements))
    for i in make_panel(leftPanel_elements):
        pixels[i] = (0,0,0,255)

    time.sleep(3)
    for i in make_panel(leftPanel_elements):
        pixels[i]= (0,0,0,0)


    for i in make_panel(rightPanel_elements):
        pixels[i] = (0,0,0,255)
   
    time.sleep(3)
    for i in make_panel(rightPanel_elements):
        pixels[i] = (0,0,0,0)
