from art import logo


def add(number1,number2):
  return number1 + number2
  
def sub(number1,number2):
  return number1 - number2
  
def mul(number1,number2):
  return number1 * number2
   
def div(number1,number2):
  return number1 / number2


operation = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}


def calculator():
  print (logo)
  x = float(input("What is the first number?:"))
  for i in operation:
    print(i)
  final_status = False  

  while not final_status:
    operation_Symbol = input ("Pick an operation?:")
    y = float(input("What is the second number?:"))
    calc_function = operation[operation_Symbol]
    answer = calc_function(x,y)
    print (x,"",operation_Symbol,"",y,"","=","",answer)
    final_status = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new Calculation: ")
    if final_status == 'n':
      final_status = True
      calculator()
    else:
      final_status = False
      x = answer

calculator();
  


