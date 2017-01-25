# Problem 2 - Paying Debt Off in a Year
# 15.0 points possible (graded)

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

balance = 3329
annualInterestRate = 0.2

balance_copy = balance
monthlyFixedPayment = 10

while balance_copy > 0:
  for months in range(12):
    monthlyInterestRate = annualInterestRate/12.0
    minimumUnpaidBalance = balance_copy - monthlyFixedPayment
    balance_copy = minimumUnpaidBalance + (monthlyInterestRate * minimumUnpaidBalance)
  if balance_copy < 0:
    print("Lowest Payment: " + str(monthlyFixedPayment))
  else:
    balance_copy = balance
    monthlyFixedPayment += 10


# Lowest Payment: 310