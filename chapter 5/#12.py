def main():
    print("This program calculates the future value\n of years of investment.")
    principal = eval(input("Enter the amount of investment: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Years of investment: "))
    print()
    print("Year      Value")#6 spaces
    print("------------------")
    for i in range(years):
        principal = principal * (1 + apr)
        
        print("{0}           {1:4.2f}".format(i,principal))
        
   
    
main()
    