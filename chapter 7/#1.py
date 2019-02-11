def main():
    print("This program calculates the total wages for the week.")
    hours = eval(input("How many hours do you worked this week?" ))
    rate = eval(input("Enter hourly rate: "))
    if hours > 40:
        overtime = rate + rate/2
        pay = hours * rate + (hours - 40) * overtime 
    else:
        pay = hours * rate
        
    print("You worked {0} hours with an hourly rate of {1}$,so you get a total of {2:0.2f}$.".format(hours,rate,pay))
    
main()
    
    