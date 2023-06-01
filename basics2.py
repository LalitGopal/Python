print("i am back")
"""
name = input("enter your name:- ")
print("hii", name)


a1, a2, a3 = input("Enter three names & use ',' for seperation ").split(",")
print("name-1 :", a1)
print("name-2 :", a2)
print("name-3 :", a3)

# single line comment



# String and String function
i = "lalit gopal"
print(i)
print(type(i))
print(i.upper())
print(i.lower())
print(i.capitalize())
print(i.title())
print(i.count("l"))
print(i.replace("l", "k"))


print(' I\'m  not a "bot" ... I\'m a "robot!" ')


# semicolon ; is used to combine two lines of code into a single line

a = "apple" ; print(a)

print("helo")


age = 10
age += 8
print(age)

age = 10
age -= 8
print(age)

age = 10
age *= 8
print(age)

name = "one\ntwo"
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

# BOOLEANS

# empty strings "" , sets , lists , tupils , dic's are generally considered as FALSE & numbers are always True except 0

"""

a = ""  #  {}, [], (), ""

if a:
    print("true")
else:
    print("false")

a = True  # False , 0
if a:
    print("true")
else:
    print("false")




one = True
two = False
three = False
four = True
Five = True

check = all([one, two, three, four, Five])
print(check)

check = any([one, two, three, four, Five])
print(check)

"""
# ENUM  used to create constance in python


"""

from enum import Enum


class state(Enum):
    a = 40
    b = 47
    c = 45
    d = 46
    e = 41


print(state.a.value)
print(state.b.value)
print(state.e.value)
print(state(45))

# list

dogs = ["pug", "huskey", "lab", "c###"]

a = "beau" in dogs
print(a)

print("huskey" in dogs)
print("pug" in dogs)

# difference between append & insert

dogs.insert(2, "boo")
print(dogs)

dogs.append("bau")
print(dogs)

fruits = ["APPLE", "mango", "orange", "GOIYA", "blueberrys", "blackberries"]
print(fruits)

fruits.sort()
print(fruits)

# lists [] can be modified but tupils () cannot be modified

dog = {"name": "booch", "age": 2, "color": "white", "alive": True}

a = dog.get("color")
b = dog.get("hair", "same")
print(a)
print(b)


"""


"""

# functions
# functions can also be nested within a function 
# a function which is written inside a main function can only be accessed inside the main function and cannot be accessed outside the function  
# if we declare a variable in the global scope before the function we can access the variables within the function. If we declare a variable inside a function with the global keyword we can access the variable even outside after the function   

# difference between parameters and arguements in a function in python
# parameters are the values accepted by the function inside the function difinition ... func(name , age):
# Arguements are the values which we pass to the function when we call it ,which will be assigned to the parameters in the function
# Arguements can have a default value which we can mention with the parameter in the function


def func(name="a", age=7):
    print(name, age)


func("boo", 3)

# the name and age are the parameters here and "boo" and 3 are the arguements and 'a' and 7 are the default arguement values
# ! if you pass an object which is mutable inside a function as a parameter and change its values of the object inside the function , the changes(modified value) will be reflected outside the function
# integers , booleans , strings , floats and tupels are immutable , so if you pass them as parameters and you modify their value inside the function ... the new value(modified value) will not be reflected outside the function
# dictionary , list is mutabl !


def change(value):
    value["name"] = "booch"


val = {"name": "boo"}
change(val)

print(val)


def change(value):
    value[0] = "booch"


val = ["apple", "mango", "orange"]
change(val)

print(val)


# return statement in function
# a function can return a value(or anything which happens inside the function) using the return statement
# the function ends as soon as it meets the return ststement , even it has code after it


def func2(name):
    print("hello there", name)
    return name
    print("hi")


func2("name")

"""

"""

# it is a common way to end a function if the starting condition is not satisfied



def func3(name):
    if name != "lalit":
        return
    print("hello there !", name)


func3("abc")

# return statement can also return multiple values , which could also be merged with a sentense


def func4(name, age):
    return "your name is", name, "and age is", age


print(func4("lalit", 19))

# the above function returns multiple values:- name and age merging it with a sentense

# if a main function has a nested function inside it the nested functions can use the variables of the main function using the keyword 'nonlocal'
# in this function ... the main function count has the variable 'count' and the nested function add uses the 'count' variable from the main function using the nonlocal keyword


def count():
    count = 5

    def add():
        nonlocal count
        count = count + 5
        print(count)

    add()


count()


def count():
    count = 5

    def add():
        nonlocal count
        count = count + 5
        print(count)
        count1 = 44

    add()

    def sub():
        nonlocal count
        count = count - 2
        print(count)

    sub()


count()

"""

"""
# Loops
# while loops
# a while loops runs until the given condition becomes False

counter = 1
while counter <= 10:
    print("hellow")
    counter += 1

