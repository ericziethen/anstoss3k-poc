
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.engine.definitions import GameAction
from anstoss3k.ui.definitions import MEDIA_PATH, StateScreen


class ProgressWeekStateScreen(StateScreen):
    # TODO - If this comes from Config Files then move it to parent class
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Progress Week (grafik_cpr-0000000544).jpg')
        #print(img_path)
        self.background = ImageTk.PhotoImage(file=img_path)
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        #print(self.background.width(), self.background.height())
        #print(self.canvas.__dict__)

    def _draw_dynamic_graphics(self):
        print('ProgressWeekStateScreen:Call _draw_dynamic_graphics()')

    def _draw_dynamic_content(self):
        print('ProgressWeekStateScreen:Call _draw_dynamic_content()')

    def _draw_completed(self):
        print('ProgressWeekStateScreen:Call _draw_completed()')
        self.root_window.after(3000, self.week_over)

    def week_over(self):
        print('ProgressWeekStateScreen:Call week_over()')
        self.ui_actions.append(GameAction.FINISH_MOVE)
