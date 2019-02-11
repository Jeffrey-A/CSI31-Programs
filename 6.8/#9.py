def grade(score):
    
    grades = ['A','B','C','D','F']
    
    if score <= 100 and score>= 90:
        a = print("Your grade is:",grades[0])
        return a
    elif  score <= 89 and score>= 80:
        b = print("Your grade is:",grades[1])
        return b
    elif score <= 79 and score>= 70:
        c = print("Your grade is:",grades[2])
        return c
    elif score <=69 and score >= 60:
        d = print("Your grade is:",grades[3])
        return d
    elif score < 60:
        f = print("Your grade is:",grades[4])
        return f
    else:
        error = print("Sorry score out of range!")
        return error
        
def main():
    sc = int(input("Enter your score from 0-100: "))
    gr = grade(sc)
    print(gr)
main()