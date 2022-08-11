replace=""
flag=False     #flag is used to avoid print
print("******      WELCOME TO CALCULATOR     ******")
num1=int(input("Enter the  number1 :"))
print(num1)
num2=int(input("Enter the number2 :"))
print(num2)
print("operator you can use:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
result=0
operator=input("choose an option from these (1,2,3,4,5):")
if operator=="1":
    replace1="Addition"
    result=num1+num2
if operator=="2":
    if num1<num2:
        flag=False
        print("cannot subtract the First number is less than the Second number")
    else:
        flag=True
        replace1="Subtraction"
        result=num1-num2
if operator=="3":
    replace1="Multiplication"
    result=num1*num2
if operator=="4":
    replace1="Division"
    result=num1//num2
if operator=="5":
    replace1="Modulus"
    result=num1%num2
if flag==True:
   print("The result of",replace1,"of",num1,"and",num2,"is",result)