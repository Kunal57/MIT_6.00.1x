# Grader
# 10.0 points possible (ungraded)
# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

from math import tan, pi

def polysum(n, s):
  """ calculate the sum of the perimeter and area of the polygon """
  perimeter_squared = (n * s)**2

  fraction_top = (.25 * n) * (s**2)
  fraction_bottom = tan(pi/n)

  area = fraction_top/fraction_bottom

  return round(perimeter_squared + area, 4)

print(polysum(52, 78))