def squareEach(nums):
    sq = 0
    for i in range(nums):
        sq = eval(input("Enter a number: "))
        sqrt = sq**2
        print("The square of",sq,"is",sqrt)
    return sqrt
      
def main():
    print("This program sum numbers.")
    n = eval(input("How many numbers you want to square? "))
    square = squareEach(n)
  
        
main()
