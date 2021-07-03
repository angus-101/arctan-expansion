#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:25:02 2018
"""

import math         


def MyArcTan(x,N):                                                              #Lines 10 - 37 are the creation of the function MyArcTan
    
    arctan = float(0)                                                           #Initialises the variable arctan
    
    if abs(x) <= 1:                                                             #Case of |x| < 1
        
        for n in range(0,N + 1):                                                            
            arctan += (((-1) ** n)*(x ** (2 * n + 1)))/(2 * n + 1)              #Calculates arctan using the forumla and adds it to the former arctan, updating it       
            n += 1                                                                          
    
    elif x > 0:                                                                 #Case of |x| > 1 and x > 0
        
        for n in range(0,N + 1):                                                    
                arctan += ((((-1) ** n)*((1 / x) ** (2 * n + 1)))/(2 * n + 1))      
                n += 1
            
        arctan = math.pi / 2 - arctan
        
    else:                                                                       #Case of |x| > 1 and x < 0
        
        for n in range(0,N + 1):                                                    
                arctan += ((((-1) ** n)*((1 / x) ** (2 * n + 1)))/(2 * n + 1))     
                n += 1
            
        arctan = -(math.pi / 2) - arctan                                                                        
        
            
    return arctan
    

MyInput = '0'

while MyInput != 'q':
    
    MyInput = input('Enter a choice, "a", "b" or "q" to quit: ')
    print('You entered the choice: ' + MyInput)

    if MyInput == 'a':
        
        print('You have chosen part (a)')
        x = float(input('Enter a value for x (floating point number): '))       #Shortened the x and N variables to a single line
        N = int(input("Enter a value for N (positive integer): ")) 
        
        while N < 0:                                                            #While loop to make sure N is positive
            print("N must be a positive integer!")
            N = int(input("Enter a value for N (positive integer): "))                      
        
        print('The answer is: ' + str(MyArcTan(x,N)))

    elif MyInput == 'b':
        
        print('You have chosen part (b)')
        N = int(input('Enter a value for N (positive integer): '))
        
        while N < 0:                                                            #While loop to make sure N is positive
            print("N must be a positive integer!")
            N = int(input("Enter a value for N (positive integer): "))
        
        print("|x    |N        |MyArcTan value          |Python arctan value      |Difference             |")   #This prints the headings for the table of values        
        
        for i in range(-200,201):                                                                               #i varies between -200 and 200 to better show changes in the difference between the approximation and the real value of arctan
            
            x = i/100
            row_i = "|" + str(x) + " "*int(5-len(str(x))) + "|" + str(N) + " "*int(9-len(str(N))) + "|" + str(MyArcTan(x,N)) + " "*(24-len(str(MyArcTan(x,N)))) + "|" + str(math.atan(x)) + " "*(25-len(str(math.atan(x)))) + "|" + str(abs(MyArcTan(x,N)-math.atan(x))) + " "*(23-len(str(abs(MyArcTan(x,N)-math.atan(x))))) + "|"                                                                                                  
            print(row_i)                                                                                        #The line above sets up each row of the table, allowing for excess space in each element to make it look nice
                                                                                                                #If the columns do not all fit in the console, simply widen the console
    elif MyInput != 'q':
        
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')
