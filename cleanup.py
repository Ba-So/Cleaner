# little script that can be used to clean output files of random origin.
# arose from the need of making the ICON output files csv readable.

# turns out quite the piece of work...

import os
import glob
import sys
import csv
from scipy import io as scio

class Data(object):

    def __init__(self, fpath):
        self.path   = fpath
        self.lines  = {}
        self.read_file()
        self.write_file()

    def read_file(self):
        """reads contents of a file line by line
            first line is assumed to contain variable names
            lines below are values in columns
        """
        file = open((self.path), 'r')
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            self.lines[i]   = Line(lines[i])

    def write_file(self):
        with open(self.path.strip('.dat') +'_clean.csv', 'w') as f:
            writer  = csv.writer(f, 
                                delimiter=',',
                                )
            for i in range(len(self.lines)):
                writer.writerows([self.lines[i].data])

class Line(object):

    def __init__(self, line):
        self.line   = line
        self.data   = []
        self.split()
        self.strip()
        self.split_comma()
        self.remove_empty()


    def split(self):
        self.data   = self.line.split(' ')

    def strip(self):
        nocomma     = []
        for string in self.data:
           nocomma.append(string.strip(',').rstrip())
        self.data   = nocomma

    def split_comma(self):
        commasplit   = []
        for string in self.data:
            newstrings  = string.split(',')
            for new in newstrings:
                commasplit.append(new)
        self.data   = commasplit

    def strip_whites(self):
        nowhites = []
        for string in self.data:
            nowhites.append(string.strip())
        self.data   = nowhites

    def remove_empty(self):
        noempties = []
        for string in self.data:
            if string:
               noempties.append(string)
        self.data   = noempties



if __name__== '__main__':
    cwd     = os.getcwd()
    for file in glob.glob('*.dat'):
        data    = Data(cwd+r'/'+file)
