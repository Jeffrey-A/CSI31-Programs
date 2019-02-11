import math
def sumN(n):
    #returns the sum of the first n natural numbers.
    ad = 0
    for i in range(n):
        ad = ad + i
    return ad

    
def sumNCubes(n):
    #returns the sum of the cubes of the first natural numbers.
    add = 0
    for i in range(n):
        add = add + i**3
    return add
        
def main():
    print('This program calculates the sum and the cubes sum of naturals numbers.')
    n = int(input("How many numbers you want to evaluate? : "))
    su = sumN(n)
    cubessu = sumNCubes(n)
    print("The sum =",su,"and the the sum of the cubes of the first naturals numbers =",cubessu)
    
main()
    
    
