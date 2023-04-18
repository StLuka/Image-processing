import cv2
import numpy
import math

CONST = 0.6


class Functions:

    def contrast(img, proc):
        x = 128 * proc * CONST / 100
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                for c in range(img.shape[2]):
                    if x > 0:
                        if img[h][w][c] < 255 / 2:
                            if img[h][w][c] - x > 0:
                                img[h][w][c] = img[h][w][c] - x
                            else:
                                img[h][w][c] = 0
                        else:
                            if img[h][w][c] + x < 255:
                                img[h][w][c] = img[h][w][c] + x
                            else:
                                img[h][w][c] = 255
                    else:
                        if img[h][w][c] < 255 / 2:
                            if img[h][w][c] - x < 128:
                                img[h][w][c] = img[h][w][c] - x
                            else:
                                img[h][w][c] = 128
                        else:
                            if img[h][w][c] + x > 128:
                                img[h][w][c] = img[h][w][c] + x
                            else:
                                img[h][w][c] = 128
        cv2.imshow('Contrast image', img)
        cv2.waitKey(0)

    def brightness(img, proc):
        x = 255 * proc * CONST / 100
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                for c in range(img.shape[2]):
                    if x > 0:
                        if img[h][w][c] + x < 255:
                            img[h][w][c] = img[h][w][c] + x
                        else:
                            img[h][w][c] = 255
                    else:
                        if img[h][w][c] + x > 0:
                            img[h][w][c] = img[h][w][c] + x
                        else:
                            img[h][w][c] = 0
        cv2.imshow('Brightness image', img)
        cv2.waitKey(0)

    def black_and_white(img, proc):
        c = proc / 100
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                t = (img[h][w][0] + img[h][w][1] + img[h][w][2]) / 3
                img[h][w][0] = (1 - c) * img[h][w][0] + c * t
                img[h][w][1] = (1 - c) * img[h][w][1] + c * t
                img[h][w][2] = (1 - c) * img[h][w][2] + c * t

        cv2.imshow('Black and white', img)
        cv2.waitKey(0)

    def highlights(img, proc):
        x = 128 * proc * CONST / 100
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                for c in range(img.shape[2]):
                    if img[h][w][c] > 127:
                        if img[h][w][c] + x < 255:
                            img[h][w][c] = img[h][w][c] + x
                        else:
                            img[h][w][c] = 255
        cv2.imshow('Highlights', img)
        cv2.waitKey(0)

    def shadows(img, proc):
        x = 128 * proc * CONST / 100
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                for c in range(img.shape[2]):
                    if img[h][w][c] < 128:
                        if img[h][w][c] - x > 0:
                            img[h][w][c] = img[h][w][c] - x
                        else:
                            img[h][w][c] = 0
        cv2.imshow('Shadows', img)
        cv2.waitKey(0)

    def warmth(img, proc):
        c = proc / 100 * CONST
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                hsv_img[h][w][0] = 30

        img2 = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                img[h][w][0] = (1 - c) * img[h][w][0] + c * img2[h][w][0]
                img[h][w][1] = (1 - c) * img[h][w][1] + c * img2[h][w][1]
                img[h][w][2] = (1 - c) * img[h][w][2] + c * img2[h][w][2]

        cv2.imshow('Warmth', img)
        cv2.waitKey(0)

    def blur(img, type):
        if type == 1:
            for h in range(img.shape[0]):
                for w in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    sum += img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c] * 9
                        img[h][w][c] = sum / 9

        if type == 2:
            for h in range(img.shape[0]):
                for w in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-2, 3):
                            for j in range(-2, 3):
                                try:
                                    sum += img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c] * 25
                        img[h][w][c] = sum / 25

        if type == 3:
            for h in range(img.shape[0]):
                for w in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-3, 4):
                            for j in range(-3, 4):
                                try:
                                    sum += img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c] * 49
                        img[h][w][c] = sum / 49

        if type == 4:
            for h in range(img.shape[0]):
                for w in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-4, 5):
                            for j in range(-4, 5):
                                try:
                                    sum += img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c] * 81
                        img[h][w][c] = sum / 81

        if type == 5:
            for h in range(img.shape[0]):
                for w in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-5, 6):
                            for j in range(-5, 6):
                                try:
                                    sum += img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c] * 121
                        img[h][w][c] = sum / 121
        cv2.imshow('Blur', img)
        cv2.waitKey(0)

    def sharpen(img, type):
        if type == 1:
            for h in range(1, img.shape[0] - 1):
                for w in range(1, img.shape[1] - 1):
                    for c in range(img.shape[2]):
                        sum = 0
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                try:
                                    if (i == 0) and (j == 0):
                                        sum += 8 * img[h][w][c]
                                    else:
                                        sum -= img[i + h][j + w][c]
                                except:
                                    sum = img[h][w][c]
                        img[h][w][c] = sum

        cv2.imshow('Sharpen', img)
        cv2.waitKey(0)

    def vignette(img, proc):
        m = numpy.empty((img.shape[0], img.shape[1]))
        max = math.sqrt(pow(img.shape[0] / 2, 2) + pow(img.shape[1] / 2, 2))
        min = proc / 100 * (0.3 * math.sqrt(pow(img.shape[0] / 2, 2) + pow(img.shape[1] / 2, 2))) + (
                    1 - proc / 100) * max
        for h in range(img.shape[0]):
            for w in range(img.shape[1]):
                m[h][w] = math.sqrt(pow(abs(h - img.shape[0] / 2), 2) + pow(abs(w - img.shape[1] / 2), 2))
                for c in range(img.shape[2]):
                    if m[h][w] > min:
                        t = abs(min - m[h][w]) / (max - min)
                        img[h][w][c] = (1 - t) * img[h][w][c]

        cv2.imshow('Vignette', img)
        cv2.waitKey(0)

    def zoom_in(img, proc):
        new_img = numpy.empty((img.shape[0], img.shape[1], img.shape[2]))
        proc = (100 + proc) / 100
        t1 = round((img.shape[0] - (img.shape[0] / proc)) / 2)
        t2 = round((img.shape[1] - (img.shape[1] / proc)) / 2)
        tmph = 0
        tmpw = 0
        for h in range(t1, img.shape[0] - t1 - 1):
            for w in range(t2, img.shape[1] - t2 - 1):
                h1 = round(proc * tmph)
                w1 = round(proc * tmpw)
                for c in range(img.shape[2]):
                    new_img[h1][w1][c] = img[h][w][c]
                tmpw += 1
            tmph += 1
            tmpw = 0

        for h in range(new_img.shape[0]):
            for w in range(new_img.shape[1]):
                for c in range(new_img.shape[2]):
                    if new_img[h][w][c] == 0:
                        new_img[h][w][c] = new_img[h][w - 1][c]
                    img[h][w][c] = new_img[h][w][c]

        for h in range(new_img.shape[0]):
            for w in range(new_img.shape[1]):
                for c in range(new_img.shape[2]):
                    if new_img[h][w][c] == 0:
                        new_img[h][w][c] = new_img[h - 1][w][c]
                    img[h][w][c] = new_img[h][w][c]

        cv2.imshow('Zoom in', img)
        cv2.waitKey(0)
