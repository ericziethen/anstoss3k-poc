
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.engine.definitions import GameAction
from anstoss3k.ui.definitions import MEDIA_PATH, StateScreen


class MatchDayResultStateScreen(StateScreen):
    # TODO - If this comes from Config Files then move it to parent class
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Match Day Results (grafik_cpr-0000002597).jpg')
        #print(img_path)
        self.background = ImageTk.PhotoImage(file=img_path)
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        #print(self.background.width(), self.background.height())
        #print(self.canvas.__dict__)

    def _draw_dynamic_graphics(self):
        print('MatchDayResultStateScreen:Call _draw_dynamic_graphics()')
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Not Selected (grafik_cpr-0000002713).bmp')
        self.ok_button_normal_img = ImageTk.PhotoImage(file=button_path)
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Selected (grafik_cpr-0000002704).bmp')
        self.ok_button_pressed_img = ImageTk.PhotoImage(file=button_path)

        self.button = tk.Button(self.canvas, image=self.ok_button_normal_img, borderwidth=0)
        self.button.bind("<Button-1>", self.ok_pressed)
        self.button.bind("<ButtonRelease-1>", self.ok_released)

        self.canvas.create_window(600, 440, window=self.button)

    def _draw_dynamic_content(self):
        print('MatchDayResultStateScreen:Call _draw_dynamic_content()')

    def _draw_completed(self):
        print('MatchDayResultStateScreen:Call _draw_completed()')

    def ok_pressed(self, event):
        print('MatchDayResultStateScreen:Call ok_pressed()')
        self.button.configure({'image': self.ok_button_pressed_img})
        self.ui_actions.append(GameAction.FINISH_MOVE)

    def ok_released(self, event):
        print('MatchDayResultStateScreen:Call ok_released()')
        self.button.configure({'image': self.ok_button_normal_img})
