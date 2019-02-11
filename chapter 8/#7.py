def main():
    print("This program finds the addition of two prime number \n that is equals to an even number that you enter.")
    user = eval(input("Enter an even number: "))
    if user%2 == 0:
        f = user//2
        print(f,"+",f,"=",user)
        
    else:
        print("Sorry you did not enter an even number.")
        
main()
                