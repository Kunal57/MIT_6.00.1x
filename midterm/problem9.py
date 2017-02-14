# Problem 9
# 15.0 points possible (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.

def flatten(aList):
  '''
  aList: a list
  Returns a copy of aList, which is a flattened version of aList
  '''
  if not aList:
    return []
  if type(aList[0]) == list:
    return flatten(aList[0]) + flatten(aList[1:])
  else:
    return [aList[0]] + flatten(aList[1:])


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
bList = [1,2,3,4,[5,6]]
print(flatten(aList))