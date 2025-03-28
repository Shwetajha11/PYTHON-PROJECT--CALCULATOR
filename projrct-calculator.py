#python program to create a calculator.
#3 steps to build simple calculator
'''
1.function for operations
2.user input
3.priint result
'''
##step-1
#funtion to add two numbers
def add(number1,number2):
    return number1+number2
#function to substract two numbers
def sub(number1,number2):
    return number1-number2
#function to muliplication of two numbers
def multiply(number1,number2):
    return number1*number2
#function to division of two numbers
def division(number1,number2):
    return number1/number2
#function to average of two numbers
def avg(number1,number2):
    return (number1+number2)/2

##step-2
print("please select an opration:\n""1.addition\n""2.substraction\n""3.multiplication\n""4.division\n""5.average\n")

select=int(input("select a operation from 1,2,3,4,5"))

number1= int(input("enter first number"))
number2= int(input("enter second number"))

## step-3
if select==1:
   print("sum of two numbers is",add(number1,number2))
elif select==2:
   print("substraction of two numbers is",sub(number1,number2))
elif select==3:
   print("multiplication of two numbers is",multiply(number1,number2))
elif select==4:
   print("division of two numbers is",division(number1,number2))
elif select==5:
   print("average of two numbers is",avg(number1,number2))
else:
   print("inavlid opration! please select again")
