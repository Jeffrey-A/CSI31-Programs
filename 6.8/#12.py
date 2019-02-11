def sumList(nums):
    add = 0
    for i in range(nums):
        s = eval(input("Enter a number: "))
        add = add + s 
    return add
      
def main():
    print("This program sum numbers.")
    print()
    n = eval(input("How many numbers you want to add? "))
    add = sumList(n)
    print("The sum equals:{0}".format(add))
        
main()
        