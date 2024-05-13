print("------------------------------")
print("Welcome to My Calculator")
print("------------------------------")

value1 = input("Enter the Value1: ")
value2 = input("Enter the Value2: ")

a = int(value1)
b = int(value2)

print(" Please Enter the operation you want to do on the number like + , - , * or /")
operator = input("Enter the operator: ")

if operator == "+":
 output = a + b
 print("------------------------------")
 print("The output of the values is: " , output )
 print("------------------------------")
elif operator == "-":
 output = a - b
 print("------------------------------")
 print("The output of the values is: " , output )
 print("------------------------------")

elif operator == "*":
 output = a * b
 print("------------------------------")
 print("The output of the values is: " , output )
 print("------------------------------")

elif operator == "/":
 output = a / b
 print("------------------------------")
 print("The output of the values is: " , output )
 print("------------------------------")
