def main():
    print("This program calculates speeding tickets in Podunksville.")
    print()
    splimit = 90
    speed = eval(input("Enter clocked speed: "))
    
    if speed <= splimit:
        print("Your speed was legal, do not worried about it.")
    else:
        a = 50
        s = speed - 90
        ticket = (s*5) + a +200
        print("Your speed {0} mph was ilegal, you got a ticket of {1}$".format(speed,ticket))
        
main()