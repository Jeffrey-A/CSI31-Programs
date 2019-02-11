def main():
    print("This program make acronyms.\n")
    user = input("Enter a phrase that you want to make an acronym: ").upper()
    u = user.split()
    for i in u:
        print(i[0], end ="") 

    
    
main()