finalAccountValue = eval(input("Enter final account value:"))
annualInterestRate = eval(input("Enter annual interest rate in percent:"))
numOfYears = eval(input("Enter number of years:"))

monthlyInterestRate = annualInterestRate / 100 / 12
numberOfMonths = numOfYears * 12

initialDeposit = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths

print("Initial deposit value is ", initialDeposit)


'''
Assume you pay interest monthly at 10 percent per year. What is your monthly interest rate 
and how much will you pay (or earn) on $100?

Convert the annual rate from percentage to decimal format (by dividing by 100)
10/100 = 0.1 annually
Divide the annual rate by 12
0.10/12 = .0083
Calculate the monthly interest on $100
0.0083 x $100 = $0.83
Convert the monthly rate in decimal format back to a percentage (by multiplying by 100)
0.0083 x 100 = 0.83 percent annually
'''
