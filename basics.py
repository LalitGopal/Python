"""
b = 5
print(b)

a = input("age?  ")
print("hi", a, "is your age.", b, "hi")

print(type(b))

c = int(input("age ?  "))
print(c)

a, b, c = "apple", "Apple", "APPLE"

print(a, b, c)

A, B, C = input("enter names? ").split(" ")
print(C, A, B)


i = "lalit gopal"
print(i)
print(type(i))
print(i.upper())
print(i.lower())
print(i.capitalize())
print(i.title())
print(i.count("l"))
print(i.replace("l", "k"))

a = "hi hi  hihi bgf hi hjsi giu sgs s  hi"

print(a.count("hi"))

a = "4"
b = "5"
print("the number is", a + ".")  # + string concatination.
print("the number is" + b + ".")



a1, a2, a3 = input("Enter three names & use ' , ' for seperation:- ").split(" , ")
# a1, a2, a3 = input("Enter three names & use ' ,' for seperation:- ").split(" ,")
# a1, a2, a3 = input("Enter three names & use ', ' for seperation:- ").split(", ")
print("name-1 :", a1)
print("name-2 :", a2)
print("name-3 :", a3)




print(' I\'m  not a "bot" ... I\'m a "robot!" ')
print(' the "BOOK" ')

name = " 1. one \n 2. two \n 3. three \n 4. four\n5. five\n6. six\n7. seven"
print(name)

"""


'''
print(
    """
    
    
    
    
    h
    
    
            e 
            
    
    l
    
    
            l
            
    
    o  
      
      """
)
'''


"""

# String Manipulation
v = "stringk"

print(v[0:2])
print(v[2])
print(v[-3])
print(v[::-1])

"""


"""

# print("  line-1           \n  line-2                  \n  line-3        ")  &  print("  line-1\n  line-2\n  line-3") gives the same output.
print("  line-1\n  line-2\n  line-3")
print(" line-1\n line-2\n line-3")
print("line-1\nline-2\nline-3")

"""


score = 10
# this is a multi-line if else statement
if score > 5:
    print("pass")

else:
    print("fail")


scoree = 6
print("pass") if scoree > 5 else print("fail")


# if the score is greater than 5 the 'a' variable will be assigned with the value of 'pass' if not it'll be assigned with 'fail'.

Score = 4

a = "pass" if Score > 5 else "fail"
print(a)

""" Variables """

a = 1  # Variables are case-sensitive
A = 2

# ' 1a = 8 '   A Variable's name can't start with a number.
# ' a-1  = 8 '   A Variable's name cannot contain ' - ' , ' ! ' , ' @ ' , ' $ ' , ' % ' .

b = "banana"  # If a string is assigned to a variable, Quotes are needed. Quotes can be both single and double.  Integers, Booleans don't need them.

a1, b1, c1 = 4, 5, 6  # assigning multiple variables in a single line

# Global variables

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

# Camel Case:-  Each word, except the first, starts with a capital letter: myVariableName = "John Wick"
# Pascal Case:-  Each word starts with a capital letter: MyVariableName = "John Wick"
# Snake Case:-  Each word is separated by an underscore character: my_variable_name = "John Wick"

# assigning the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


"""Print"""

print("hi")

fruit = "goiyaaa"
print(fruit)

print("hi", fruit)
print("hi", fruit, ".")
# By using ' + ' string concatination has been done here. It won't work if the fruit variable had a integer value.
print("hi", fruit + ".")

print(
    """
      
      L
       A
      L
       I
      T  
      """
)

name = "lalit"
age = 5
print(f"hi i'm {name} nice to see u")
print(f"hi i'm{name}nice to see u")
print(f"the age is {age}...")
# using ' , ' inside print statements while adding variables the space between them are autofilled and cannot be reduced .
# but... in f-strings we could control the spaces before and after the variable.


"""If-Else"""

a = False

if a:
    print("true")
else:
    print("false")

