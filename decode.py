#! /usr/bin/env python

import numpy as np
import argparse
import os,sys
from PIL import Image

def run_script():
    parser = argparse.ArgumentParser(description='Steganography.')
    parser.add_argument('src', help='source file')
    parser.add_argument('out', help='output file name')
    args = parser.parse_args()

    image = np.array(Image.open(args.src))
    width = image.shape[0]
    height = image.shape[1]

    out = np.zeros((width, height, 3), dtype = np.uint8)

    for x in range(width):
        for y in range(height):
            if image[x,y,0] & 1 == 1:
                out[x,y,0] = 255
                out[x,y,1] = 255
                out[x,y,2] = 255

    img = Image.fromarray(out, 'RGB')
    img.save( args.out )

    print "Decoded file %s written" % (args.out)


if __name__ == '__main__':
    run_script()
