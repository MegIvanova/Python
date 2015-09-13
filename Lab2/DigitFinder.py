'''
Created on Sep 12, 2015

@author: meglena
'''

print ('###   Program Name: DigitFinder   ###')
print('\nDescription: Program that finds and sums all digits in a string.')
print("Example: '2,3,6.0,bananas,Python,34'")

# input validation
hasNumber = False
hasLatter = False
hasSeparator = False

displayFirstInputMessage = True

while (hasNumber == False or hasLatter == False or hasSeparator == False):
        
    if displayFirstInputMessage:
        userinput = input("\nEnter a combination of digits and letters separated by comma: ")
        displayFirstInputMessage = False
    else:
        userinput = input("\nYour input is incorrect. Please enter a combination of digits and letters separated by comma: ")
    
    for char in userinput:
        if char.isdigit():  # for string objects; checks if a character in a string is a number (float).
            hasNumber = True
        elif char == ',':
            hasSeparator = True
        else:
            hasLatter = True
            

userinput.translate(' ') # translate(' ') deletes the unwanted characters  
components = userinput.split(",")  # .split() splits the string where "," is the delimiter
digitSum = 0
for i in components:
    try:
        number = float(i)
        digitSum += float(number)
    except:
        continue
               
print('The Sum of all integers is: ', digitSum) 

#    result
#    ###   Program Name: DigitFinder   ###
#    Description: Program that finds and sums all digits in a string.
#    Example: '2,3,6.0,bananas,Python,34'
#    Enter a combination of digits and letters separated by comma: a, 2, 0.4
#    The sum of all integers is:  2.4