# The if statement checks if the given condition or variable is true , when it's not true it passes to to else statement.
# In the above example the a variable has the value 'false' therefore the if part is skipped and the else statement is printed.

n = "nigeria"  # This is not an empty string so this variable n is considered as True
nn = [1, 2, 3]  # This is not an empty list so the list is considered as True
nnn = ""

if nn:
    print("true")
else:
    print("false")


# empty strings "" , sets , lists , tupils , dic's are generally considered as FALSE & numbers are always True except 0
# if they are not empty then they're True.


"""For-Loop"""

list = ["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"]
# for " each of the individual items " in list: - We are giving a name which represents each individual items of the list
# The name which you give that represents each individual items can be customised based on the list and the purpose of thr code. In this case the name can be 'alphabats'.
for a in list:
    # the 'a' represents one element of the list at a time. here 'a' is the customised name which i give, which represents each of the individual items on the list.
    print(a)  # prints each of the list items seperately.
    # print('hi')  -  the list has seven items so, the 'hi' will be printed seven times.

# using for-loops for printing sequense of numbers.
for i in range(10):  # the first number is '0' zero
    print(i)

for i in range(
    10, 21
):  # the 1st parameter 10 is the starting number, and the secound parameter 21 is the ending number.
    print(i)

for i in range(10, 21, 2):  # the 3rd parameter 2 is the iteration eg:- 10,12,14...
    print(i)

for i in range(20, 10, -1):  # printing reverse sequence of numbers.
    print(i)

for i in range(1, 21):  # using if conditions on the selected range of numbers
    if i % 4 != 0:
        print(i)

# Code Explanation:- the numbers between 1 to 20 are selected in the for loop by using the range() function. The selected numbers are printed with a specefied if condition.
# In the previous two examples, a group of numbers are selected with range() and then printed. In the last one the selected group of numbers are printed with a if condition.


"""While-loop"""

# while-loop = execute some code while some condition remain true.
# x = 0 zero is always the first number in pyython. the counter variable in while loop must be 1 if it's 0 it gives an extra one.
x = 1  # counter variable.
while x <= 20:  # while condition.
    print(x, ".", x)
    x += 1  # value incrementor.

food = input("enter a food u like (q to quit)  :  ")
# the loop runs until the user types 'q'
while not food == "q":  # code-explanation:  while the value of food is not q
    print(f"{food} that's niceee.")
    food = input("enter a food u like (q to quit)  :  ")

print("bye")


"""Functions"""

# function-name , function-parameters , function-arguements , return statements in function


def function(names):
    for name in names:
        print(name)


function(["abc", "def", "ghi", "jkl", "mno"])


args = ["lalit", 19, "a", "male"]
kwargs = {"name": "lalit", "gender": "male", "section": "a", "age": 19}


def fun222(name, age, section, gender):
    print(name, age, gender, section)


# return statement is used to get information or a value back from a function
fun222(*args)
fun222(**kwargs)


"""""" """""" """""" """""" """""" """""" """""" """""" """""" ""


def func1(**dic):
    print(dic)


func1(a="agd", b="kgfk", c="hmkgn")


def func2(*list):
    print(list)


func2("a", "b", "c", 4, 5, 6, "sdf")


def func3(name, age, number, time):
    print(name, age, number, time)


# func3(*["lalit", 5, 565, "abcdefg"])  = shortform of the next two lines of code.
lst = ["lalit", 5, 565, "abcdefg"]
func3(*lst)


def func4(name, age, number, time):
    print(name, age, number, time)


# shortcut func4(**{"age": 5, "time": 50.00, "number": 55655755855, "name": "lalit"})
# dictionary = {"age": 5, "time": 50.00, "number": 55655755855, "name": "lalit"}
# func4(**dictionary)
func4(**{"age": 5, "time": 50.00, "number": 55655755855, "name": "lalit"})


"""List"""

