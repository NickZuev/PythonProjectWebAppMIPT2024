from PIL import Image, ImageChops

import matplotlib.pyplot as plt
import io


def latex_to_img(tex):
    white = (255, 255, 255, 255)
    buf = io.BytesIO()
    plt.rcParams["figure.figsize"] = (20,5)
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.05, 0.5, f'${tex}$', size=40)
    plt.savefig(buf, format='png')
    plt.close()

    im = Image.open(buf)
    bg = Image.new(im.mode, im.size, white)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return im.crop(bbox)