#!/usr/bin/python3
'''Create fnctn 2 return list of list of ints rprsnt Pascals triangle of n'''
'''Returns an empty list if n <= 0,assume n will be always an integer'''

def pascal_triangle(n):
    n = input(int("Enter int valueof n:"))

    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//factorial(j)*factorial(i-j)), end=" ")
        print()
    return()
