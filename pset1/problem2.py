# Problem 2
# 10.0 points possible (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'qoboboboboobobobobbobobcoboboqobo'
num_of_times = 0

for i in range(len(s)):
  if i <= len(s) - 3:
    if (s[i] == "b") and (s[i+1] == "o") and (s[i+2] == "b"):
      num_of_times += 1
      i = i + 2

print("Number of times bob occurs is " + str(num_of_times))