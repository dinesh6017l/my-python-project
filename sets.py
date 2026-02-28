my_sets = {"a", "b", "c", "d"}
print(my_sets)
print(type(my_sets))

my_lists = [1, 2, 3, 4]
my_sets = set(my_lists)
print(my_sets)
my_sets = {"a", "b", "c", "d"}
print("a" in my_sets)
for item in my_sets:
    print(item)
my_sets.add('e')
print(my_sets)
my_sets.update("f", "g", "h")
print(my_sets)
my_set = {"a", "b", "c", "c"}
my_set.remove("a")
print(my_set)

my_set.pop()
print(my_set)

my_test = {"Elephant", "ball", "cat", "dog"}
my_test.pop()
print(my_test)


first_set = {'one', 'two', 'three'}
second_set = {'orange', 'banana', 'peach', 'one'}
print(first_set.union(second_set))
print(first_set)

intersection = first_set.intersection(second_set)
print("Intersection: ", intersection)

first_difference = first_set.difference(second_set)
print("first difference is ", first_difference)

second_difference = second_set.difference(first_set)
print("second difference is ", second_difference)


print(bool('1'))
print(bool('0'))
print(bool(''))


x = None
y = None

print(id(x))
print(id(y))

mystr = 'abcdefg'
for items in mystr:
    print(items)

users = {'mdriscoll': 'password', 'guido': 'python',
         'steve': 'guac', 'ethanf': 'enum'}
for user in users:
    print(user)


users = {'mdriscoll': 'password', 'guido': 'python', 'steve': 'guac',
         'ethanf': 'enum'}
for user, password in users.items():
    print(f"{user}'s password is {password}")


list_of_tuples = [(1, 'banana'), (2, 'apple'), (3, 'pear')]
for number, fruits in list_of_tuples:
    print(f"{number} - {fruits}")


# using enumerate with loops

mystr = "abcdefgh"
for pos, letter in enumerate(mystr):
    print(f"{pos} - {letter}")


count = 0
while count < 10:
    count += 1
    if count == 4:
        print("Breaking out of loops at 4")
        break
    print(count)


list_of_fruits = [(1, 'banana'), (2, 'apple'), (3, 'pears')]
for number, fruit in list_of_fruits:
    if fruit == 'apple':
        print("apple found!!")
        break
    print(f"{number} - {fruit}")

# using continue statement
for number in range(3, 12):
    if number % 2 == 0:
        continue
    print(number)


list = [1, 2, 3, 4]
for number in list:
    if number == 4:
        print("Found number 4!")
        break
    print(number)
else:
    print("Number 4 not Found")

nested = [['mike', 12], ['jan, 15'], ['alice', 8]]
for lst in nested:
    print(f"List = {lst}")
    for item in lst:
        print(f"Item - {item}")
