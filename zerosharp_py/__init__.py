def math(num1, num2, action): 
  if action == "add":
    return num1 + num2
  if action == "subtract":
    return num1 + num2
  if action == "multiply":
    return num1 + num2
  if action == "divide":
    return num1 + num2

def terminal(text):
  print(text)

terminal(math(5, 2, "divide"))
