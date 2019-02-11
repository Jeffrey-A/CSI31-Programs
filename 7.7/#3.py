def main():
    grades = ['F','F','D','C','B','A']
    stu = eval(input("Enter your score from 0-100: "))
    
    if stu <= 100 and stu >= 90:
        grad = grades[5]
        print("Your grade is:",grad)
    elif stu <= 89 and stu >= 80:
        grad = grades[4]
        print("Your grade is:",grad)
        
    elif stu <= 79 and stu >= 70:
        grad = grades[3]
        print("Your grade is:",grad)  
        
    elif stu <= 69 and stu >= 60:
        grad = grades[2]
        print("Your grade is:",grad)
        
    elif stu < 60:
        grad = grades[0]
        print("Your grade is:",grad)      
        
    else:
        print("Sorry score out of range")
        
main()