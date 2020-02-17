
import os
import tkinter as tk

import PIL.ImageOps
from PIL import Image, ImageTk

MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'graphics')


class StateScreen():
    def __init__(self, root_window, dim_x, dim_y, *, menu=False):
        self.root_window = root_window
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


class MenuStateScreen(StateScreen):
    def __init__(self, root_window, dim_x, dim_y):
        super().__init__(root_window, dim_x, dim_y, menu=True)
        self.buttons = []
        self.active_bttn = None
        self.unpressed_bttn_imgs = {}
        self.pressed_bttn_imgs = {}

    def _draw_menu(self):
        frame = tk.Frame(master=self.root_window, bg='', borderwidth=0)

        button_image_dir = os.path.join(MEDIA_PATH, 'menu-buttons')
        for idx, bttn_file in enumerate(os.listdir(button_image_dir)):
            file_path = os.path.join(button_image_dir, bttn_file)

            # Store The button images
            img = Image.open(file_path)
            self.unpressed_bttn_imgs[idx] = ImageTk.PhotoImage(img)
            button = tk.Button(frame, image=self.unpressed_bttn_imgs[idx], borderwidth=0, text=str(idx))
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        print('self.canvas.winfo_height()', self.canvas.winfo_height())

        self.canvas.create_window(8, 480-31-2, window=frame, anchor=tk.NW)




        '''
        frame = tk.Frame(master=self.root_window, bg='red', borderwidth=5)
        frame_height = 31

        label = tk.Label(master=frame, text='Eric')
        label.pack(expand=tk.YES, fill=tk.BOTH)

        self.canvas.create_window(
            #0, self.canvas.winfo_height() - frame_height - 100,
            0, 400,
            anchor=tk.CENTER, window=frame, width=self.canvas.winfo_width(), height=frame_height)
        frame.pack(expand=tk.YES, fill=tk.BOTH)
        '''
        #'''
        #'''
        '''
        button_image_dir = os.path.join(MEDIA_PATH, 'menu-buttons')
        for idx, bttn_file in enumerate(os.listdir(button_image_dir)):
            file_path = os.path.join(button_image_dir, bttn_file)

            # Store The button images
            img = Image.open(file_path)
            self.unpressed_bttn_imgs[idx] = ImageTk.PhotoImage(img)
            self.pressed_bttn_imgs[idx] = ImageTk.PhotoImage(PIL.ImageOps.invert(img))

            # Create the Buttons
            #self.buttons.append(tk.Button(self.canvas, image=self.unpressed_bttn_imgs[idx], borderwidth=0, text=str(idx), command=lambda c=idx: self.command(c)))
            self.buttons.append(tk.Button(frame, image=self.unpressed_bttn_imgs[idx], borderwidth=0, text=str(idx)))
            self.buttons[idx].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        '''


