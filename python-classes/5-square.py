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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # If value is not an integer
            raise TypeError("size must be an integer")
        elif value < 0:  # If value is negative
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' Function to calculate the area of the square '''
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
