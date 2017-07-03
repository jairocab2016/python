#List
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

str = "Hello world!"
print(str[6])


#List Operations
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#List Functions
nums = [1, 2, 3]
nums.append(4)
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z'))


#Range
numbers = list(range(10))
print(numbers)

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

numbers = list(range(5, 20, 2))
print(numbers)


#Loops
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1

#For Loop
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

for i in range(5):
  print("hello!")
