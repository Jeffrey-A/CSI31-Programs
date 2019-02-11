def main():
    grades = ['F','F','D','C','B','A']
    user = int(input("Enter your score from 0-5: "))
    if user<=5:
        yourg = grades[user]
        print("Your grade is: {0}".format(yourg))
    else:
        print("Sorry, score out of range")
    
    
main()
               