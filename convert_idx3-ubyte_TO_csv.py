#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:12:32 2019

@author: anurag
"""
def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

convert("/home/anurag/Downloads/train-images.idx3-ubyte", "/home/anurag/Downloads/train-labels.idx1-ubyte",
"/home/anurag/Downloads/mnist_train.csv", 60000)
convert("/home/anurag/Downloads/t10k-images.idx3-ubyte", "/home/anurag/Downloads/t10k-labels.idx1-ubyte",
"/home/anurag/Downloads/mnist_test.csv", 10000)