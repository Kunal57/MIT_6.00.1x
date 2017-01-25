# Problem 1 - Paying Debt off in a Year
# 10.0 points possible (graded)

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# given variables
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# counter (12 months in a year)
months = 12

# 12 month loop
while months > 0:
  monthlyInterestRate = annualInterestRate/12.0
  minimumMonthlyPayment = balance * monthlyPaymentRate
  minimumUnpaidBalance = balance - minimumMonthlyPayment
  balance = minimumUnpaidBalance + (monthlyInterestRate * minimumUnpaidBalance)
  months -= 1

print("Remaining balance: " + str(round(balance, 2)))


# Remaining balance: 31.38




# RECURSIVE SOLUTION

# def payingDebt(balance, annualInterestRate, monthlyPaymentRate, months):
#   if months == 0:
#     print("Remaining balance: " + str(round(balance, 2)))
#     return balance
#   else:
#     monthlyInterestRate = annualInterestRate/12.0
#     minimumMonthlyPayment = balance * monthlyPaymentRate
#     minimumUnpaidBalance = balance - minimumMonthlyPayment
#     updatedBalanceEachMonth = minimumUnpaidBalance + (monthlyInterestRate * minimumUnpaidBalance)

#     return payingDebt(updatedBalanceEachMonth, annualInterestRate, monthlyPaymentRate, months - 1)


# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# months = 12

# payingDebt(balance, annualInterestRate, monthlyPaymentRate, months)