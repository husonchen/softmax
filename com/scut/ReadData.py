#encoding:utf-8
'''

Created on Apr 18, 2016

@author: husonchen
'''
import numpy as np 
import struct
from PIL import Image
import struct
from numpy import *

def read(filename):
    data = zeros((60000,784))
    f = open(filename,'rb')
    
    index = 0
    buf = f.read()
    f.close()
    magic,images,rows,columns = struct.unpack_from('>IIII',buf,index)
    index += struct.calcsize('>IIII')
    
    for i in xrange(images):
        for x in xrange(rows):
            for y in xrange(columns):
                pix = int(struct.unpack_from('>B',buf,index)[0])
                data[i][x*28 + y] = pix
                index += struct.calcsize('>B')
    return data


if __name__ == '__main__':
    data = read("train-images.idx3-ubyte")
    print data