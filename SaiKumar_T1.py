while(True):
    print("1. +ve or -ve or zero")
    print("2. fibonaci series")
    print("3. Armstrong number")
    print("0. Exit")
    c=input("choice:")
    match c:
        case "2":
            print("------fibonaci series program----------")
            a=0
            b=1
            temp=0
            n=int(input("enter n: "))
            print("First",n,"terms in fibonacci series are: ")
            for i in range(n):
                print(a,end=" ")
                temp=a
                a=b
                b=temp+b
            print()

        case "1":
            print("------Check number is +ve or -ve or zero program----------")
            n=int(input('enter a number: '))
            if n>0:
                print(n,'is positive')
            elif n==0:
                print(n,'is zero')
            else:
                print(n,'is negative')
        case "3":
            print("------Armstrong number program----------")
            n=input('enter a three digit number: ')
            ar=0
            if len(n)==3:
                for i in n:
                    ar+=int(i)**3
                if ar==int(n):
                    print(n,'is armstrong number')
                else:
                    print(n,"is not a armstrong number")
            else:
                print("enter a three digit number")
        case '0':
            exit(0)