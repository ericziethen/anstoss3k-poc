
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.engine.definitions import GameAction
from anstoss3k.ui.definitions import MEDIA_PATH, StateScreen


class SeasonEndStateScreen(StateScreen):
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Year End (grafik_cpr-0000001875).jpg')
        self.background = ImageTk.PhotoImage(file=img_path)  # pylint: disable=attribute-defined-outside-init
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

    def _draw_dynamic_graphics(self):
        print('SeasonEndStateScreen:Call _draw_dynamic_graphics()')
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Not Selected (grafik_cpr-0000002713)_TRANS.png')
        self.ok_button_normal_img = ImageTk.PhotoImage(file=button_path)  # pylint: disable=attribute-defined-outside-init
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Selected (grafik_cpr-0000002704)_TRANS.png')
        self.ok_button_pressed_img = ImageTk.PhotoImage(file=button_path)  # pylint: disable=attribute-defined-outside-init

        self.button = self.canvas.create_image(  # pylint: disable=attribute-defined-outside-init
            400 - 88 / 2, 440 - 95 / 2, image=self.ok_button_normal_img, anchor=tk.NW)
        self.canvas.tag_bind(self.button, '<Button-1>', self.ok_pressed)
        self.canvas.tag_bind(self.button, '<ButtonRelease-1>', self.ok_released)

    def _draw_dynamic_content(self):
        print('SeasonEndStateScreen:Call _draw_dynamic_content()')

    def _draw_completed(self):
        print('SeasonEndStateScreen:Call _draw_completed()')

    def ok_pressed(self, event):  # pylint: disable=unused-argument
        print('SeasonEndStateScreen:Call ok_pressed()')
        self.canvas.itemconfigure(self.button, image=self.ok_button_pressed_img)

    def ok_released(self, event):  # pylint: disable=unused-argument
        print('SeasonEndStateScreen:Call ok_released()')
        self.canvas.itemconfigure(self.button, image=self.ok_button_normal_img)
        self.ui_actions.append(GameAction.FINISH_MOVE)
