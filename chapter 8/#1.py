def main():
    print("This program calculates the Fibonacci number.")
    user = int(input("Enter a number to find the Fibonacci number: "))
    x = 1
    y = 1
    xy = user - 2
    
    for i in range(xy):
        x,y = y, x + y
    print(y)
        
main()
        
               