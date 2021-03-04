import tkinter as tk
import time
import math
import random

def intersect(slist, sdot):
    ret_val = False

    for s in slist:
        dx = c.coords(s)[0] - c.coords(sdot)[0]
        dy = c.coords(s)[1] - c.coords(sdot)[1]
        d = dx*dx + dy*dy
        if d <= 4*R*R + 4:
            ret_val = True
            break

    return ret_val

def rotate(ox, oy, s, fi):
    x = (c.coords(s)[0] + c.coords(s)[2]) / 2 - ox
    y = (c.coords(s)[1] + c.coords(s)[3]) / 2 - oy
    _x = x * math.cos(fi) - y * math.sin(fi) + ox
    _y = x * math.sin(fi) + y * math.cos(fi) + oy
    return [_x, _y]
    
HEIGHT = 500
WIDTH = 500
RAND = 2
R = 1
SYM = 6

w = tk.Tk()
c = tk.Canvas(w, bg='black', height=HEIGHT, width=WIDTH)
c.pack()

dots = []

for i in range(200):
    x = WIDTH
    y = HEIGHT/2
    dot = c.create_oval(x - R, y - R, x + R, y + R, fill="white", outline="white")

    while c.coords(dot)[0] > WIDTH/2 and not intersect(dots, dot):
        d = random.randint(-RAND, RAND)
        if c.coords(dot)[1] + d < HEIGHT/2 - (math.tan(math.pi/SYM) * (c.coords(dot)[0] - WIDTH/2)):
            d = HEIGHT/2 - (math.tan(math.pi/6) * (c.coords(dot)[0] - WIDTH/2)) - c.coords(dot)[1]
        elif c.coords(dot)[1] + d > HEIGHT/2:
            d = HEIGHT/2 - c.coords(dot)[1]
        c.move(dot, -1, d)
        
        c.update()
        time.sleep(0.01)

    dots.append(dot)
    mirror_dot = c.create_oval(c.coords(dot)[0], HEIGHT - c.coords(dot)[1], c.coords(dot)[2], HEIGHT - c.coords(dot)[3], fill="white", outline="white")

    for j in range(SYM):
        sym_coords = rotate(WIDTH/2, HEIGHT/2, dot, j*math.pi*2/SYM)
        sym_dot = c.create_oval(sym_coords[0] - R, sym_coords[1] - R, sym_coords[0] + R, sym_coords[1] + R, fill="white", outline="white")

        sym_coords = rotate(WIDTH/2, HEIGHT/2, mirror_dot, j*math.pi*2/SYM)
        sym_dot = c.create_oval(sym_coords[0] - R, sym_coords[1] - R, sym_coords[0] + R, sym_coords[1] + R, fill="white", outline="white")
    c.update()

w.mainloop()
