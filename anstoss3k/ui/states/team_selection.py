
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.ui.definitions import MEDIA_PATH, MenuStateScreen


class TeamSelectionStateScreen(MenuStateScreen):
    # TODO - If this comes from Config Files then move it to parent class
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Team Selection (grafik_cpr-0000001450).jpg')
        print(img_path)
        self.background = ImageTk.PhotoImage(file=img_path)
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        print(self.background.width(), self.background.height())
        print(self.canvas.__dict__)

    def _draw_dynamic_graphics(self):
        print('Call _draw_dynamic_graphics()')

    def _draw_dynamic_content(self):
        print('Call _draw_dynamic_content()')

