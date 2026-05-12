num1= int(input("Enter first number :- "))
operator= input("Enter operator :- ")
num2= int(input("Enter second number :- "))
if operator == "+" :
  print("Result: ",num1+num2)
elif operator == "-" :
  print("Result: ",num1-num2)
elif operator == "*" :
  print("Result: ",num1*num2)
elif operator == "/" :
  print("Result: ",num1/num2)
elif operator == "**" :
  print("Result: ",num1**num2)
elif operator == "%" :
  print("Result: ",num1%num2)
else :
  print("Invalid operator!")



