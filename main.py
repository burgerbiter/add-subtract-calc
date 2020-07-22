
def addNumbers(num1, num2):
  print(num1+num2)
def subNumbers(num1, num2):
  print(num1-num2)
num1=int(input("enter a number"))
num2=int(input("enter another number"))
operator=input("add or subtract")
if operator.lower() == "add":
  addNumbers(num1,num2)
elif operator.lower() == "subtract":
  subNumbers(num1, num2)
else:
  print("i said add or subtract")
