def my_list():
    this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    return this_list


def another_list():
    this_list = ["avocado", "peach", "grapes"]
    return this_list


def a_tuple():
    this_tuple = ("kiwi", "orange")
    return this_tuple


new_list = []

number_list = [100, 50, 65, 82, 23]

another_list = another_list()
my_list = my_list()
a_tuple = a_tuple()

print(my_list)
print(len(my_list))
print(type(my_list))

#  Accessing list items
print(my_list[-1])  # printing the last item in a list
print(my_list[2:5])  # prints the 3rd, 4th and fifth items starting from index 2 to index 4, not including 5
print(my_list[:4])  # prints from index 0 to 3, excluding 4
print(my_list[2:])  # prints from index 2 to the end
print(my_list[-4:-1])  # prints from -4 to -2 excluding -1 which is last item in the list

#  Changing list items
my_list[1] = "blackcurrant"
print(my_list)

my_list[1:3] = ["blackcurrant", "watermelon"]
print(my_list)

my_list[1:2] = ["blackcurrant", "paw paw"]
print(my_list)

my_list[1:3] = ["strawberry"]
print(my_list)

#  Insert into a list
my_list.insert(2, "pineapple")  # adds an item to the specified index
print(my_list)

#  Append to a list
my_list.append("paw paw")  # adds an item to the end of a list
print(my_list)

#  Extending a list, ie adding a list to another list
my_list.extend(another_list)
print(my_list)

#  Another iterable to a list, ie adding tuples, sets or dictionary to a list
my_list.extend(a_tuple)  # appending a tuple to a list
print(my_list)

#  Remove from a list
my_list.remove("apple")  # remove by specifying the name of the item
print(my_list)

my_list.pop(3)  # remove by specifying the index of the item
print(my_list)

my_list.pop()  # removes the last item of the list
print(my_list)

my_list.pop(-1)  # also removes the last item of the list
print(my_list)

del my_list[3]  # del also removes according to the specified index
print(my_list)

# Looping through a list
for x in my_list:
    print(x)

print()

for i in range(len(my_list)):  # looping through index and len
    print(my_list[i])

print()

[print(x) for x in my_list]  # Using list comprehension

#  List comprehension
for x in my_list:
    if "o" in x:
        new_list.append(x)

print(new_list)

print()

new_list = [x for x in new_list if "a" in x]
print(new_list)

print()

new_list = [x for x in new_list if x != "apple"]
print(new_list)

#  Sorting a list
my_list.sort()
print(my_list)

print()

new_list.sort(reverse=True)
print(new_list)

print()

number_list.sort(reverse=True)
print(number_list)

new_list.reverse()
print(new_list)

#  Copying a list
mylist = my_list.copy()
print(mylist)

another_list = list(number_list)
print(another_list)

# Joining lists
list3 = another_list + new_list
print(list3)

for x in mylist:
    number_list.append(x)

print(number_list)

new_list.extend(another_list)
print(new_list)
