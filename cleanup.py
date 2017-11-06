# little script that can be used to clean output files of random origin.
# arose from the need of making the ICON output files csv readable.

# turns out quite the piece of work...

import os
import sys
import numpy as np
from scipy import io as scio

class Data(object):

    def __init__(self, fpath):
        self.path   = fpath
        self.lines  = self.read_file(fpath)
        self.line   = self.lines[0]

        #####################
        #++++++++++++++++++++
        ####################

# Problem here 'cuz when initializing the respective functions are called

        self.choices = choices 
        self.check  = True
        self.run()

    choices = {
                'b' : self.look_at_lines(),
                'c' : self.choose_line(),   
          #      'd' : self.remove_whites()
          #      'e' : self.remove_oddchars()
                'f' : self.save_n_exit(),
                'g' : self.exit()
                }

    def run(self):
        while self.check == True:
            self.look_at_line()
            print self.choices
            choice = raw_input("choose option")
            if choice not in choices:
                print "invalid choice"
                pass
            else:
                self.choices(choice)
            

    def exit(self):
        self.check  = False

    def save_n_exit(self):
        #saving
        self.exit()

    def look_at_line(self):
        """prints current line"""
        print self.line

    def look_at_lines(self):
        """prints multiple lines"""
        check = True
        while check:
            a = int(raw_input("choose line to start with"))
            b = int(raw_input("choose line to end with"))
            if a >= 0 & b >= a:
                check = False

        if a < b:
            for i in range(a,b,1):
                print self.lines[i]
        elif a == b:
            print self.lines[a]


    def choose_line(self):
        print "data set has {} lines".format(len(self.lines))
        a = int(raw_input("choose line to be edited"))
        self.line = self.lines[a]

    def remove_whites(self, strings):
        nowhites = []
        for string in strings:
            nowhites.append(string.strip())
        return nowhites

    def remove_oddchars(self, name):
        """removes all non chars or digits from a string"""
       
        chars = list(name)
        out_name = ''
        for char in chars:
            if char.isdigit() or char.isalpha():
                out_name += char
            else:
                pass
        return out_name

    def clean_oddchars(self, names):
        """removes all non chars or digits from array of strings"""
        out_names = []
        for name in names:
            out_names.append(remove_oddchars(name))
        return out_names

    def names_cleanup(self, names):
        """nasty cleanup routine"""
        # Maybe turn this one into split custom or something
        # where split and to be split are input
        # through a user interface
        # - fast alle sind via , getrennt
        c_names = np.array(names.split(','))
        # - nur der erste und zweite Eintrag nicht
        help = c_names[0].split()
        #print help
        # - rejoin scnd entry
        help = np.array([help[0], (help[1]+help[2])])
        # - der letzte Eintrag ist versehentlich mit . getrennt
        #help2 = np.array(c_names[len(c_names)-1].strip('.').split('.'))

        #help    = np.concatenate((help, c_names[1:len(c_names)-1], help2[0:2]))
        # - remove all spaces from strings
        names = remove_whites(c_names)
        return clean_oddchars(names)
       
    def resort_array(self, data):
        """Function changes from a column of lines
           to a line of columns.
           """
        # - length of lines. 
        lenx    = len(data[0])
        # - length of columns. 
        leny    = len(data) 
        out     = []
        # - step the lines
        for i in range(lenx):
            out.append([])
            # - step the columns
            for j in range(leny):
                out[i].append(data[j][i])
        
        return out

    def read_file(self, file_name):
        """reads contents of a file line by line
        
            first line is assumed to contain variable names
            lines below are values in columns
        """

        file = open((file_name), 'r')
        lines = file.readlines()
        file.close()

        return lines
        
   #     data = []
   #     names= names_cleanup(lines[0])

    #    for line in lines[1:]:
    #        a = line.split() 
    #        data.append([float(i) for i in a])

     #   data        = resort_array(data)
     #   data_dict   = {}
     #   for i in range(len(names)):
     #       data_dict[names[i]] = data[i][:]

      #  return data_dict 

if __name__== '__main__':
    cwd     = os.getcwd()
    fname = raw_input("input file in {} you'd like to be cleaned up:\n".format(cwd)) 
    print "preparing {} for cleanup".format(fname)
    data    = Data(cwd+fname)


