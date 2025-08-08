'''we know that complex interest is with formula A = P(1 + r/n)^(nt)'''
principal=int(input("Enter the innitial amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time in years:"))
p= principal
r= round(rate)
t= round(time)
A= p * (1 + r/100)**t
print("The amount after", t, "years is:", A)

print("rounded to", round(A))