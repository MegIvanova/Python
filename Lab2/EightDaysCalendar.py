import calendar
'''
Created on Sep 12, 2015

@author: meglena
'''

print ('###   Program Name: EightDaysCalendar   ###')
print('\nDescription: Program that outputs 5 calendars, each with 8 days per week, asking the user for the values of n and d each time.')

def main():

    count = 0
    while count < 5:
        if count > 0:
            print("\n")
        n = int(input("Input the number of days in the month (28-31): "))
        d = int(input("Input the starting day (0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thur, 5=Fri, 6=Sun, 7=Eight): "))
        count = count + 1
        for j in range(d):
            print("  ",end=" ") # Two times space!
        i = 1
        while i <= n:
            if i < 10: # In order to line up nicely all numbers, because some dates have one digit and some have two, we use less than 10! 
                print(" "+str(i), end=" ")
            else:
                print(i, end=" ")
            if (i + d) % 8 == 0:
                print(" ")
            i = i + 1
            
              
main() 


