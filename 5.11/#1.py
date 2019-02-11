#date convert2.py
#converts day month and year numbers into two dates formats
def main():
    day = int(input("Enter day, number: "))
    month = int(input("Enter month number: "))
    year = int(input("Enter year number: "))
   
    
    date1 = str(month) +"/" +  str(day) +"/"+ str(year)
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]
    monthStr = months[month-1]
    
    date2 = monthStr+" "+ str(day)+","+str(year)
    
    print("The date is {0} or {1}.".format(date1, date2))
    
main()