def main():
    
    print("THis program illustrates a chaotic function.")
    x, y = eval(input("Enter two initial values between 0 and 1 separates by comma: "))
    z = eval(input("Enter the number of interactions: "))
    print()
    print("{0}   {1}          {2}".format("Index",x,y)) 
    print("------------------------------")
    for i in range(z):
        x = 3.9 * x* (1 - x)
        L = i + 1
       

        y = 3.9 *y* (1-y)
        print("{0}       {1:0.6f}      {2:0.6f}".format(L,x,y))
        
main()
    
 
   