
import os
import tkinter as tk

MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'graphics')


class StateScreen():  # pylint: disable=too-few-public-methods
    def __init__(self, root_window, width, height, *, ui_actions, menu=False):
        self.root_window = root_window
        self.ui_actions = ui_actions
        self.has_menu = menu
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root_window, width=self.width, height=self.height)
        self.canvas.place(x=0, y=0)

    def draw(self):
        tk.Misc.lift(self.canvas)

        self._draw_static_graphics()
        self._draw_dynamic_graphics()
        self._draw_dynamic_content()

        if self.has_menu:
            self._draw_menu()

        self._draw_completed()

    def _draw_static_graphics(self):
        raise NotImplementedError

    def _draw_dynamic_graphics(self):
        raise NotImplementedError

    def _draw_dynamic_content(self):
        raise NotImplementedError

    def _draw_menu(self):
        pass

    def _draw_completed(self):
        pass
