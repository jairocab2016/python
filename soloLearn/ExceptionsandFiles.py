#Exceptions Handling
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")


try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")


#Finally
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")


#Raising Exceptions

print(1)
#raise ValueError #Levantar excepcion
print(2)

name = "123"
#raise NameError("Invalid name!") #Levantar excepcion

try:
   num = 5 / 0
except:
   print("An error occurred")
   #raise


#Assertions
print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3
print(3)

#Opening Files
#myfile = open("filename.txt")

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

file = open("filename.txt", "w")
# do stuff to the file
file.close()


#Reading Files
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

file = open("filename.txt", "r")
print(file.readlines())
file.close()

file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()


#Writing Files
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()



file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()



msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

#Working with Files
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()


with open("filename.txt") as f:
   print(f.read())