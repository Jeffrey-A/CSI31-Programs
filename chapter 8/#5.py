def main():
    print("THis program will continues running until you enter a number not prime.")
    n = eval(input("Enter a number: "))
    while n > 2 and n % 2 != 0:
        n = eval(input("Enter a number: "))
        
    
    print("Out! you enter {} a no prime number.".format(n))
    
main()