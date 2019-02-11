import math

def cost(whpizz,diame):
    radious = diame / 2
    a = math.pi * radious**2
    
    cost = whpizz / a
    return cost
def main():
    print("This program calculates the cost per inch of a pizza.")
    cos = eval(input("Enter the cost of the whole pizza: "))
    diameter = eval(input("Enter the diameter of the pizza: "))

    result = cost(cos,diameter)
    print("The cost per inch is:{0:0.2f}".format(result))
    
main()
    
    
    
    