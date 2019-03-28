#!/usr/bin/python

import numpy as np
import sys
import getopt
from scipy import misc
import matplotlib.pyplot as plt

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

print( np.__version__ )

np_array = np.array([[ 0,  1,  2,  3,  4],
                     [ 5,  6,  7,  8,  9],
                     [10, 11, 12, 13, 14]])

print( np_array )

#
# save/load operation on numpy array
#
print( "Wrtite to file" )

np.save( 'outfile', np_array )

print( "Load from file" )

np_array_load = np.load('outfile.npy') 

print( np_array_load )

#
# read image data
#
def process_img_file( filename ):

    print( "process_img_file() is called" )

    #f = misc.face()
    #misc.imsave( filename, f) # uses the Image module (PIL)

    f = misc.imread( filename )
    plt.imshow(f)
    plt.show()


def main(argv):

    inputfile = ''
    outputfile = ''

    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

    process_img_file( inputfile )

if __name__ == "__main__":
   main(sys.argv[1:])
