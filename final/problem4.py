# Problem 4
# 20.0 points possible (graded)
# You are given the following definitions:

# A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
# A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.

# Implement a function that meets the specifications below.

def longest_run(L):
  """
  Assumes L is a list of integers containing at least 2 elements.
  Finds the longest run of numbers in L, where the longest run can
  either be monotonically increasing or monotonically decreasing.
  In case of a tie for the longest run, choose the longest run
  that occurs first.
  Does not modify the list.
  Returns the sum of the longest run.
  """
  longestIncreasingRun = []
  longestDecreasingRun = []

  increasingRun = []
  decreasingRun = []
  for i in range(len(L)):
    if len(increasingRun) == 0:
      increasingRun.append(L[i])
      decreasingRun.append(L[i])
    elif L[i] == increasingRun[-1]:
      increasingRun.append(L[i])
      decreasingRun.append(L[i])
    elif L[i] > increasingRun[-1]:
      increasingRun.append(L[i])
      decreasingRun = [L[i]]
    elif L[i] < decreasingRun[-1]:
      decreasingRun.append(L[i])
      increasingRun = [L[i]]
    if len(increasingRun) > len(longestIncreasingRun):
      longestIncreasingRun = increasingRun
    if len(decreasingRun) > len(longestDecreasingRun):
      longestDecreasingRun = decreasingRun


  if len(longestIncreasingRun) > len(longestDecreasingRun):
    return sum(longestIncreasingRun)
  elif len(longestDecreasingRun) > len(longestIncreasingRun):
    return sum(longestDecreasingRun)
  else:
    for i in range(len(L)):
      if L[i] == longestIncreasingRun[0]:
        if L[i + len(longestIncreasingRun) - 1] == longestIncreasingRun[-1]:
          return sum(longestIncreasingRun)
      elif L[i] == longestDecreasingRun[0]:
        if L[i + len(longestDecreasingRun) - 1] == longestDecreasingRun[-1]:
          return sum(longestDecreasingRun)




# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# Increasing is [3, 4, 5, 7, 7], Decreasing is [10, 4, 3]
# Answer is 26 since the longer run is the increasing list (3+4+5+7+7 = 26)
L = [-1, -10, -10, -10, -10, -10, -10, -100]
print(longest_run(L))