#!/usr/bin/python3
'''
Pascal triangle function
'''
from math import factorial


def pascal_triangle(n):
    '''
    Returns representation of the pascal triangle using n
    '''
    if n <= 0:
        return []

    else:
        for i in range(n):
            for j in range(n-i+1):

                # creates left spacing
                print(end=" ")

            for j in range(i+1):

                # nCr = n!/((n-r)!*r!) formula of pascal triangle
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

            # new line
            print()
