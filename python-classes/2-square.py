#!/usr/bin/python3
''' This module is about checking exceptions '''


class Square:
    ''' This class checks exceptions '''
    def __init__(self, size=0):
        ''' This function will check the type of the size and
        will compare with 0 '''
        if not isinstance(size, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        elif size < 0:  # If size is negative
            raise ValueError("size must be >= 0")

        self.__size = size
