def main():
    print("This program calculates the average word lenght in a sentence.")
    user = input("Type whatever you want: ")
    x = user.count(" ")#counts the spaces
    s = len(user) - x #s = de numbers of caracter without spaces
    u = user.split()#separate the words by spaces
    n = len(u)# number of words
    print("The average word length is:",s/n)
    
main()