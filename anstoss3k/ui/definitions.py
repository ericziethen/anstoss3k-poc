
import os
import tkinter as tk

MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'graphics')


class StateScreen():
    def __init__(self, root_window, width, height, *, ui_actions, menu=False):
        self.root_window = root_window
        self.ui_actions = ui_actions
        self.has_menu = menu
        self.width = width
        self.height = height
        self.canvas = None

    def draw(self):
        self.canvas = tk.Canvas(self.root_window, width=self.width, height=self.height)

        # TODO - If can use place then we don't need to destroy all the time and the canvas only needs to be created at initialisation together with 
        #self.canvas.pack()
        self.canvas.place(x=0, y=0)


        self._draw_static_graphics()
        self._draw_dynamic_graphics()
        self._draw_dynamic_content()

        if self.has_menu:
            self._draw_menu()

    def send_input_to_engine(self):
        raise NotImplementedError

    def _draw_static_graphics(self):
        raise NotImplementedError

    def _draw_dynamic_graphics(self):
        raise NotImplementedError

    def _draw_dynamic_content(self):
        raise NotImplementedError

    def _draw_menu(self):
        raise NotImplementedError
