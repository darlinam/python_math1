# CS 101 Project II CSFinalProject.py
#Name: Alexandra Darling and Susan Minnich

import math

#Locates quadrant of point A and B

def quad( ):

    # Input the coordinates for point A 
    x = float(input('Enter x varaible: '))
    y = float(input('Enter y variable: '))
    #Input the coordinates for point B
    x1 = float(input('Enter x1 varaible: '))
    y1 = float(input('Enter y1 varaible: '))

    #Point A
    if x > 0:

        #First quadrant
        if y > 0:

            print ("Both x and y variables were positive so point A is in the first quadrant!")

        #Fourth quadrant
        elif y < 0:

             print("The x variable was positive and the y variable was negative so point A is in the fourth quadrant!")

        #x-axis
        else:

            print("The y varibable equals zero so point A lies on the x-axis!")

    elif x < 0:

        #Second quadrant
        if y > 0:

            print("The x variable was negative and the y variable was positive so point A is in the second quadrant!")

        #Third quadrant
        elif y < 0:

            print("Both x and y variables were negative so point A is in the third quadrant!")

        else:

             print("The y variable equals zero so point A lies on the x-axis!")           
    
    #x and y axis
    elif x == 0 and y == 0:

        print("The point A lies on both the x and y axis!")

    #y-axis
    else:

        print("The x variable equals zero so point A lies on the y-axis!")

    #Point B
    if x1 > 0:

        #First quadrant
        if y1 > 0:

            print ("Both x and y variables were positive so point B is in the first quadrant!")

        #Fourth quadrant
        elif y1 < 0:

             print("The x variable was positive and the y variable was negative so point B is in the fourth quadrant!")

        #x-axis
        else:

            print("The y varibable equals zero so point B lies on the x-axis!")

    elif x1 < 0:

        #Second quadrant
        if y1 > 0:

            print("The x variable was negative and the y variable was positive so point B is in the second quadrant!")

        #Third quadrant
        elif y1 < 0:

            print("Both x and y variables were negative so point B is in the third quadrant!")

        else:

             print("The y variable equals zero so point B lies on the x-axis!")           
    
    #x and y axis
    elif x1 == 0 and y1 == 0:

        print("The point B lies on both the x and y axis!")

    #y-axis
    else:

        print("The x variable equals zero so point B lies on the y-axis!")

    
    over = str(input("Do you want to know the distance between the two points? "))

    if over == "yes" or over == "y":
    
        #Computes distance
        distance = math.sqrt(((x - x1)**2) + ((y - y1)**2))

        print("The distance from point A to point B is" , distance)

    else:

        print("OK!")
 

def main( ):

        answer = str(input("Hey there student! Do you want to learn about the xy plane? "))

# If the gamer wants to play the game

        while answer == "yes" or answer == "y":

             quad( )

             answer = str(input("Hey there student! Do you want to try again? "))
  
# If the gamer wants to stop playing the game
  
        print("GOOD BYE")

main( )

        
