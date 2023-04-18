from tkinter import *
from functions import *
from tkinter import filedialog

path = 'D:/Fakultet/Image processing/Prezentacija/preikestolen.jpg'
img = cv2.imread(path)


class InstagramForPoor:

    def __init__(self, root):
        root.title('Instagram for poor')
        root.geometry('500x350')
        root.maxsize(1920, 1080)

        frame = LabelFrame(root, padx='10', pady='10')
        frame.pack(padx='10', pady='10')

        contrast = Label(frame, text='Contrast (-100 - 100) ', font=('Courier', 12))
        contrast.grid(row=0, column=0)

        self.contrast_text = StringVar()
        entry = Entry(frame, textvariable=self.contrast_text)
        entry.grid(row=0, column=1)

        empty_label1 = Label(frame, text='  ')
        empty_label1.grid(row=0, column=2)

        contrast_button = Button(frame, text='Apply', command=self.press_contrast_button)
        contrast_button.grid(row=0, column=3)

        brightness = Label(frame, text='Brightness (0 - 100) ', font=('Courier', 12))
        brightness.grid(row=1, column=0)

        self.brightness_text = StringVar()
        entry = Entry(frame, textvariable=self.brightness_text)
        entry.grid(row=1, column=1)

        empty_label2 = Label(frame, text='  ')
        empty_label2.grid(row=1, column=2)

        brightness_button = Button(frame, text='Apply', command=self.press_brightness_button)
        brightness_button.grid(row=1, column=3)

        black_and_white = Label(frame, text='Black and white (0 - 100) ', font=('Courier', 12))
        black_and_white.grid(row=2, column=0)

        self.black_and_white_text = StringVar()
        entry = Entry(frame, textvariable=self.black_and_white_text)
        entry.grid(row=2, column=1)

        empty_label3 = Label(frame, text='  ')
        empty_label3.grid(row=2, column=2)

        black_and_white_button = Button(frame, text='Apply', command=self.press_black_and_white_button_button)
        black_and_white_button.grid(row=2, column=3)

        highlights = Label(frame, text='Highlights (0 - 100) ', font=('Courier', 12))
        highlights.grid(row=3, column=0)

        self.highlights_text = StringVar()
        entry = Entry(frame, textvariable=self.highlights_text)
        entry.grid(row=3, column=1)

        empty_label4 = Label(frame, text='  ')
        empty_label4.grid(row=3, column=2)

        highlights_button = Button(frame, text='Apply', command=self.press_highlights_button)
        highlights_button.grid(row=3, column=3)

        shadows = Label(frame, text='Shadows (0 - 100) ', font=('Courier', 12))
        shadows.grid(row=4, column=0)

        self.shadows_text = StringVar()
        entry = Entry(frame, textvariable=self.shadows_text)
        entry.grid(row=4, column=1)

        empty_label5 = Label(frame, text='  ')
        empty_label5.grid(row=4, column=2)

        shadows_button = Button(frame, text='Apply', command=self.press_shadows_button)
        shadows_button.grid(row=4, column=3)

        warmth = Label(frame, text='Warmth (0 - 100) ', font=('Courier', 12))
        warmth.grid(row=5, column=0)

        self.warmth_text = StringVar()
        entry = Entry(frame, textvariable=self.warmth_text)
        entry.grid(row=5, column=1)

        empty_label6 = Label(frame, text='  ')
        empty_label6.grid(row=5, column=2)

        warmth_button = Button(frame, text='Apply', command=self.press_warmth_button)
        warmth_button.grid(row=5, column=3)

        blur = Label(frame, text='Blur (0 - 5) ', font=('Courier', 12))
        blur.grid(row=6, column=0)

        self.blur_text = StringVar()
        entry = Entry(frame, textvariable=self.blur_text)
        entry.grid(row=6, column=1)

        empty_label7 = Label(frame, text='  ')
        empty_label7.grid(row=6, column=2)

        blur_button = Button(frame, text='Apply', command=self.press_blur_button)
        blur_button.grid(row=6, column=3)

        sharpen = Label(frame, text='Sharpen (0 - 5) ', font=('Courier', 12))
        sharpen.grid(row=7, column=0)

        self.sharpen_text = StringVar()
        entry = Entry(frame, textvariable=self.sharpen_text)
        entry.grid(row=7, column=1)

        empty_label8 = Label(frame, text='  ')
        empty_label8.grid(row=7, column=2)

        sharpen_button = Button(frame, text='Apply', command=self.press_sharpen_button)
        sharpen_button.grid(row=7, column=3)

        vignette = Label(frame, text='Vignette (0 - 100) ', font=('Courier', 12))
        vignette.grid(row=8, column=0)

        self.vignette_text = StringVar()
        entry = Entry(frame, textvariable=self.vignette_text)
        entry.grid(row=8, column=1)

        empty_label9 = Label(frame, text='  ')
        empty_label9.grid(row=8, column=2)

        vignette_button = Button(frame, text='Apply', command=self.press_vignette_button)
        vignette_button.grid(row=8, column=3)

        zoom_in = Label(frame, text='Zoom in (0 - 200) ', font=('Courier', 12))
        zoom_in.grid(row=9, column=0)

        self.zoom_in_text = StringVar()
        entry = Entry(frame, textvariable=self.zoom_in_text)
        entry.grid(row=9, column=1)

        empty_label10 = Label(frame, text='  ')
        empty_label10.grid(row=9, column=2)

        zoom_in_button = Button(frame, text='Apply', command=self.press_zoom_in_button)
        zoom_in_button.grid(row=9, column=3)

        empty_label10 = Label(frame, text='----------------------------------------------')
        empty_label10.grid(row=10, column=0)

        choose_file_button = Button(frame, text='Choose file', command=self.press_choose_file_button)
        choose_file_button.grid(row=11, column=0)

    def press_contrast_button(self):
        proc = float(self.contrast_text.get())
        if proc < -100:
            proc = -100
        if proc > 100:
            proc = 100
        Functions.contrast(img, proc)

    def press_brightness_button(self):
        proc = float(self.brightness_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.brightness(img, proc)

    def press_black_and_white_button_button(self):
        proc = float(self.black_and_white_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.black_and_white(img, proc)

    def press_warmth_button(self):
        proc = float(self.warmth_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.warmth(img, proc)

    def press_highlights_button(self):
        proc = float(self.highlights_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.highlights(img, proc)

    def press_shadows_button(self):
        proc = float(self.shadows_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.shadows(img, proc)

    def press_blur_button(self):
        type = float(self.blur_text.get())
        if type < 0:
            type = 0
        if type > 5:
            type = 5
        Functions.blur(img, type)

    def press_sharpen_button(self):
        type = float(self.sharpen_text.get())
        if type < 0:
            type = 0
        if type > 5:
            type = 5
        Functions.sharpen(img, type)

    def press_vignette_button(self):
        proc = float(self.vignette_text.get())
        if proc < 0:
            proc = 0
        if proc > 100:
            proc = 100
        Functions.vignette(img, proc)

    def press_zoom_in_button(self):
        proc = float(self.zoom_in_text.get())
        if proc < 0:
            proc = 0
        if proc > 200:
            proc = 200
        Functions.zoom_in(img, proc)

    @staticmethod
    def press_choose_file_button():
        filepath = filedialog.askopenfilename()
        print(filepath)
        img = cv2.imread(filepath)
        




