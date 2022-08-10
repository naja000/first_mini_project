print("********    Welcome to Calculator   ********")
num1=input("enter a number1:")
print(num1)
num2=input("enter a number2:")
print(num2)
print("These are the operators you can use: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=='1':
    print("This is an Addition operation")
    print("The sum of the two number is",num1 + num2)
if operator=='2':
    print("This is an Subtraction operation")
    print("The difference of the two number is", num1 - num2)
if operator=='3':
    print("This is an Multiplication operation")
    print("The product of the two number is", num1 * num2)
if operator == '4':
    print("This is an Division operation")
    print("The divident of the two number is", num1 / num2)
if operator=='5':
    print("This is an Modulus operation")
    print("The mod of the two number is", num1 % num2)
sum=num1+num2
print()