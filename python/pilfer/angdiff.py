#!/usr/bin/env python

from numpy import arccos,sin,cos

def diff(zen1,azi1,zen2,azi2) :
    return arccos(sin(zen1)*sin(zen2)*(sin(azi1)*sin(azi2)+cos(azi1)*cos(azi2))+cos(zen1)*cos(zen2))

