from tkinter import *
from functions import *
from tkinter import filedialog
from PIL import Image, ImageTk

class InstagramForThePoor:

    def __init__(self, root):
        root.title('Instagram for the poor')
        root.geometry('1100x600')
        root.maxsize(1920, 1080)

        self.functions = Functions(None)

        frame = Frame(root)
        frame.pack()

        leftframe = Frame(root)
        leftframe.pack(side=LEFT)

        self.rightframe = Frame(root, bg='light gray', width=650, height=500)
        self.rightframe.pack(side=RIGHT)

        self.photo_label = Label(self.rightframe, text='Image loader', font=('Courier', 12), bg='light gray')
        self.photo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        contrast = Label(leftframe, text='Contrast', font=('Courier', 12))
        contrast.grid(row=0, column=0)

        self.contrast_text = IntVar()
        self.contrast_scale = Scale(leftframe, variable=self.contrast_text, from_=-100, to=100, orient=HORIZONTAL)
        self.contrast_scale.grid(row=0, column=1)

        contrast_button = Button(leftframe, text='Apply', command=self.press_contrast_button)
        contrast_button.grid(row=0, column=3)

        brightness = Label(leftframe, text='Brightness', font=('Courier', 12))
        brightness.grid(row=1, column=0)

        self.brightness_text = IntVar()
        self.brightness_scale = Scale(leftframe, variable=self.brightness_text, from_=0, to=100, orient=HORIZONTAL)
        self.brightness_scale.grid(row=1, column=1)

        brightness_button = Button(leftframe, text='Apply', command=self.press_brightness_button)
        brightness_button.grid(row=1, column=3)

        black_and_white = Label(leftframe, text='Black and white', font=('Courier', 12))
        black_and_white.grid(row=2, column=0)

        self.black_and_white_text = IntVar()
        self.black_and_white_scale = Scale(leftframe, variable=self.black_and_white_text, from_=0, to=100, orient=HORIZONTAL)
        self.black_and_white_scale.grid(row=2, column=1)

        black_and_white_button = Button(leftframe, text='Apply', command=self.press_black_and_white_button_button)
        black_and_white_button.grid(row=2, column=3)

        highlights = Label(leftframe, text='Highlights', font=('Courier', 12))
        highlights.grid(row=3, column=0)

        self.highlights_text = IntVar()
        self.highlights_scale = Scale(leftframe, variable=self.highlights_text, from_=0, to=100, orient=HORIZONTAL)
        self.highlights_scale.grid(row=3, column=1)

        highlights_button = Button(leftframe, text='Apply', command=self.press_highlights_button)
        highlights_button.grid(row=3, column=3)

        shadows = Label(leftframe, text='Shadows', font=('Courier', 12))
        shadows.grid(row=4, column=0)

        self.shadows_text = IntVar()
        self.shadows_scale = Scale(leftframe, variable=self.shadows_text, from_=0, to=100, orient=HORIZONTAL)
        self.shadows_scale.grid(row=4, column=1)

        shadows_button = Button(leftframe, text='Apply', command=self.press_shadows_button)
        shadows_button.grid(row=4, column=3)

        warmth = Label(leftframe, text='Warmth', font=('Courier', 12))
        warmth.grid(row=5, column=0)

        self.warmth_text = IntVar()
        self.warmth_scale = Scale(leftframe, variable=self.warmth_text, from_=0, to=100, orient=HORIZONTAL)
        self.warmth_scale.grid(row=5, column=1)

        warmth_button = Button(leftframe, text='Apply', command=self.press_warmth_button)
        warmth_button.grid(row=5, column=3)

        blur = Label(leftframe, text='Blur', font=('Courier', 12))
        blur.grid(row=6, column=0)

        self.blur_text = IntVar()
        self.blur_scale = Scale(leftframe, variable=self.blur_text, from_=0, to=5, orient=HORIZONTAL)
        self.blur_scale.grid(row=6, column=1)

        blur_button = Button(leftframe, text='Apply', command=self.press_blur_button)
        blur_button.grid(row=6, column=3)

        sharpen = Label(leftframe, text='Sharpen', font=('Courier', 12))
        sharpen.grid(row=7, column=0)

        self.sharpen_text = IntVar()
        self.sharpen_scale = Scale(leftframe, variable=self.sharpen_text, from_=0, to=5, orient=HORIZONTAL)
        self.sharpen_scale.grid(row=7, column=1)

        sharpen_button = Button(leftframe, text='Apply', command=self.press_sharpen_button)
        sharpen_button.grid(row=7, column=3)

        vignette = Label(leftframe, text='Vignette', font=('Courier', 12))
        vignette.grid(row=8, column=0)

        self.vignette_text = IntVar()
        self.vignette_scale = Scale(leftframe, variable=self.vignette_text, from_=0, to=100, orient=HORIZONTAL)
        self.vignette_scale.grid(row=8, column=1)

        vignette_button = Button(leftframe, text='Apply', command=self.press_vignette_button)
        vignette_button.grid(row=8, column=3)

        zoom_in = Label(leftframe, text='Zoom in', font=('Courier', 12))
        zoom_in.grid(row=9, column=0)

        self.zoom_in_text = IntVar()
        self.zoom_in_scale = Scale(leftframe, variable=self.zoom_in_text, from_=0, to=200, orient=HORIZONTAL)
        self.zoom_in_scale.grid(row=9, column=1)

        zoom_in_button = Button(leftframe, text='Apply', command=self.press_zoom_in_button)
        zoom_in_button.grid(row=9, column=3)

        empty_label10 = Label(leftframe, text='-------------------------------------')
        empty_label10.grid(row=10, column=0)

        empty_label11 = Label(leftframe, text='---------------------------')
        empty_label11.grid(row=10, column=1)

        empty_label11 = Label(leftframe, text='---------------')
        empty_label11.grid(row=10, column=3)

        choose_file_button = Button(leftframe, text='Choose file', command=self.press_choose_file_button, bd=2, font=('Courier', 11), bg='light gray')
        choose_file_button.grid(row=11, column=1)

    def press_contrast_button(self):
        proc = float(self.contrast_text.get())
        img = self.functions.contrast(proc)
        self.load_image(img)

    def press_brightness_button(self):
        proc = float(self.brightness_text.get())
        img = self.functions.brightness(proc)
        self.load_image(img)

    def press_black_and_white_button_button(self):
        proc = float(self.black_and_white_text.get())
        img = self.functions.black_and_white(proc)
        self.load_image(img)

    def press_warmth_button(self):
        proc = float(self.warmth_text.get())
        img = self.functions.warmth(proc)
        self.load_image(img)

    def press_highlights_button(self):
        proc = float(self.highlights_text.get())
        img = self.functions.highlights(proc)
        self.load_image(img)

    def press_shadows_button(self):
        proc = float(self.shadows_text.get())
        img = self.functions.shadows(proc)
        self.load_image(img)

    def press_blur_button(self):
        type = float(self.blur_text.get())
        img = self.functions.blur(type)
        self.load_image(img)

    def press_sharpen_button(self):
        type = float(self.sharpen_text.get())
        img = self.functions.sharpen(type)
        self.load_image(img)

    def press_vignette_button(self):
        proc = float(self.vignette_text.get())
        img = self.functions.vignette(proc)
        self.load_image(img)

    def press_zoom_in_button(self):
        proc = float(self.zoom_in_text.get())
        img = self.functions.zoom_in(proc)
        self.load_image(img)

    def press_choose_file_button(self):
        filepath = filedialog.askopenfilename()
        img = cv2.imread(filepath)
        self.functions = Functions(filepath)
        self.restart_scales()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        photo_from_array = Image.fromarray(img)

        frame_width = self.rightframe.winfo_width()
        frame_height = self.rightframe.winfo_height()

        width_ratio = frame_width / photo_from_array.width
        height_ratio = frame_height / photo_from_array.height
        scale_factor = min(width_ratio, height_ratio)

        new_width = int(photo_from_array.width * scale_factor)
        new_height = int(photo_from_array.height * scale_factor)

        resized_image = photo_from_array.resize((new_width, new_height))

        photo_image = ImageTk.PhotoImage(image=resized_image)
        self.photo_label.configure(image=photo_image)
        self.photo_label.image = photo_image

        self.frame.update()
        self.photo_label.place(x=(frame_width - self.photo_label.winfo_width()) // 2,
                               y=(frame_height - self.photo_label.winfo_height()) // 2)

    def load_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        photo_from_array = Image.fromarray(img)

        frame_width = self.rightframe.winfo_width()
        frame_height = self.rightframe.winfo_height()

        photo_image = ImageTk.PhotoImage(image=photo_from_array)
        self.photo_label.configure(image=photo_image)
        self.photo_label.image = photo_image

        self.frame.update()
        self.photo_label.place(x=(frame_width - self.photo_label.winfo_width()) // 2,
                               y=(frame_height - self.photo_label.winfo_height()) // 2)

    def restart_scales(self):
        self.contrast_scale.set(0)
        self.brightness_scale.set(0)
        self.black_and_white_scale.set(0)
        self.highlights_scale.set(0)
        self.shadows_scale.set(0)
        self.warmth_scale.set(0)
        self.blur_scale.set(0)
        self.sharpen_scale.set(0)
        self.vignette_scale.set(0)
        self.zoom_in_scale.set(0)
