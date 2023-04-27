import cv2
import numpy
import math

CONST = 0.6


class Functions:

    def __init__(self, filepath):
        self.img = cv2.imread(filepath)

    def contrast(self, proc):
        x = 128 * proc * CONST / 100
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                for c in range(self.img.shape[2]):
                    if x > 0:
                        if self.img[h][w][c] < 255 / 2:
                            if self.img[h][w][c] - x > 0:
                                self.img[h][w][c] = self.img[h][w][c] - x
                            else:
                                self.img[h][w][c] = 0
                        else:
                            if self.img[h][w][c] + x < 255:
                                self.img[h][w][c] = self.img[h][w][c] + x
                            else:
                                self.img[h][w][c] = 255
                    else:
                        if self.img[h][w][c] < 255 / 2:
                            if self.img[h][w][c] - x < 128:
                                self.img[h][w][c] = self.img[h][w][c] - x
                            else:
                                self.img[h][w][c] = 128
                        else:
                            if self.img[h][w][c] + x > 128:
                                self.img[h][w][c] = self.img[h][w][c] + x
                            else:
                                self.img[h][w][c] = 128
        cv2.imshow('Contrast image', self.img)
        cv2.waitKey(0)

    def brightness(self, proc):
        x = 255 * proc * CONST / 100
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                for c in range(self.img.shape[2]):
                    if x > 0:
                        if self.img[h][w][c] + x < 255:
                            self.img[h][w][c] = self.img[h][w][c] + x
                        else:
                            self.img[h][w][c] = 255
                    else:
                        if self.img[h][w][c] + x > 0:
                            self.img[h][w][c] = self.img[h][w][c] + x
                        else:
                            self.img[h][w][c] = 0
        cv2.imshow('Brightness image', self.img)
        cv2.waitKey(0)

    def black_and_white(self, proc):
        c = proc / 100
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                t = (self.img[h][w][0] + self.img[h][w][1] + self.img[h][w][2]) / 3
                self.img[h][w][0] = (1 - c) * self.img[h][w][0] + c * t
                self.img[h][w][1] = (1 - c) * self.img[h][w][1] + c * t
                self.img[h][w][2] = (1 - c) * self.img[h][w][2] + c * t

        cv2.imshow('Black and white', self.img)
        cv2.waitKey(0)

    def highlights(self, proc):
        x = 128 * proc * CONST / 100
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                for c in range(self.img.shape[2]):
                    if self.img[h][w][c] > 127:
                        if self.img[h][w][c] + x < 255:
                            self.img[h][w][c] = self.img[h][w][c] + x
                        else:
                            self.img[h][w][c] = 255
        cv2.imshow('Highlights', self.img)
        cv2.waitKey(0)

    def shadows(self, proc):
        x = 128 * proc * CONST / 100
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                for c in range(self.img.shape[2]):
                    if self.img[h][w][c] < 128:
                        if self.img[h][w][c] - x > 0:
                            self.img[h][w][c] = self.img[h][w][c] - x
                        else:
                            self.img[h][w][c] = 0
        cv2.imshow('Shadows', self.img)
        cv2.waitKey(0)

    def warmth(self, proc):
        c = proc / 100 * CONST
        hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                hsv_img[h][w][0] = 30

        img2 = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                self.img[h][w][0] = (1 - c) * self.img[h][w][0] + c * img2[h][w][0]
                self.img[h][w][1] = (1 - c) * self.img[h][w][1] + c * img2[h][w][1]
                self.img[h][w][2] = (1 - c) * self.img[h][w][2] + c * img2[h][w][2]

        cv2.imshow('Warmth', self.img)
        cv2.waitKey(0)

    def blur(self, type):
        if type == 1:
            for h in range(self.img.shape[0]):
                for w in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    sum += self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c] * 9
                        self.img[h][w][c] = sum / 9

        if type == 2:
            for h in range(self.img.shape[0]):
                for w in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-2, 3):
                            for j in range(-2, 3):
                                try:
                                    sum += self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c] * 25
                        self.img[h][w][c] = sum / 25

        if type == 3:
            for h in range(self.img.shape[0]):
                for w in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-3, 4):
                            for j in range(-3, 4):
                                try:
                                    sum += self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c] * 49
                        self.img[h][w][c] = sum / 49

        if type == 4:
            for h in range(self.img.shape[0]):
                for w in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-4, 5):
                            for j in range(-4, 5):
                                try:
                                    sum += self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c] * 81
                        self.img[h][w][c] = sum / 81

        if type == 5:
            for h in range(self.img.shape[0]):
                for w in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-5, 6):
                            for j in range(-5, 6):
                                try:
                                    sum += self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c] * 121
                        self.img[h][w][c] = sum / 121
        cv2.imshow('Blur', self.img)
        cv2.waitKey(0)

    def sharpen(self, type):
        if type == 1:
            for h in range(1, self.img.shape[0] - 1):
                for w in range(1, self.img.shape[1] - 1):
                    for c in range(self.img.shape[2]):
                        sum = 0
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    if (i == 0) and (j == 0):
                                        sum += 8 * self.img[h][w][c]
                                    else:
                                        sum -= self.img[i + h][j + w][c]
                                except:
                                    sum = self.img[h][w][c]
                        self.img[h][w][c] = sum

        cv2.imshow('Sharpen', self.img)
        cv2.waitKey(0)

    def vignette(self, proc):
        m = numpy.empty((self.img.shape[0], self.img.shape[1]))
        max = math.sqrt(pow(self.img.shape[0] / 2, 2) + pow(self.img.shape[1] / 2, 2))
        min = proc / 100 * (0.3 * math.sqrt(pow(self.img.shape[0] / 2, 2) + pow(self.img.shape[1] / 2, 2))) + (
                    1 - proc / 100) * max
        for h in range(self.img.shape[0]):
            for w in range(self.img.shape[1]):
                m[h][w] = math.sqrt(pow(abs(h - self.img.shape[0] / 2), 2) + pow(abs(w - self.img.shape[1] / 2), 2))
                for c in range(self.img.shape[2]):
                    if m[h][w] > min:
                        t = abs(min - m[h][w]) / (max - min)
                        self.img[h][w][c] = (1 - t) * self.img[h][w][c]

        cv2.imshow('Vignette', self.img)
        cv2.waitKey(0)

    def zoom_in(self, proc):
        new_img = numpy.empty((self.img.shape[0], self.img.shape[1], self.img.shape[2]))
        proc = (100 + proc) / 100
        t1 = round((self.img.shape[0] - (self.img.shape[0] / proc)) / 2)
        t2 = round((self.img.shape[1] - (self.img.shape[1] / proc)) / 2)
        tmph = 0
        tmpw = 0
        for h in range(t1, self.img.shape[0] - t1 - 1):
            for w in range(t2, self.img.shape[1] - t2 - 1):
                h1 = round(proc * tmph)
                w1 = round(proc * tmpw)
                for c in range(self.img.shape[2]):
                    new_img[h1][w1][c] = self.img[h][w][c]
                tmpw += 1
            tmph += 1
            tmpw = 0

        for h in range(new_img.shape[0]):
            for w in range(new_img.shape[1]):
                for c in range(new_img.shape[2]):
                    if new_img[h][w][c] == 0:
                        new_img[h][w][c] = new_img[h][w - 1][c]
                    self.img[h][w][c] = new_img[h][w][c]

        for h in range(new_img.shape[0]):
            for w in range(new_img.shape[1]):
                for c in range(new_img.shape[2]):
                    if new_img[h][w][c] == 0:
                        new_img[h][w][c] = new_img[h - 1][w][c]
                    self.img[h][w][c] = new_img[h][w][c]

        cv2.imshow('Zoom in', self.img)
        cv2.waitKey(0)
