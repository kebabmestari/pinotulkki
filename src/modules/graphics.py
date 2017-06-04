import threading
import tkinter
from queue import Empty
from queue import Queue

from tools import logger

_gfx = None


class GFX_Window(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.color = 'black'
        self.events = Queue()
        self.events_empty_count = 0
        self.start()

    def run(self):
        self.root = tkinter.Tk()
        self.C = tkinter.Canvas(self.root, bg='white', height=480, width=640)
        self.C.pack()
        self.pop_event(50)
        self.root.mainloop()

    def push_event(self, callback, *args):
        self.events.put((callback, args))

    def pop_event(self, time):
        try:
            callable, args = self.events.get_nowait()
        except Empty:
            self.events_empty_count += 1
        else:
            self.events_empty_count = 0
            callable(*args)

        if self.events_empty_count == 10:
            time = 500
        self.root.after(time, self.pop_event, time)

    def draw_line(self, x0, y0, x1, y1):
        self.C.create_line(x0 + 2, y0 + 2, x1 + 2, y1 + 2, fill=self.color)

    def draw_circle(self, x, y, r):
        self.C.create_oval(x + 2, y + 2, x + r + 2, y + r + 2, outline=self.color)

    def draw_rect(self, x0, y0, x1, y1):
        self.C.create_rectangle(x0 + 2, y0 + 2, x1 + 2, y1 + 2, outline=self.color)

    def set_color(self, color):
        self.color = color

    def exit(self):
        self.root.destroy()



def init_handler():
    global _gfx
    _gfx = GFX_Window()
    logger.log_graphics('Initialized Tkinter window')


def line_handler(x0, y0, x1, y1):
    (x0, y0, x1, y1) = convert_arguments(x0, y0, x1, y1)
    _gfx.push_event(_gfx.draw_line, x0, y0, x1, y1)


def circle_handler(x, y, r):
    (x, y, r) = convert_arguments(x, y, r)
    _gfx.push_event(_gfx.draw_circle, x, y, r)


def box_handler(x0, y0, sl):
    (x0, y0, sl) = convert_arguments(x0, y0, sl)
    _gfx.push_event(_gfx.draw_rect, x0, y0, x0 + sl, y0 + sl)


def rect_handler(x0, y0, x1, y1):
    (x0, y0, x1, y1) = convert_arguments(x0, y0, x1, y1)
    _gfx.push_event(_gfx.draw_rect, x0, y0, x1, y1)


def triangle_handler(x0, y0, sl):
    (x0, y0, sl) = convert_arguments(x0, y0, sl)
    _gfx.push_event(_gfx.draw_line, x0 + sl / 2, y0, x0, y0 + sl)
    _gfx.push_event(_gfx.draw_line, x0 + sl / 2, y0, x0 + sl, y0 + sl)
    _gfx.push_event(_gfx.draw_line, x0, y0 + sl, x0 + sl, y0 + sl)


def color_handler(color):
    _gfx.push_event(_gfx.set_color, color)


# Convert arguments to integers
def convert_arguments(*args):
    return [int(i) for i in args]


# Quit TKinter
def close_gfx():
    if _gfx == None:
        return
    logger.log_debug('Closing TKinter')
    _gfx.push_event(_gfx.exit)