list1 = [
    "a",
    "b",
    "c",
    "d",
    "a",
    "a",
    1,
    2,
    3,
    4,
    5,
    1,
    1,
    1,
    True,
    True,
    False,
    True,
    ["A", "B", "C"],
]
print(list1)  # printing the list.
print(
    list1[5], list1[6]
)  # printing two individual items from the list using their index number.
print(list1[-6])  # printing an item from the list by using the reverse index number.
print(list1[0:8])  # croping the list using index numbers
print(list1[2:])  # single croping - from the start
print(list1[:2], list1[:3])  # single froping - from the end
print(list1[18][0])  # accessing a list which is inside the main list.

list2 = list1.copy()  # copies the whole list
print(list2)

list2.clear()  # clears the whole list, now its an empty list.
print(list2)

print(list1.count("a"))  # counts how many a's are there in the list.
print(list1.index(5))  # returns the index number of '5' which is 10
print(len(list1))  # returns the length of the list.
# print(max(list1)) min & max works on the list which only has integers.
# print(min(list1))

lst2 = [True, False, True, False, True, False, True, False]
print(lst2)
lst2.pop(1)  # deleting the index value 1 which is False
print(lst2)

list1.extend(lst2)  # merging the two lists
print(list1)

list1[0] = "A"  # modifying the list using index number.
print(list1)

list1.remove("c")  # removing 'c' from the list.
print(list1)

list1.append(
    True
)  # appending / adding True to the list, the newely added item will be the last item of the list.
print(list1)

list1.insert(2, "c")  # adding c to the list by specifying the index number which is 2.
print(list1)

list1.reverse()  # reverses the whole list.
print(list1)

# list1.sort()
# print(list1)  not supported between instances of 'list' and 'bool'


"""String-Methods"""  # https://youtu.be/bnSYeYFRCaA

# 1. casefold() - casefold returns a version of the string for caseless comparisons.

NAME1 = "IROnMan"
name2 = "iroNmAN"

print(name2, NAME1)
print(name2 == NAME1)
print(NAME1.casefold(), name2.casefold())
print(name2.casefold() == NAME1.casefold())
print(name2, NAME1)


# 2. center() - specefies how many characters you want this string to occupy, and places the text in the center.

Fruit = "Banana"

print(Fruit)
print(Fruit.center(10))
# the string takes 20 characters and the text is placed in the middle
print(Fruit.center(20))
print(Fruit.center(10, "/"))
print(Fruit.center(30, "/"))
# this string takes 30 characters and the text is placed  in the middle the rest of the spaces are fillrd with ' / '
print(Fruit.center(30, "."))
# this string takes 30 characters and the text is placed  in the middle the rest of the spaces are fillrd with ' . '
print(Fruit.center(30, "."))


# 3. join() - joins all the strings together with the specefied character.

lst3 = ["abcdefg", "hjgnbbk"]  # works only with strings
print(lst3)
print("-".join(lst3))

lst4 = ".".join(lst3)
print(lst4)


# 4. zfill()

var = "text"

print(var)
print(var.zfill(10))


# 5. format()

line1 = "The{subject} is {action}."  # could be used in complete the sentense game.

print(line1.format(subject="cat", action="dancing"))


line2 = "the {} is on the {}."

print(line2.format("car", "road"))


"""Tuple"""

ABC = "\x41\x42"
abc = "\x4C\x41\x4C\x49\x54"

print(ABC)
print(abc)

"""set"""
# set never follows a sequence. it will not follow the sequence in which you've added the elements .
# indexing is not supported in set . because it doesn't have proper sequence.
# setalso does not support duplicate values.
# set uses a conceptt of 'hash' to inprove the performance
set = {1, 1, 2, 5, 8, 6, 9}
print(set)

"""Operators"""

# Unary Operator

val = 5
print(val)

val = -val
print(val)


""" _ """

_ = "a"
print(_)

# number_formatting
num = 10_00_00_00_000
print(num)

# reserved names
_True = True
if_ = 45
_else = "hlkij"
class_ = 5665
