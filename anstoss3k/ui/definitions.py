
import os
import tkinter as tk

MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'graphics')


class StateScreen():
    def __init__(self, root_window, dim_x, dim_y, *, ui_actions, menu=False):
        self.root_window = root_window
        self.ui_actions = ui_actions
        self.has_menu = menu
        self.canvas = tk.Canvas(root_window, width=dim_x, height=dim_y)
        self.canvas.pack()
        self._draw_static_graphics()

    def draw(self):
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
