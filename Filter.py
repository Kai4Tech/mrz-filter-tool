from PIL import Image, ImageEnhance

def increase_contrast(img_name, level):  # 0~127
    image = Image.open(img_name).convert("RGBA")
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c):
        value = 128 + factor * (c - 128)
        return max(0, min(255, value))
    new_frame = image.point(contrast)
    path = frame_save(img_name, new_frame)
    return path, new_frame


def increase_contrast2(img_name, level):  # 0~3, 1 is original
    image = Image.open(img_name).convert("RGBA")
    factor = ImageEnhance.Contrast(image)
    factor_im = factor.enhance(level)
    path = frame_save(img_name, factor_im)
    return path, factor_im


def increase_brightness(img_name, level):  # 0~5 , 1 is original
    image = Image.open(img_name).convert("RGBA")
    factor = ImageEnhance.Brightness(image)
    factor_im = factor.enhance(level)
    path = frame_save(img_name, factor_im)
    return path, factor_im


def frame_save(name, factor):
    if name.find('filtered') == 7:
        path = name
    else:
        path = 'images/filtered/{}.png'.format(name[7:-4])
    factor.save(path)
    return path


if __name__ == '__main__':
    filename = 'images/passport_06.jpg'

    frame = increase_brightness(filename, 3)

    print(frame)

    # frame = increase_contrast2(Image.open(file), 5)
    #
    # frame = increase_brightness(frame, 1)

    # frame.save('images/filtered/{}2.png'.format(filename))

