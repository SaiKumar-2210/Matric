def rec_fac(n):
    if n!=0:
        return n*rec_fac(n-1)
    else:
        return 1

def itr_fac(n):
    fac=1
    while n!=0:
        fac*=n
        n-=1
    return fac
def occ_str(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

print('===========Task 2==========')
while True:
    print("1. Factorial program")
    print('2. No of occurances in String')
    print('3. Check for palindrome')
    print('0. Exit')
    choice=input("Enter your choice: ")
    match choice:
        case '1':                               #Factorial of number
            print("1.recursive    2. iteration")
            c=input("Enter: ")
            n=int(input('Enter a number: '))
            if c=='1':              #recursive
                print(rec_fac(n),'is factorial of',n,'\n\n\n')
            elif c=='2':
                print(itr_fac(n),'is factorial of',n,'\n\n\n')
            else:                   #iterative
                print("Invalid choice\n\n\n")
        case '2':                               #Occurances of String using Dictionary
            s=input('Enter a string: ')
            ocr=occ_str(s)
            for i in ocr:
                print(i,' : ',ocr[i])
            print('\n')
        case '3':                                   #Palindrome Code
            s=input('Enter a string: ')
            if s==s[::-1]:
                print(s, 'is a palindrome\n\n\n')
            else:
                print(s,"is not a palindrome\n\n\n")
        case '0':
            exit(0)