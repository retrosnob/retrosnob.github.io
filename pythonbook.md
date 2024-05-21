# About this book
I often get students asking me if there is a book or a course they can do to learn more about Python and I often say no, because:
* Most books will cover lots of stuff you don't need to know for the GCSE
* The GCSE exam board (Edexcel) has weird ways of doing things that you won't find in books

So I have decided to write my own book that
* covers only what is covered by the GCSE
* tells you all the weird things that the exam board want you to do
# Getting started with Python
## Downloading Thonny
I recommend that you use Thonny as your Python editor because it has the Python interpreter built in. It can be downloaded from https://thonny.org and it perfectly good for GCSE and A-Level. 
## The Thonny interface
When you open Thonny you will see two panes. 

The upper pane is a text editor that allows you to edit Python files. Write whole programs in here and press the green play button to execute. (You will need to have saved the file somewhere first.)

The bottom pane is the shell. Here you can execute single lines of Python in an interactive REPL mode. When you write a line of code and execute it, Python will evaluate it and print the result. If the line of code doesn't evaluate to anything, nothing will be printed.

**The Thonny interface**
![Thonny user interface](http://retrosnob.github.io/PythonBook_ThonnyUI.png)

_Examples of using the interactive shell. _
![Thonny interactive shell](http://retrosnob.github.io/Thonny_shell.png)

**Thonny tips:**
* If your program hangs, use the red Stop button to halt it.
* You can clear the shell by right-clicking on it and choosing Clear.
* Thonny has an "assistant" that warns you of various things. I find it annoying. You can disable it in Tools, Options, Assistant....
* Python has a debugger built in. In my opinion, the default setting of *Nicer* is too verbose. You can change it to *Faster* in Tools, Options, Run & Debug....

# Variables and data types

## Variables

We can store items of data for use in computer programs. These stored items are called variables. We refer to variables using names.

``` Python
# Store the value 5 in a variable called x
x = 5

# Store the value "Fred" in a variable called name
name = "Fred"
```
You give a variable a value by using the `=`, which is known as the *assignment operator*. So when we assign the value 5 to the variable x like this `x = 5`, we are really saying *let x take the value of 5*. Some languages actually use the word `let` when they do assignment, e.g. `let x = 5`, but Python doesn't.

In the statement `x = 5`, the x is an *integer variable* and the 5 is an *integer literal*. Assignment always happens right to left. You cannot write 5 = x.  
### Variable names

Variable names can include letters, numbers and the underscore (_) character, but they cannot *begin* with numbers.

You should try to choose variable names that make it easy to tell meaning of the data held in the variable. 

> **GCSE tip: Capitalization in variable names**
> There are different conventions about whether to include capital letters in variable names or not. Edexcel likes to use **camel case**, in which the:
> * If the variable name is just one word, then it is all lower case.
> * If the variable is two or more words together, the first is lower case and the rest are title case (with the first letter capitalised).
> 
> The following variable names are in camel case:
> * name
> * emailAddress
> * passwordIsValid
> 
> You should probably adopt this convention (even though it's not normal for Python programmers, who generally use something called snake case).

#### Naming conflicts

Some names in Python already mean something and you should therefore not use them as variable names. 

Some examples of names you should **not** use for variables are:

sum, max, min, int, float, bool, str, string, random, list, type, dir

Single-letter names are generally not a good idea but sometimes they're ok. For instance:

* i, j, k are often used as simple counter integers (integer means whole number)
* x, y, z are often used for coordinates

## Data types

Variables stored data and data can be of different types. The GCSE focuses on the following data types:

* Whole numbers (**integers**)
* Numbers with decimal points (**floats**)
* Sequences of text characters (**strings**)
* True/False variables (**booleans**)

## Vocabulary
**Assignment**
Giving a variable its first or a new value. In Python, initialisation and assignment are the same except the initialisation is a special term used for the *first* assignment.
**Intialisation**
Creating and giving a variable it's first value, e.g. `x = 5`
## Exercises
1. Which of the following are valid variable names in Python?
   - EMAILADDRESS
   - emailaddress
   - email-address
   - email_address
   - emailaddress1
   - 1emailaddress
   - emailAddress
1. Which of the variable names for email address given above would you expect to see in an Edexcel GCSE paper?
. Name the data type (integer, float, string, boolean) of each of these variables after they have been initialised:
    - `name = "Fred"`
    - `isPrefect = True`
    - `age = 15`
    - `height = 1.73`
. Explain why `x` is not a good variable name for storing the height of a rectangle. What would be a better variable name?

# Getting input from the user
I include this section early because it quickly allows us to write interactive programs that do something useful. You can get input from the user by using the `input` function.

This program asks the user their name and then prints a "Hello " followed by whatever name they entered.
```Python
name = input("Enter your name: ")
print("Hello " + name)
```
Note the the `input` function **always** returns a string. *Returns* is a special term used in relation to functions. It means *gives back* and I will use it a lot in the section on functions later. 

It makes sense in the example above that `name` is a string, since it is a word, a sequence of characters, but try running this program:
```Python
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
print("The sum is " + str(n1 + n2))
```
> Enter the first number: 4
> Enter the second number: 5
> The sum is 45

This program has gone wrong because the *return type* of the `input` function is *string*, and when you use the *plus operator* (+) between two strings the strings are *concatenated*, i.e. chained together. 

We can fix this problem by *converting* the strings into integers, because when you use the plus operator (+) between two integers the integers are added.
```Python
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("The sum is " + str(n1 + n2))
```
> Enter the first number: 4
> Enter the second number: 5
> The sum is 9

Look carefully at the line:
```Python
n1 = int(input("Enter the first number: "))
```
This is the order of events:
1. Make a string literal "Enter the first number: " and *pass it* to the `input` function.
2. The input function then prints "Enter the first number: " and waits for the user to type something.
3. Take the thing that the user typed and pass it to the `int` function, which turns it from a string to an integer.
4. Assign that integer to the variable n1.

Now look carefully at the line:
```Python
print("The sum is " + str(n1 + n2))
```
Now that `n1` and `n2` are integers, we need to turn them back to strings before we can concatenate them with the string "The sum is ". We do this with the `str` function.

This is the order of events:
1. Add the values of the two integer variables n1 and n2.
2. The str function then turns the result from an integer to a string.
3. The string is then concatenated on the end of the string literal "The sum is " to form a longer string.
4. That longer string is then passed to the print function, which prints it out on the screen.

In summary:
* The `int` function is used to turn strings into integers. You will need to use it when you want to do arithmetic or comparison (e.g. <, >, etc) with the thing the user entered.
* The `str` function is used to turn integers into strings. You will need to use it if you want to concatenate an integer value to a string value before printing.

** Exercises:**
1. Write a program that asks the user to enter their age and then prints "You are N years old", where N is the age they entered.
2. Write a program that asks the user to enter their age and then prints "You are N+10 years old", where N+10 is their age plus 10 years. 
3. Explain why you need to use the `int` function in task 2 but not in task 1. 
# More about strings
## String functions
You have seen some functions that are built-in to Python, e.g. len, int, input, print. We refer to these as **built-in functions**. There are also functions just for strings. We refer to these as **string functions**. 

This program asks the user for their name and then prints it in capital (upper case) letters:

```Python
name = input("Enter your name: ")
print(name.upper())
```
You can call (execute, run) string functions by using dot notation: adding a dot after the string, followed by the name of the function, followed by ().
> **Watch out:**
> With any function, you must put () after its name if you want to **call** it. Try just printing name.upper and you will get an odd result because Python will try to print the function itself and not the result of calling it. 
> ```Python
> name = input("Enter your name: ")
> print(name.upper) # left out the brackets!
> 
> # prints <built-in method upper of str object at 0x000002B1FE6E5E30>
> ```

### String functions in the GCSE
The GCSE expects you to be familiar with the following string functions  (\<str\> just means any string variable):

| Function | Description |
| --- | --- |
| \<str\>.lower | Returns \<str\> as all lower case |
| \<str\>.upper | Returns \<str\> as all upper case |
## Strings as sequences
There are two **sequence types** that you need to be familiar with for the GCSE: **strings** and **lists**. Sequence types allow you to:
* Get individual items of the sequence using an **index**.
* **Iterate** through every item in the sequence using a **for loop**.
* Use the keyword **in** to check if an item is in the sequence (although the GCSE doesn't seem to use this much).

### Example of string indexing
Consider this program, which asks the user for their name and tells them the 4th character:
```Python
name = input("Enter your name: ")
print("The 4th character of your name is " + name[3])
```
**Notes:**
* We put `name[3]` because counting starts at zero.
* If the name is less then 4 characters we will get an `IndexError`, meaning we've tried to access an item of a sequence that isn't there.
### Example of iterating through a string using a for loop
Consider this program, which counts the number of "a"s in the string "Aardvark", but iterating through the string.
```Python
count = 0
s = "Aardvark"
for ch in s:
	if ch == "a":
		count = count + 1
print("There are " + str(count) + " a's in " + s)
```
**Notes:**
* It's ok to use a single-letter variable name like `s` in this example, because my variable is just a throw-away value.
* We have to use the `str` function to convert the integer `count` to a string before we can concatenate it with the rest of the message string, but we don't need to do that with `s` because `s` is already a string.
* This example prints 2, because Python is case-sensitive; "a" is different from "A".
### Example of using `in` to check if a character is in a string
Consider this program, which says whether there is a "z" in the user's input.
```Python
s = input("Enter some text: ")
if "z" in s:
	print("There is a z in what you typed")
else:
	print("There is no z in what you typed")
```
# Operators and expressions
## Arithmetic operators
The GCSE requires you to know the following arithmetic operators:
| Operator | Operation | Example | Result
|---|---|---|---|
|+|Add|19+5|24|
|-|Subtract|19-5|14|
|*|Multiply|19*5|95|
|/|Divide|19/5|3.8|
|//|Integer division|19//5|3|
|%|Modulo (remainder after division)|19%5|4|
|**|To the power|19**5|2476099|

## Comparison operators
The GCSE requires you to know the following comparison operators.
|Operator|Description|Example|Result|
|---|---|---|---|
|==|is equal to|5 == 5|True|
|!=|is not equal to|5 != 5|False|
|>|is greater than|5 > 5|False|
|>=|is  greater than or equal to|5 >= 5|True|
|<|5 < 5|is less than|False|
|<=|is less then or equal to|5 <= 5|True|

## Logical operators
Consider the following two statements:
1. Paris is the capital of France
2. Beijing is the capital of Germany

It is clear that **statement 1 is True** and **statement 2 is False**.

Now consider the statements:
1. Paris is the capital of France **and** Beijing is the capital of Germany
2. Paris is the capital of France **or** Beijing is the capital of Germany

**Statement 1 is False**, because both statements either side of AND need to be True for the whole statement to be True.
**Statement 2 is True**, because only one of the statements either side of OR need to be True for the whole statement to be True.

In general then:

something True **and** something False is **False**
something True **or** something False is **True**

We can summarise how the logical operators work using **truth tables**.

This is the **truth table for AND**:

| Statement | Result
|---|---|
True and True|True|
True and False|False|
False and True|False|
False and False|False|

This is the **truth table for OR**:

| Statement | Result
|---|---|
True or True|True|
True or False|True|
False or True|True|
False or False|False|

### Logical operator precedence and the use of brackets
You are familiar with the idea of operator precedence from mathematics. For instance `5 - 3 x 2 = -1`, whereas `(5 - 3) x 2 = 4`.

In Python, `and` takes precedence over `or`. For example, `True or False and False` evaluates to `True`, whereas `(True or False) and False` evaluates to `False`.

I think it's unlikely that the GCSE would require you to know this, but it's handy to know when you write your own programs.

## Example program using operators
This program asks the user to enter a number between 1 and 10 (inclusive) and prints an appropriate message.
```Python
number = int(input("Enter a valid number (1-10): ")):
print("Number valid: " + str(number > 0 and number < 11))  
```
This program does the same.
```Python
number = int(input("Enter a valid number (1-10): ")):
print("Number valid: " + str(number >= 1 and number <= 0))  
```
Output:
> Enter a valid number (1-10): 6
> Number valid: True
> Enter a valid number (1-10): 14
> Number valid: False

## Notes
1. A statement that evaluates to True or False is known as a *condition*.
2. Note that when using logical operators, each side of the operator has to be an expression which **on its own** evaluates to True or False. So if you want to check that a and b are both greater than 10, for instance, you have to write `a > 10 and b > 10`. You **cannot** write `a and b > 10`; in fact this will lead to a nasty bug.
## Exercises
1. Write two statements involving countries and capitals such that if you put an OR operator between them the whole statement is False.
2. Write a condition that evaluates to True if `n` is positive and even, and False otherwise. Hint: What is the remainder on division by 2 for numbers that are even?
# Printing output to the screen
Here is a summary of the main ways of printing strings (and variable values) to the console (screen). For each, `age` is an integer variable with value 15.

---
`print(age)`
> 15

This works ok. The print function can print types other than strings. 

---
`print("Fred is", age, "years old.")`
> Fred is 15 years old.

This works ok. If you separate string literals and variables with commas, Python automatically puts a space between them (but sometimes you won't want it to).

---
`print("Fred is " + age + " years old.")`
> **TypeError!** You cannot concatenate strings and integers.

This works ok. The print function can print types other than strings. 

---
`print("Fred is" + str(age) + "years old.")`
> Fred is15years old.

This works ok but we forgot to add spaces where we needed them.

---
`print("Fred is " + str(age) + " years old.")`
> Fred is 15 years old.

This works ok (same as above but with spaces) because we have converted the integer to a string using the `str` function before we concatenated it. **This is used in the GCSE and *must* be used when the question tells you to use concatenation.**

---
`print("Fred is {} years old.".format(age)`
> Fred is 15 years old.

This works ok. More information about this is given later in the chapter. **This is heavily used in the GCSE and must be used when the question tells you to use the format function.** 

---
`print(f"Fred is {age} years old.")`
> Fred is 15 years old.

This works ok. This is the modern way to print variables and string literals, but it is not used in the GCSE. 

### Using the format function
The basic use of the format function can be seen in the program below.
```Python
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (m): ")
lay
```

# Grouping lots a variables together with lists

# Selecting which lines of code to execute with If statements

# Looping: repeating a block of code once for every item in a sequence (for loops)

# Looping: repeating a block of code as long as a condition is true (while loops)

# Functions: named blocks of code that do a job and return a result

# Working with files


# This is heading 1
## This is heading 2
### This is heading 3

This is normal text. 

This is *italic*.

This is **bold**.

This is ~strikethrough~.

This is <span style="color: red">red</span>. This doesn't work. 

```python
for word in words:
    print(len(word))
```

Click [here](http://www.google.com) to go to Google.

Operation | Operator
--- | ---
add | +
subtract | -
multiply | *
divide | /

# Ideas
A selection of Youtube videos to accompany the text.
Downloadable Python source files and data files. 
Error types and what they mean. 
Exercises that require students to correct errors, e.g. not using brackets after a function call, etc, etc, etc
Must provide answers to exercises
Common things like counting and keeping a running total
Where to get more practice: e.g. project Euler, adventofcode

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU4Mzk3Mzg4MywtMTI3NjUxOTgwNCw4OD
I2Mzg5MTIsMTkxOTIyNjMxMSwtMTcwNDM5MzMwOSwxOTM3NDk1
NTM0LC01NTA0MzA1NzYsNTEzNTA3MDUxLC04MTQ2NjUwMzAsMT
YxNDQ3OTgxOSwyODg4NzY0NzQsLTExMzQ1MTkxMjgsLTE4Mjkx
MTI3NjksLTk1MDEwNjQyMCwtODM2Njc2MTczLDgwNjAxNTc5MC
wtMTIxNzgxMTQ1MywtNjg4MTAyMzk0LDE4MDU5NTY2MDUsMTU0
ODI0NTM2Ml19
-->