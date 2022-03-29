#Imports modules (You may have to import in your own script)
from time import sleep
from tkinter import *

def pack(): #Creates a function called pack() that stores all the functions
    def wait(x): #Creates a function called wait() to make sleep() look better
        #You call the function using wait() and in the () type how long it has to wait (in seconds)
        sleep(x) #Calls sleep()

    def out(var): #Creates a function called out() to make print() look better
        #You call the function using out() and in the () type what you want to print
        print(var) #Calls print()
    
    def add(x, y): #Creates a function called add() to add 2 numbers together
        #You call the function using add() and in the () type the numbers you want to add together
        global num #Declares a global variable called num which will have the output value
        num = x + y #Sets the variable to the sum of x and y
     
    def win(x, y): #Creates a function called win() to make a tkinter window easily
        win = Tk() #Creates the window
        win.geometry(x) #You pass the string with the size to x (e.g. "400x200") and set it as the size
        win.title(y) #This sets y as the title for the window

#Now some fun for later:
#Does a set of all sets contain itself?















#Idk why I did this