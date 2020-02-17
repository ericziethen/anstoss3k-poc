
import os
import tkinter as tk

import PIL.ImageOps
from PIL import Image, ImageTk

from anstoss3k.engine.definitions import GameAction
from anstoss3k.engine.states import *
from anstoss3k.ui.definitions import MEDIA_PATH, StateScreen


class MenuStateScreen(StateScreen):
    def __init__(self, root_window, dim_x, dim_y, *, ui_actions):
        super().__init__(root_window, dim_x, dim_y, ui_actions=ui_actions, menu=True)
        self.buttons = []
        self.active_bttn = None
        self.unpressed_bttn_imgs = {}
        self.pressed_bttn_imgs = {}
        self.finish_move_bttn_idx = None

    def _draw_menu(self):
        frame = tk.Frame(master=self.root_window, bg='', borderwidth=0)

        button_image_dir = os.path.join(MEDIA_PATH, 'menu-buttons')
        for idx, bttn_file in enumerate(os.listdir(button_image_dir)):
            file_path = os.path.join(button_image_dir, bttn_file)

            # Store The button images
            img = Image.open(file_path)
            self.unpressed_bttn_imgs[idx] = ImageTk.PhotoImage(img)
            button = tk.Button(
                frame, image=self.unpressed_bttn_imgs[idx], borderwidth=0, text=str(idx),
                command=lambda c=idx: self.bttn_press(c))
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # For now the last button we draw is the Finish Move button
            self.finish_move_bttn_idx = idx

        # Magic Numbers for now
        self.canvas.create_window(8, 480-31-2, window=frame, anchor=tk.NW)

    def bttn_press(self, idx):
        if idx == self.finish_move_bttn_idx:
            # Finish the move
            # TODO - Need to trigger sending a finish move action to the engine
            self.ui_actions.append(GameAction.FINISH_MOVE)