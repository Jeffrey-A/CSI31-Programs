def main():
    sc = int(input("Enter your score from 0-100: "))
    grades = ['A','B','C','D','F']
    
    if sc <= 100 and sc>= 90:
        print("Your grade is:",grades[0])
    elif  sc <= 89 and sc>= 80:
        print("Your grade is:",grades[1])
    elif sc <= 79 and sc>= 70:
        print("Your grade is:",grades[2])
    elif sc <=69 and sc >= 60:
        print("Your grade is:",grades[3])
    elif sc < 60:
        print("Your grade is:",grades[4])
    else:
        print("Sorry score out of range!")
        
main()