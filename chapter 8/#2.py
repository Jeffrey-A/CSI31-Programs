def main():
    print("This program calculates the windchill index.")
    t = eval(input("Enter the temperature in Fahrenheit: "))
    v = eval(input("Enter the wind speed in miles per hour: "))
    
    result = 35.74 + 0.6215*t - 35.75*(v**0.16)+ 0.4275*t*(v**0.16)
   
    wind = 35.74 + 0.6215*t - 35.75*(v**0.16)+ 0.4275*t*(v**0.16)
    temp = - 35.75*(v**0.16)+ 0.4275*t*(v**0.16)
    print(round(wind),round(temp))
             
main()