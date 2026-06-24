# flake8: noqa
# 1 - Convert the input image in grayscale
# 2 - Split the image in M*N tiles
# 3 - Correct M (= rows) to match the image and font aspect ratio
# 4 - Compute the average brightness for each image tile then look up a suitable ASCII character for each.
# 5 - Assemble rows of ASCII character strings and print them to a file to form the final image.

from PIL import Image               # import module
from PIL.Image import Image as IM   # import object, alias for typing 
import numpy as np
import sys # remplacer en argparse


def get_avg_L(tile: IM):
    im = np.array(tile) # transform the tile in a grey-level matrix [[a,b,c], [d, e, f], ...]
    r, c = im.shape # get the dimension of the matrix 
    return np.average(im.reshape(r*c)) # reshape() is used to transform the entire matrix of r, c dimensions into a vector (matrix of 1 dim), and then calculate the mean value of the tile brightness

def main():
    # Make it CLI, default = 80 cols | 0.43 scale
    cols = 80 # It's the number of characters to form the width
    scale = 0.43

    # gscales = ramps, so the "definition" of the image, from darker to brighter char
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gscale2 = "@%#*+=-:. "

    # open the image and convert to grayscale, L for "luminance"
    image = Image.open("/Users/tod/Desktop/mario.png").convert("L")
    W, H = image.size[0], image.size[1]  # store the image dimensions, .size() returns a tuple.
    w = W/cols  # tile width, each ASCII char will represents a "w" pixel-width zone
    h = w/scale  # tile height based on aspect ratio AND font in order to correct the deformation of the ASCII char
    rows = int(H/h) # compute the number of rows to use in the final grid



if __name__ == "__main__":
    main()
