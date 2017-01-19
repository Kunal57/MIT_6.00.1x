# Problem 3
# 15.0 points possible (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'azcbobobegghakl'

alphabet = "abcdefghijklmnopqrstuvwxyz"
longest_substring = s[0]
current_substring = ""
previous_x_value = 0

for i in range(len(s)):
  for x in range(len(alphabet)):
    if s[i] == alphabet[x]:
      if len(current_substring) == 0:
        current_substring += s[i]
        previous_x_value = x
      elif x >= previous_x_value:
        current_substring += s[i]
        previous_x_value = x
        if len(current_substring) > len(longest_substring):
          longest_substring = current_substring
      elif x < previous_x_value:
          current_substring = s[i]
          previous_x_value = x

print("Longest substring in alphabetical order is: " + longest_substring)

