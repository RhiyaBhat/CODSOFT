#addition function
def add(n1, n2):
    return n1+n2

#subtration function
def subtract(n1,n2):
    return n1-n2

#multiplication function
def multiply(n1,n2):
    return n1*n2

#division function
def divide(n1,n2):
    return n1/n2

while True:
    #User makes a choice on the operation to be performed
    print("Select:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print('0.Exit')

    choice=input("Enter your choice (1/2/3/4):")

    #End loop if user wants to exit
    if choice == '0':
        break

    n1 = float(input('Enter your first number:'))
    n2 = float(input('Enter your second number:'))

    if choice == '1':
        print('Sum:',n1,'+',n2,'=',add(n1,n2))
    elif choice == '2':
        print('Difference:', n1, '-', n2,'=', subtract(n1,n2))
    elif choice == '3':
        print('Product:', n1, '*', n2, '=', multiply(n1, n2))
    elif choice == '4':
        print('Quotient:', n1, '/', n2, '=', divide(n1, n2))
    else:
        print("Invalid input")





