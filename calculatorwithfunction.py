
print("*****Welcome to Zodiac Calculator*****")
print("Enter the first number:")
num1=int(input())
print("Enter the second number:")
num2=int(input())
print("These opertion you ca use:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
a=input("please choose an option(1,2,3,4,5):")
def add(num1,num2):
    return num1+num2
if a=="1":
        result=add(num1,num2)
        print("This is an Addition")
        print(result)
def sub(num1,num2):
    return num1-num2
if a=="2":
    result=sub(num1,num2)
    print("This is an Subtraction")
    print(result)
def Mul(num1,num2):
    return num1*num2
if a=="3":
    result=Mul(num1,num2)
    print("This is an Multiplication")
    print(result)
def Div(num1,num2):
   return num1/num2
if a=="4":
    result=Div(num1,num2)
    print("This is an Divison")
    print(result)
def  Mod(num1,num2):
   return num1%num2
if a=="5":
    result=Mod(num1,num2)
    print(result)

