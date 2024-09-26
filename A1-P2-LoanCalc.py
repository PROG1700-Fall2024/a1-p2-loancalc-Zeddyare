#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #starting with math things again
    #weekly amount is going to be the total value divided by years and then divided by 52
    #interest rate has to be applied before any division

    #Program name
    print("Weekly Loan Calculator\n")

    #input for loan amount
    loanAmt=input("Enter the amount of loan: ")

    #input for interest rate
    interest=input("Enter the interest rate (%): ")

    #input for years
    years=input("Enter the number of years: ")
    print(" ") #again unsure how to make a blank line after an input that doesnt put the input area below

    #math time
    interestRate=(float(interest)/5200)
    weeklyPay=(float(interestRate)/(1-(1+float(interestRate))**(-52*int(years))))*float(loanAmt)
    #I had an entire other way of doing this math and it ended up like $3 off
    #copying the formula off the assignment page worked great (shocker!!!)
    #being good at math vs knowing how it works is so clear now

    #output for weekly payments
    print("Your weekly payment will be: ${0:.2f}".format(weeklyPay))






    # YOUR CODE ENDS HERE

main()