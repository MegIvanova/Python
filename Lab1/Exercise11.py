'''
Created on Sep 8, 2015

@author: meglena
'''
#Python Program to Print all factorials Numbers in an Interval 0 to 20
import math
def main():
    n = 0
    
    for n in range (20):
        f = math.factorial(n)
        print (n,"! = ", f)

 
main()