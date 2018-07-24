#Functions
def findMedian():
    """
    Takes low and high and finds the number in between.  If it is a decimal then it rounds down to an integer
    """
    
    global low, high
    #Enter code here and delete pass
    pass

def changeRange(higher):
    """
    Eliminates the numbers that we know cannot be the secret number
    If higher is true, set low as the computer guess.
    If higher is false, set high as the computer guess.
    """
    global low, high
    #Enter code here and delete pass
    pass


#Variables
secretNumber = 0
computerGuess = 50
low = 1
high = 100
guessCorrect = False
invalid = True

#Main loop

#To Do, write an input statement that asks the user for a secret number from 1 to 100.
#Store the input as the secret number

#To Do, write a logical statement that will check to see if the input is from 1 to 100.
#If it is continue, else write to the console "invalid number" and loop.

#To Do, write an input statement asking if the computer guess is the secret number,
#If the user enters "y", then set guessCorrect to True.
#If the user enters "n", then ask the user if the secret number is higher or lower.
#Else If the user enters anything write "Invalid Input" and loop.

#To Do, if the user enters "h", set higher as True
#if the user enters "l", set higher to False
#if the user enters anything else print "Invalid Input" and loop

#To Do, run changeRange.  Make sure to pass into it the variable higher

#To Do, run findMedian.  Set the result to computerGuess so that it is the computer's next guess.

#Outside the main loop
"""
If the program gets here it means that the computer has successfully guessed the secret number.
print 'yeah I was correct' or some other taunt message to the user.  The code will stop running after this.
"""






