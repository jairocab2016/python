# booleans
my_boolean = True
print (my_boolean)
print (2 == 3)
print ("hello" == "hello")
print(1 != 1)
print ("eleven" != "seven")
print (7 > 5)
print(9 >= 9.0)

# if Statements
if 10 > 5:
    print("10 greater than 5")

print("Program ended")

num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")


# else Statements
x = 4
if x == 5:
   print("Yes")
else:
   print("No")


num = 7
if num == 5:
  print("Number is 5")
else:
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else:
      print("Number isn't 5, 11 or 7")

num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")

#Boolean Logic
print (1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print (1 != 1 or 2 == 2)
print (2 < 1 or 3 > 6)
print (not 1 == 1)
print (not 1 > 7)

#Operator Precedence
print (False == (False or True))
print ((False == False) or True)

x = 4
y= 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("Nop")


# while Loops
i = 1
while i <= 5:
   print(i)
   i = i + 1
print("Finished!")

#break
i = 0
while 1==1:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

#continue
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")