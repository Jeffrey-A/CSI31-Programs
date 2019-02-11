def main():
    print("This program calculates if a year is leap.")
    year = eval(input("Enter a year in your digits: "))
    
    if year % 400 == 0:
        print("The year {0} is a year leap.".format(year))
    else: 
        print("The year {0} is not a year leap.".format(year))
        
main()
    