# Problem 3 - Using Bisection Search to Make the Program Faster
# 20.0 points possible (graded)

# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!


balance = 999999
annualInterestRate = 0.18

balance_copy = balance
monthlyInterestRate = annualInterestRate / 12.0
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
lowerBound = balance / 12

while round(balance_copy, 2) != 0:
  monthlyFixedPayment = ((upperBound - lowerBound) / 2) + lowerBound
  for months in range(12):
    monthlyInterestRate = annualInterestRate/12.0
    minimumUnpaidBalance = balance_copy - monthlyFixedPayment
    balance_copy = minimumUnpaidBalance + (monthlyInterestRate * minimumUnpaidBalance)
  if round(balance_copy, 2) == 0:
    print("Lowest Payment: " + str(round(monthlyFixedPayment, 2)))
  elif balance_copy < 0:
    upperBound = monthlyFixedPayment
    balance_copy = balance
  elif balance_copy > 0:
    lowerBound = monthlyFixedPayment
    balance_copy = balance

# Lowest Payment: 90325.03