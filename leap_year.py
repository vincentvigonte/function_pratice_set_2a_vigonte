'''
A program that contains a function which determines if a year is a leap year or not
'''

def leap_year(year):
    '''
    Determines the year whether it a leap year ot not

    Args:
        year = the year that will be determine if its leap year or not

    Return
        The whether its leap year or not
    '''
    if (year % 4 == 0 & year % 100 != 0) or (year % 400 == 0): #computes and determine if the year given is a leap year or not
        return True #return true if the year is a keap year
    else:
        return False #return false if the year is not a leap year
    
year = int(input("Enter the year: ")) #accepts the year you want to determine if it is a leap year or not

if leap_year(year):
    print(year, "is a leap year.") #print it is a leap year 
else:
    print(year, "is not a leap year") #print it is not a leap year