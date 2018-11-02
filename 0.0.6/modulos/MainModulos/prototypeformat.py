#prototype_format.py
#!-*- coding:utf-8 -*-

import datetime
import os

class FormatString:

    """
    The class is for smarth formating a string on the terminal
    """
    terminal = os.get_terminal_size()
    terminal_columns = terminal.columns #pass the columns from terminal
    terminal_lines = terminal.lines # pass the lines from terminal

    def formatDate(self, string, boolean=False):
        """
        Format a string to add time before
        """
        self.s = string
        self.b = boolean
        now = datetime.datetime.now()
        if self.b == True:
            return "\n>> {}: {}".format(now.strftime("[%d-%m-%y/%H:%M]"), self.s)
        elif self.b == False:
            #formating the output
            return ">> {}: {}".format(now.strftime("[%d-%m-%y/%H:%M]"), self.s)

    def formatCenter(self, string, mode=None):
        """
        Format a string to:
        if the second argument is "CENTER", the string will be centered 
        on the terminal.
        if the second argument is a NUMBER, the string will be whataver user 
        want to be.
        """
        self.s = string
        self.mode = mode
        if self.mode == "CENTER":
            return "{:^{}}".format(self.s, self.terminal.columns)
        else:
            return "{:^{}}".format(self.s, self.mode)

    def formatMenu(self, string):
        self.s = string
        return "\n".join(map(str, self.s))
