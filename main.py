import cv2

CONST = 0.6

def contrast(img, proc):
    x = 128 * proc * CONST / 100
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for c in range(img.shape[2]):
                if(x > 0):
                    if(img[h][w][c] < 255/2):
                        if(img[h][w][c] - x > 0):
                            img[h][w][c] = img[h][w][c] - x
                        else:
                            img[h][w][c] = 0
                    else:
                        if(img[h][w][c] + x < 255):
                            img[h][w][c] = img[h][w][c] + x
                        else:
                            img[h][w][c] = 255
                else:
                    if(img[h][w][c] < 255/2):
                        if(img[h][w][c] - x < 128):
                            img[h][w][c] = img[h][w][c] - x
                        else:
                            img[h][w][c] = 128
                    else:
                        if(img[h][w][c] + x > 128):
                            img[h][w][c] = img[h][w][c] + x
                        else:
                            img[h][w][c] = 128
    cv2.imshow('contrast image', img)
    cv2.waitKey(0)

def brightness(img, proc):
    x = 255 * proc * CONST / 100
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for c in range(img.shape[2]):
                if(x > 0):
                    if(img[h][w][c] + x < 255):
                        img[h][w][c] = img[h][w][c] + x
                    else:
                        img[h][w][c] = 255
                else:
                    if (img[h][w][c] + x > 0):
                        img[h][w][c] = img[h][w][c] + x
                    else:
                        img[h][w][c] = 0
    cv2.imshow('brightness image', img)
    cv2.waitKey(0)

def black_and_white(img, proc):
    c = proc / 100
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            t = (img[h][w][0] + img[h][w][1] + img[h][w][2]) / 3
            img[h][w][0] = (1 - c) * img[h][w][0] + c * t
            img[h][w][1] = (1 - c) * img[h][w][1] + c * t
            img[h][w][2] = (1 - c) * img[h][w][2] + c * t

    cv2.imshow('black and white image', img)
    cv2.waitKey(0)

def highlights(img, proc):
    x = 255 * proc * CONST / 100
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for c in range(img.shape[2]):
                if(img[h][w][c] > 127):
                    if(img[h][w][c] + x < 255):
                        img[h][w][c] = img[h][w][c] + x
                    else:
                        img[h][w][c] = 255
    cv2.imshow('highlights', img)
    cv2.waitKey(0)

def shadows(img, proc):
    x = 255 * proc * CONST / 100
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for c in range(img.shape[2]):
                if(img[h][w][c] < 128):
                    if(img[h][w][c] - x > 0):
                        img[h][w][c] = img[h][w][c] - x
                    else:
                        img[h][w][c] = 0
    cv2.imshow('shadows', img)
    cv2.waitKey(0)

def warmth(img, proc):
    x = 255 * proc * CONST / 100
    # c = proc / 100
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            # hsv_img[h][w][0] = (1 - c) * hsv_img[h][w][0] + c * 30
            if(hsv_img[h][w][1] + x < 255):
                hsv_img[h][w][1] = hsv_img[h][w][1] + x
            else:
                hsv_img[h][w][1] = 255

    img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imshow('warmth - saturation', img)
    cv2.waitKey(0)



if __name__ == '__main__':
    path = r'D:\Fakultet\Image processing\bmwix.jpg'
    img = cv2.imread(path)
    warmth(img, 100)
   # shadows(img, 100)
   # highlights(img, 10)
   # brightness(img,-100)
   # contrast(img,100)
   # black_and_white(img, 20)

