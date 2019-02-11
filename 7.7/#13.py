def leapyear(year):
    
    if int(year) % 400 == 0:
        e = "yes"
    else: 
        e = "no"
    return e

def validyear(month,day,year):
    if int(month) <= 12:
        if int(day) <= 31:
            eva = "yes"
        else:
            eva = "no"
    else:
        eva = "no"
    return eva
            
        
def main():
    month,day,year = input("Enter a year in this format month/day/year: ").split("/")
    valid = validyear(month,day,year)
    leap = leapyear(year)
    
    if valid == "yes":
        daynum = 31 * (int(month) - 1) + int(day)
    elif int(month) > 2:
        daynum = (4*(month) + 23) // 10
    elif leap == "yes" and int(month) > 2:
        daynum = ((4*(month) + 23) // 10) + 1
    print("Day number {0} of the year {1}.".format(daynum,year))
    
main()
    
    
     
    