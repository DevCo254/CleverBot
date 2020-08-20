print('Enter your name : ')
x = input()
print('hello '+ x)
print('Your Interest calculator')

print('Enter 1 for compound interest, or 2 for simple interest')
y = input()
if y == 1:
    P = int(input("Enter starting principle please. "))
    n = int(input("Enter Compound intrest rate.(daily, monthly, quarterly, half-year, yearly) "))
    r = float(input("Enter annual interest amount. (decimal) "))
    t = int(input("Enter the amount of years. "))
    final = (P * (((1 + (r/n)) ** (n*t))))+P
else :
    print('Principal amount :')
    P = int(input())
    print('Time :')
    t = int(input())
    print('Interest rate :')
    r = float(input())

    final = ((P*r*t)/100)+P
print ("The final amount after", t, "years is", final)