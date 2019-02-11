def grades():
    grades = ['F','F','D','C','B','A']
    stu = eval(input("Enter your score from 0-5: "))
    
    if stu == 5:
        grad = grades[5]
        print("Your grade is:",grad)
    elif stu == 4:
        grad = grades[4]
        print("Your grade is:",grad)
        
    elif stu == 3:
        grad = grades[3]
        print("Your grade is:",grad)  
        
    elif stu == 2:
        grad = grades[2]
        print("Your grade is:",grad)
        
    elif stu == 1 or stu == 0:
        grad = grades[0]
        print("Your grade is:",grad)      
        
    else:
        print("Sorry score out of range")
        
grades()