from PIL import Image
import os
import sys

paths = [path for path in os.listdir() if (not(path.endswith('.jpg')) and not(path.endswith('.py')))]


def cvt(x):
    x = x.convert('RGB')
    return x

for path in paths:

    image_names = [image for image in os.listdir(path) if not(image.endswith('.pdf'))]

    images = []

    for image in image_names:
        page = Image.open(f'{path}/{image}')
        page.load()
        images.append(page)
        exif_data = page._getexif()


    map(cvt, images)

    im_1 = images[0]


    im_1.save(f'{path[17:]}.pdf', save_all=True, append_images=images[1:])
