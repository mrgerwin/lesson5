# lesson5
Mini-Project Number Guess Game

This is the first mini-project.  You have learned enough to program some fairly intelligent programs.  In this mini-project you will make a program that will guess a user's number with the fewest number guesses possible.

I will guide you through the program with a series of steps, but you can take detours.  In fact, trying things out on your own is probably one of the better ways to learn in computer science.  

Overview:  The program will first ask the user for a number between 1 and 100.  The program will check to see if the user typed in a valid choice.  Then it will run a while loop where it will guess a number (it will select the median), and if wrong will ask if the number is higher or lower.  That will logically eliminate half of the numbers as possibilities so it will guess the median of the range that is possible.  Eventually, the computer will guess the correct number.  This is called binary search .

1. Use the template NumberGuess.py
2. Write a function named findMedian that will take the global variables low and high and determine an integer value that is between the numbers and return it.  If the median is a decimal then round it to an integer value or use integer division. (hint: find the halfway distance between both values and add it to the low value)
3. Write a function named changeRange that will take the variable higher and use global variables low and high.  If higher is True it will set the low variable as the computerGuess else if higher is False it will set the high variable as the computerGuess.  There will be no return statement.
4. Write an input statement that asks the user to type a secret number between 1 and 100 in the console and store it in the variable secretNumber.
5. If secretNumber is in the correct range continue to the next steps, else print “invalid number” and end program.
6. If secretNumber is in the correct range, write a while loop that uses guessCorrect to determine if it should run, if guessCorrect is False run the loop.
7. In the while loop, make an input statement on the console asking if the computerGuess number is correct.  Store the input in a temporary variable.  If the user types anything other than “y” or “n”, then it should loop and repeat the question.  If the user types “y”, then set guessCorrect to True.  Else if the user types “n”, then keep guessCorrect as False and ask the user if it is higher or lower.  
8. Ask the user if the number is higher or lower, give them the options ‘h’ or ‘l’.
9. If the user enters ‘h’ then set higher as True, else if the user enters ‘l’ set higher as False.  If the user enters anything else, you should repeat the question. (hint: use a while loop and the invalid variable to keep track if you should keep looping and asking the question.
1. Once this step is complete run the changeRange function passing it the variable higher.
2. Then set the computerGuess variable to the result of the findMedian function
3. End the while statement by not indenting the next line.
4. Outside the while loop print “Yeah I was correct!” or some other taunt message from the computer.

Think about how you could use a while loop to run the program multiple times if the user wants to play again.  If you have time, change the program.  Peer review someone else’s project.

### Debug
#### See if these scenarios are handled correctly
* The user’s secret number is lower than 0
* The user’s secret number is above 100
* The user’s secret number is 100
* The user’s secret number is 1
* The user’s secret number is a random odd number above 50 but below 100
* The user’s secret number is a random odd number below 50 but above 1
* Anything else you can think of.

I understand that there are multiple ways to write this program.  I purposely used steps that would expose your understanding of functions, while loops, and if statements.  You might find a more concise way that is also correct in addressing the program.