# in this loop 'counter <= 10' is the condition ... the loop repeates for 10 times and after that the value of counter becomes '11' soo the given loop condition becomes false and the loop breakes

# python knows a number of compound data types which is used to group-together other values
# they are :- *lists *sets *tuples *dictionary

# tuples

t = 123, 345, "hii", "abc"

# the 't' above is considered as a tuple ... it dosent really need that () curly braces to mention it as a tuple ... you dont need parentheses to pack the tuple
# if you have a list inside a tuple then the list can be modified
# list is a mutable object ... and a tuple can contain a list as one of its items and that list can be modified
tple = ("abcd", [1, 2, 3], [4, 5, 6], 456, "string")
tple[1][1] = 88
print(tple)
# tple[3] = "hvbdhb"

# a tuple which has only one item in it which is even without a bracket should have a comma at the end of it.
tple2 = ("apple",)
print(type(tple2))

# unpacking a tuple
# the x , y , z are variables which takes and assigns the items of the tuple as per the index order
# even the tuple is unpacked and assigned to vaariables the tuple never bocomes empty
tple5 = (12, 22, 32)

x, y, z = tple5

print(x, y, z)
print(tple5)

# built-in tuple() function
# by using this built-in tuple function we can convert a mutable list into a immutable tuple

x = ["apple", "mango", "banana", "orange"]
print(x, type(x))

x = tuple(["apple", "mango", "banana", "orange"])
print(x, type(x))
print(type(x))

"""


"""
# converting dictionary and sets ino a tuple !

d = {"apple": "red", "mango": "yellow", "orange": "orange"}
print(d)
print(type(d))
d = tuple({"apple": "red", "mango": "yellow", "orange": "orange"})
print(d)
print(type(d))

s = {"abc", "def", "ghi", "jkl", "mno"}
print(s, type(s))

s = tuple({"abc", "def", "ghi", "jkl", "mno"})
print(s)
print(type(s))
print(s)
"""
# sets
# a set cannot have duplications which means a set cannot have two values with the same name
# a set is mutable

'''
set1 = {"one", "two", "one", "three", "four", "five", "five", "three", "four"}

print(set1)
print(type(set1))

# the above set had a duplication( two same values ) of one, five, three and four but when we print it the duplications are removed

# membership testing :-

set2 = {"aple", "mngo", "bnana", "kiwiii"}
print("aple" in set2)
print("goiyaaa" in set2)

# set() built-in function
# converting a tuple into a set
# by converting a tuple into a set it becomes mutable and the duplicate values are removed

tpl6 = ("abb", "abb", "abc", "abc", "efg")
print(tpl6, type(tpl6))

tpl6 = set(("abb", "abb", "abc", "abc", "efg"))
print(tpl6, type(tpl6))

# text literal


def func456():
    # its a comment
    """its a textliteral"""
    """its a multiline comment """

    print("hello world")

    return "hellowww"


print(func456())



# the ' ... ' indicates that the statment or function is created , but the implementation steps will be coded later

a = 3
if a <= 10:
    ...


def func4368():
    ...

'''

"""
# eval() function allows us to evaluate an expression from a string

code = input("enter some codeee  ")
eval(code)

# exec() function allows us to evaluate python statements not just expressions

code = input("enter some codeee  ")
exec(code)

"""


# frozenset() function

a = {"a", "b", "c", "d", "e"}

a = frozenset(a)
print(type(a))

# a[1] = "c" executing this code gives an error because frozenset makes a set immutable ... which could be used as a key in dictionary

# sum() function

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(l))

a = sum(l, start=5)
print(a)

# vars() function
# zip() function

# multiple variable asigning in single line

a, b, c, d, e = 1, 2, 3, 4, 5
print(a, b, c, d, e)

# inline / Ternary condition
# if-else condition in a single line

score = 10
# this is a multi-line if else statement
if score > 5:
    print("pass")

else:
    print("fail")

# the same statement in a single line
print("pass") if score > 5 else print("fail")

# storing it in a variable to use it later
a = "pass" if score > 5 else "fail"
print(a)

# *args and **kwargs


def fun222(name, age, section, gender):
    print(name, age, gender, section)


args = ["lalit", 19, "a", "male"]
kwargs = {"name": "lalit", "gender": "male", "section": "a", "age": 19}

fun222(*args)
fun222(**kwargs)

# for-else and while-else statement

# Camel Case:-  Each word, except the first, starts with a capital letter: myVariableName = "John Wick"
# Pascal Case:-  Each word starts with a capital letter: MyVariableName = "John Wick"
# Snake Case:-  Each word is separated by an underscore character: my_variable_name = "John Wick"

# assigning the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
# If you do not know how many arguments are going to be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# Recursive function :- it is a function which is calling itself
# String Formatting :-
# python has 67 buit-in functions & 33 keywords
