# Problem 1
# 10.0 points possible (graded)
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = 'azcbobobegghakl'

vowels = "aeiou"
num_of_vowels = 0

for letter in s:
  if letter in vowels:
    num_of_vowels += 1

print("Number of vowels: " + str(num_of_vowels))