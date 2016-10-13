#! /usr/bin/env python

import numpy as np
import argparse
import os,sys
from PIL import Image

def run_script():
    parser = argparse.ArgumentParser(description='Steganography.')
    parser.add_argument('src', help='source file')
    parser.add_argument('secret', help='secret file')
    parser.add_argument('out', help='output file name')
    args = parser.parse_args()

    image = np.array(Image.open(args.src))
    secret = np.array(Image.open(args.secret))

    hid_av = np.average(secret)

    width  = min(secret.shape[0], image.shape[0])
    height  = min(secret.shape[1], image.shape[1])

    out = image[:width, :height, :]

    for x in range(width):
        for y in range(height):
            if secret[x,y,0] > hid_av:
                out[x,y,0] |= 1
            else:
                out[x,y,0] |= 1
                out[x,y,0] -= 1


    img = Image.fromarray(out, 'RGB')
    img.save( args.out )

    print "Encoded file %s written" % (args.out)

if __name__ == '__main__':
    run_script()
