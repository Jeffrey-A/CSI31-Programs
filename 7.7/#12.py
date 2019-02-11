def main():
    print("This program is a year evaluator.")
    month,day,year = input("Enter a year in this format month/day/year: ").split("/")
    if int(month) <= 12:
        if int(day) <= 31:
            print("The year {0}/{1}/{2} is valid.".format(month,day,year))
        else:
            print("The year entered have an invalid format.")
    else:
        print("The year entered have an invalid format.")
    
main()
        
            