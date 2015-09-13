'''
Created on Sep 11, 2015

@author: Meglena
'''

print ('###   Program Name: LeapYearFinder   ###')
print('\nDescription: Program that shows you a leap year or not when you enter a year.')

year = int(input("\nEnter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year.".format(year))
        else:
            print("{0} is NOT a leap year.".format(year))
    else:
        print("{0} is a leap year.".format(year))
else:
    print("{0} is NOT a leap year.".format(year))
    
#   result 
#   Enter a year: 2000
#   2000 is a leap year.