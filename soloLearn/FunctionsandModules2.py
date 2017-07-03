#Comments
x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment


#Docstring
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")


#Functions as Objects
def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))


def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10



#Modules

print(do_twice(add, a, b))