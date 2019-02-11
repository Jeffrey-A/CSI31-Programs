import math
def main():
    print("This program calculates your BMI.")
    weight = eval(input("Enter your weight in pounds: "))
    height = eval(input("Enter your height in inches: "))
    
    bmi = (weight * 720) / height**2
    
    if bmi >= 19 and bmi <= 25:
        print("Your BMI is {0:0.2f}, within the healthy.".format(bmi))
    elif bmi > 25:
        print("Your BMI is {0:0.2f},above the healthy range.".format(bmi))
    else:
        print("Your IBM is {0:0.2f}, below the healthy range.".format(bmi))
        
main()