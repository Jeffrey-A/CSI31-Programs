def main():
    print("This program find the greatest common divisor of two values.")
    n, m = eval(input("Enter two number separates by comma: "))
    
    while m != 0:
        n, m = m, n%m
    print(n,"is the GCD")
    
main()
    