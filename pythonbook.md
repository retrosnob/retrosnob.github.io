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

#### Naming conflicts

Some names in Python already mean something and you should therefore not use them as variable names. 

Some examples of names you should **not** use for variables are:

sum, max, min, int, float, bool, str, string, random, list, type, dir

Single-letter names are generally not a good idea but sometimes they're ok. For instance:

* i, j, k are often used as simple counter integers (integer means whole number)
* x, y, z are often used for coordinates

## Data types

Variables stored data and data can be of different types. The GCSE focuses on the following data types:

* Whole numbers (integers)
* Numbers with decimal points (floats)
* Sequences of text characters (strings)
* True/False variables (booleans)



## Vocabulary
**Intialisation**
Creating and giving a variable it's first value, e.g. `x = 5`
**Assignment**
Giving a variable its first or a new value. In Python, initialisation and assignment are the same except the initialisation is a special term used for the *first* assignment.

## Exercises
1. Which of the following are valid variable names in Python?
   - EMAILADDRESS
   - emailaddress
   - email-address
   - email_address
   - emailaddress1
   - 1emailaddress
2. Name the data type (integer, float, string, boolean) of each of these variables after they have been initialised:
    - `name = "Fred"`
    - `isPrefect = True`
    - `age = 15`
    - `height = 1.73`
3. Explain why `x` is not a good variable name for storing the height of a rectangle. What would be a better variable name?

# Getting input from the user
I include this section early because it quickly allows us to write interactive programs that do something useful. You can get input from the user by using the `input` function.

This program asks the user their name and then prints a "Hello " followed by whatever name they entered.
```Python
name = input("Enter your name: ")
print("Hello " + name)
```
Note the the `input` function always returns a string. 
# More about strings

# Operators and expressions

# Printing output to the screen

# Grouping lots a variables together with lists

# Selecting which lines of code to execute with If statements

# Looping: repeating a block of code once for every item in a collection (for loops)

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1NjkwMjI4Nyw0NjA0OTA2ODUsLTE1ND
A2MDI5NDIsMTUzNDIzMTQwNSw0NTE5ODc5MTIsLTU4OTQxOTc1
NCwtMjEzOTAwNTkzNSwtMTM3NTk4MjQxNCwtMTgwNDc3NzE2My
w2NTQ3NDYwODUsLTUxMDM0NDEzMF19
-->