
import os
import tkinter as tk

from PIL import ImageTk

from anstoss3k.engine.definitions import GameAction
from anstoss3k.ui.definitions import MEDIA_PATH, StateScreen


class MatchDayPreviewStateScreen(StateScreen):
    # TODO - If this comes from Config Files then move it to parent class
    def _draw_static_graphics(self):
        img_path = os.path.join(MEDIA_PATH, 'backgrounds', 'Match Day Preview (grafik_cpr-0000000951).jpg')
        #print(img_path)
        self.background = ImageTk.PhotoImage(file=img_path)
        self.canvas.create_image(0, 0, image=self.background, anchor=tk.NW)

        #print(self.background.width(), self.background.height())
        #print(self.canvas.__dict__)

    def _draw_dynamic_graphics(self):
        print('MatchDayPreviewStateScreen:Call _draw_dynamic_graphics()')
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Not Selected (grafik_cpr-0000002713)_TRANS.png')
        self.ok_button_normal_img = ImageTk.PhotoImage(file=button_path)
        button_path = os.path.join(MEDIA_PATH, 'buttons', 'OK Selected (grafik_cpr-0000002704)_TRANS.png')
        self.ok_button_pressed_img = ImageTk.PhotoImage(file=button_path)

        self.button = tk.Button(self.canvas, image=self.ok_button_normal_img, borderwidth=0)
        #self.button.bind("<Button-1>", self.ok_pressed)
        #self.button.bind("<ButtonRelease-1>", self.ok_released)

        self.canvas.create_window(600, 440, window=self.button)


        self.button_frame = tk.Frame(width=88, height=95)
        self.eric = self.canvas.create_image(400-88/2, 440-95/2, image=self.ok_button_normal_img, anchor=tk.NW)
        #self.canvas.create_window(400, 440, window=self.button_frame)


        #self.rectang = self.canvas.create_rectangle(400-88/2, 440-95/2, 400-88/2+88, 440-95/2+95, fill='')
        #print(type(self.rectang), self.rectang)
        self.canvas.tag_bind(self.eric, '<Button-1>', self.ok_pressed2)
        self.canvas.tag_bind(self.eric, '<ButtonRelease-1>', self.ok_released2)

        #print(type(self.button_canvas), self.button_canvas)
        #self.button_canvas.bind("<Button-1>", self.ok_pressed2)
        #self.button_canvas.bind("<ButtonRelease-1>", self.ok_released2)



    def _draw_dynamic_content(self):
        print('MatchDayPreviewStateScreen:Call _draw_dynamic_content()')

    def _draw_completed(self):
        print('MatchDayPreviewStateScreen:Call _draw_completed()')

    def ok_pressed(self, event):
        print('MatchDayPreviewStateScreen:Call ok_pressed()')
        self.button.configure({'image': self.ok_button_pressed_img})

    def ok_released(self, event):
        print('MatchDayPreviewStateScreen:Call ok_released()')
        self.button.configure({'image': self.ok_button_normal_img})
        self.ui_actions.append(GameAction.FINISH_MOVE)








    def ok_pressed2(self, event):
        print('MatchDayPreviewStateScreen:Call ok_pressed()')
        #self.button.configure({'image': self.ok_button_pressed_img})
        self.canvas.itemconfigure(self.eric, image=self.ok_button_pressed_img)

    def ok_released2(self, event):
        print('MatchDayPreviewStateScreen:Call ok_released()')
        #self.button.configure({'image': self.ok_button_normal_img})
        self.canvas.itemconfigure(self.eric, image=self.ok_button_normal_img)





