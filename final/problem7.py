# Problem 7
# 20.0 points possible (graded)
# Write a function called general_poly.

def general_poly(L):
  """ L, a list of numbers (n0, n1, n2, ... nk)
  Returns a function, which when applied to a value x, returns the value
  n0 * x^k + n1 * x^(k-1) + ... nk * x^0
  """
  numList = L[::-1]

  def apply(number):
    value = 0
    for i in range(len(numList)):
      result = numList[i] * (number ** i)
      value += result
    return value

  return apply



L = [1, 2, 3, 4]
print(general_poly([1, 2, 3, 4])(10))