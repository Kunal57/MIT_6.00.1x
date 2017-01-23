# Exercise: guess my number
# 10.0 points possible (graded)
# ESTIMATED TIME TO COMPLETE: 15 minutes

# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

# Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

print("Please think of a number between 0 and 100!")


answer = ""
number = 50
low = 0
high = 100

while answer != "c":
  print("Is your secret number " + str(number))

  answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

  if answer == "c":
    print("Game over. Your secret number was: " + str(number))
  elif answer == "h":
    high = number
    number = int(((high - low)/2) + low)
  elif answer == "l":
    low = number
    number = int((high + low)/2)
  else:
    print("Sorry, I did not understand your input.")
