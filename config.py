# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:46:02 2020

@author: Fandy
Main Program for Solving 1D Acoustic Wave Equation Based on 2nd Order Finite Difference
An Exercise to Create 1D Wave Propagation Simulation
Input File= ParFile Contains Details of Geometry
            SrcFile Contains Details of Source Parameter
For Current Program the Source Function is limited to the first derivative of Gaussian Function (Only)
"""


try:
    # Python 3
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser


class FakeGlobalSectionHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[global]\n'

    def readline(self):
        if self.sechead:
            try:
                return self.sechead
            finally:
                self.sechead = None
        else:
            return self.fp.readline()

class Parameter(object):
    def __init__(self):
        cp = SafeConfigParser(defaults={
            'NX': 10001,
            'XMAX': 10000,
            'C0': 334,
            'NT': 1001,
            'DT': 0.001,
            'Freq': 25,
        })
        with open('ParFile') as f:
            try:
                cp.read_string('[global]\n' + f.read(), source='Par_file')
            except AttributeError:
                # Python 2
                cp.readfp(FakeGlobalSectionHead(f))
    
        self.nx = cp.getint('global','NX')
        self.xmax = cp.getint('global','XMAX')
        self.c0 = cp.getint('global','C0')
        self.nt = cp.getint('global','NT')
        self.dt = cp.getfloat('global','DT')
        self.gx = cp.getint('global','GX')
        self.freq = cp.getint('global','Freq')
        self.sx = cp.getint('global','SX')
        self.snap = cp.getint('global','SNAP')
    
    
