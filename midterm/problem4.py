# Problem 4
# 10.0 points possible (graded)
# Implement a function called closest_power that meets the specifications below.

# For example,

# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

def closest_power(base, num):
  '''
  base: base of the exponential, integer > 1
  num: number you want to be closest to, integer > 0
  Find the integer exponent such that base**exponent is closest to num.
  Note that the base**exponent may be either greater or smaller than num.
  In case of a tie, return the smaller value.
  Returns the exponent.
  '''
  num = int(num)
  difference = base**num
  integerExponent = num
  exponents = range(0, num)
  for exponent in exponents:
    exponentValue = base**exponent
    if abs(exponentValue - num) < difference:
      difference = abs(exponentValue - num)
      integerExponent = exponent
    else:
      break
  return integerExponent


print(closest_power(10, 550.0))
