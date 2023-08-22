'''
A program that contains a function which calculate the are of a triangle usinig heron's formula
'''

def calculate_area_triagle(a, b ,c):
    '''
    Calculates the area of the tringles using it three sides

    Args:
        a = the lenght of side a
        b = the lenght of side b
        c = the lenght of side c

    Return
        The calculated area of the tringle
    '''

    half_piremeter = (a + b + c) / 2 #calculates half of the piremeter of the triangle

    area = (half_piremeter * (half_piremeter - a ) * (half_piremeter - b) * (half_piremeter - c)) ** 0.5 #calculates the area of the triangle using the heron's formula

    return area #returns the calculated area of the triangle

#accepts the length of each side of the triangle
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

final_area = calculate_area_triagle(side_a, side_b, side_c) #calculates the area
print("The area of the triangle is : ", final_area) #prints the area


