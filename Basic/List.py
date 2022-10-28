# List is a collection which is ordered and changeable. Allows duplicate members.

print("------------------------------------------------------------------------- List create")

# Create List
thisList = ["apple", "banana", "cherry"]
print(thisList)

# Using List constructor to create List
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Get the item with the given position
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Check the length of the List
print(len(thisList))

# Check if str exist in the List
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Get the number of times the value "cherry" appears in the list
fruits = ['apple', 'banana', 'cherry']
print(fruits.count("cherry"))

# Get the index with the given item
fruits = ['apple', 'banana', 'cherry']
print(fruits.index("cherry"))

# Get the max/min element in the list
myList = [1,2,5,4]
print(max(myList))
print(min(myList))

print("--------------------------------------------------------------------------- List Slicing")

# Slice from 2(inclusive) to 5(exclusive)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Slice from beginning to 4(exclusive)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Slice from 2 (inclusive) to end (inclusive)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Slice from back, -4 (inclusive) to -1 (exclusive)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("-------------------------------------------------------------------------- List Modify")

# Change item in List
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change two items in List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change two items in List
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change two items in List
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("------------------------------------------------------------------------- List Adding")

# Insert item at the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert item at the given position
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("-------------------------------------------------------------------------- List Remove")

# Removes given item from the List
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

# Remove item at given position
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item from the List
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("-------------------------------------------------------------------------- List Loop")

# Natural for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# For loop through index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# While loop through index
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("-------------------------------------------------------------------------- List Sort")

# Sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Sort with case-insensitive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse the List    -> will reverse the original list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Reverse the List   -> without reverse the original list (More Common!)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
newList = thislist[::-1]
print(newList)


print("-------------------------------------------------------------------------- List Copy")

# Copy the List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Copy List using constructor
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("-------------------------------------------------------------------------- List Joining")

# Combine two List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Combine two List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Copy by for loop
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

print("-------------------------------------------------------------------------- Special Methods")
# Get all possible combinations for the array
from itertools import permutations
perm = permutations([1,8,3,2])
print(list(perm))