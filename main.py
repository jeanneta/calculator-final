from art import logo
# add
def add(a,b):
  return a+b

# subtract
def subtract(a,b):
  return a-b

# divide
def divide(a,b):
  return a/b

# add
def multiply(a,b):
  return a*b

# a=10
# b=5
dictionary={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def recursion():

  print(logo)

  num_one=float(input("first num: "))

  finish_game=False
  while not finish_game:
    operation=input("operation? ")
    num_two=float(input("second num: "))
    calc_function=dictionary[operation]
    answ=calc_function(num_one, num_two)
    print(f"{num_one} {operation} {num_two} = {answ}")
    question=input("'y' to play again and 'n' to starn new : ")
    if question=='y':
      num_one=answ   
    else:
      finish_game=True
      recursion()
recursion()