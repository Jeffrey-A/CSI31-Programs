def main():
    print("This program calculates how much you will take two double an investment.")
    inv = eval(input("Enter the initial capital: "))
    rate = eval(input("Enter the anualized rate: "))
    year = 0
    gain = inv *(1+rate)
    
    while gain < (2*inv):
        year = year + 1
        gain = inv *(year+rate)
    print("It will take",year,"years to get",round(gain))
        
main()  