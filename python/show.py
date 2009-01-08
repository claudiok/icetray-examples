#!/usr/bin/python

"""
Print the table of contents of the first physics frame
in a .i3 file.
"""

import sys
from icecube import icetray, dataclasses, dataio

def main():
    i3f = dataio.I3File(sys.argv[1])

    frame = i3f.pop_physics()

    print frame

if __name__ == '__main__':
    main()

    
