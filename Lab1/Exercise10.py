'''
Created on Sep 8, 2015

@author: meglena
'''
# Python Program to convert temperature in Celsius to Fahrenheit
# Input is provided by the user in degree Celsius
 
def main():
    tempC = float(input("Input the temperature in Celsius: "))
    tempF = 9.0/5.0 * tempC + 32
    print("The temperature in Fahrenheit is: ", tempF, "F")
 
main()
