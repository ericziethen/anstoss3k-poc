
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.ui.definitions import MEDIA_PATH
from anstoss3k.ui.menu import MenuStateScreen


class TeamSelectionStateScreen(MenuStateScreen):
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Team Selection (grafik_cpr-0000001450).jpg')
        self.background = ImageTk.PhotoImage(file=img_path)  # pylint: disable=attribute-defined-outside-init
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

    def _draw_dynamic_graphics(self):
        print('TeamSelectionStateScreen:Call _draw_dynamic_graphics()')

    def _draw_dynamic_content(self):
        print('TeamSelectionStateScreen:Call _draw_dynamic_content()')
