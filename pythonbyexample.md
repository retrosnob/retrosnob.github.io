### Program 1
This program asks the user for their height in metres and prints it. It doesn't work properly.
```Python
height = int(input("Enter your height (m): "))
print("Your height is " + str(height))
```
### Program 2
This program asks the height in metres of two people. It then adds them together and prints the result. It doesn't work properly.
```Python
n1 = input("Enter the first height (m): ")
n2 = input("Enter the second height(m): ")
print("The combined height is " + n1 + n2 + " metres.")
```
**Tasks:**
1. Run Program 1 and test it with various heights, including 1.7 metres. Describe how it behaves. Fix Program 1 using the ```float``` function. Write a short paragraph explaining why the program didn't work. Your paragraph should use the terms *int, float, function, truncate, decimal point*.
2. Run Program 2 and describe how it behaves. Fix Program 2 using the ```float``` function and the ```str``` function. Write a short paragraph explaining why the program didn't work. Your paragraph should use the terms *float, str, string, function, plus operator, add, concatenate*.

### Program 1
This program asks the user for a distance in miles and converts it to kilometres.
```Python
miles = float(input("Enter distance in miles: ")
print("That's " + str(miles * 1.60934) + " kilometres.")
```
### Program 2
This program does the same as Program 1.
```Python
miles = input("Enter distance in miles: "))
print("That's {} kilometres.".format(float(miles) * 1.60934))
```
### Program 3
This program asks the user to enter a character and tells them if it was a vowel or not. Note that it is case insensitive and it prints an appropriate message if the user didn't enter a letter or entered more than a single character.
```Python
letter = input("Enter a letter: ")

if letter.isalpha() and len(letter) == 1:
    if letter.lower() in "aeiou":
        print("You entered a vowel.")
    else:
        print("You didn't enter a vowel.")
else:
    print("You didn't enter a letter.")
```
**Task:**
1. Write a program that asks the user to enter a number and then asks them to enter C or F. If they enter C it should convert the number from Fahrenheit to Celsius and print the result. If they enter an F it should convert the number from Celsius to Fahrenheit and print the result. It should be case insensitive and if they enter neither C nor F it should print an appropriate message.

### Program 1
This program asks the user for their name and then says hello to them and tells them how many letters are in their name.
```Python
name = input("Enter your name: ")
print("Hello " + name + ". Your name has " + str(len(name)) + " letters in it.")
```
### Program 2
This program ees the same as Program 1.
```Python
name = input("Enter your name: ")
print("Hello {}. Your name has {} letters in it.".format(name, len(name)))
```
### Program 3
This program asks the user for two numbers and then tells the user which of the numbers was the larger.
```Python
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 > n2:
    print("The first number is greater than the second.")
elif n2 > n1:
    print("The second number is greater than the first.")
else:
    print("The numbers are the same.")
```
**Task:**
1. Write a program that asks the user to enter two words and then prints the longer of the two words. If the words are of the same length it should display an appropriate message along with both words.

### Program 1

This program creates a list of integers and prints them out on separate lines.
```Python
nums = []
nums.append(2)
nums.append(3)
nums.append(5)
nums.append(8)

for num in nums:
	print(num)
```
### Program 2
This program does the same as Program 1.

```Python
mylist = []
mylist.append(2)
mylist.append(3)
mylist.append(5)
mylist.append(8)

for thing in mylist:
	print(thing)
```
### Program 3
This program asks the user for a password. If the correct password "sesame" is entered, the program displays an appropriate message. If not, the program displays an appropriate message and prompts for a new password attempt. 
```Python
password = input("Enter a password: ")
while password != "sesame":
	print("Incorrect password")
	password = input("Enter a password: ")
print("Access granted")
```
**Task:**

1. Write a program that asks the user to enter single words. It should keep asking the user to enter a word until the user enters an empty string. (An empty string is written in Python as "" and is entered by the user by just pressing Enter in response to an input prompt.) After the user has finished entering words, the program should print all the words that the user entered, one per line.

### Program 1
This program asks the user to enter a single character and then tells the user if the character is an uppercase letter, a lower case letter, a number or is non-alphanumeric (neither a letter nor a number). If the user has not entered a single character, the program displays an appropriate message.
```Python
character = input("Enter character: ")
if len(character) != 1:
	print("Single character not entered")
else:
	if character.isalpha():
		if character.isupper():
			print("Upper case")
		else:
			print("Lower case")
	elif character.isdigit():
		print("Number")
	else:
		print("Non-alphanumeric")
```

### Program 2
This program asks the user for string input and tells the user if the string is of mixed case (contains both upper and lower case letters) or not. 
```Python
text = input("Enter text: ")
containsUpper = False
containsLower = False
for character in text:
	if character.isupper():
		containsUpper = True
	elif character.islower():
		containsLower = True
if containsUpper and containsLower:
	print("Mixed case")
else:
	print("Not mixed case")
```

### Program 3
This program does the same as Program 2, but it defines a function `mixedCase` to help.
```Python
def mixedCase(pString):
	containsUpper = False
	containsLower = False
	for character in pString:
		if character.isupper():
			containsUpper = True
		elif character.islower():
			containsLower = True
	return containsUpper and containsLower
	
text = input("Enter text: ")
if mixedCase(text):
	print("Mixed case")
else:
	print("Not mixed case")
```
**Task:**
Write a program that asks the user for a new password and then tells them if the password is valid. In order to be valid, a password have at least 6 characters and must contain at least one upper case letter, at least one lower case, at least one digit and at least one non-alphanumeric character. The program should define a function passwordValid that takes the password as a parameter and returns True if the password is valid and False if it is not valid.

### Program 1

This program defines a function to swap the two items of a list that are at indexes m and n. It tests the function on the list [12, 45, 23, 85, 31, 77] using m = 1 and n = 4.

```Python
def swap(lst, m, n):
	tmp = lst[n]
	lst[n] = lst[m]
	lst[m] = tmp

nums = [12, 45, 23, 85, 31, 77]
swap(nums, 1, 4)
print(nums)
```

### Program 2

This program does the same as Program 1.
```Python
def swap(lst, m, n):
	lst[m], lst[n] = lst[n], lst[m]
	lst[n] = lst[m]
	lst[m] = tmp

nums = [12, 45, 23, 85, 31, 77]
swap(nums, 1, 4)
print(nums)
```

### Program 3
This program defines a function to to find whether all numbers in a list are divisible by a certain number n. It tests the function on the list [12, 45, 23, 85, 31, 77] with n = 3.

```Python
def isAdjacent(lst, n):
	for num in lst:
		if num % n != 0:
			return False
	return True
```

**Task:**

1. Write a program that defines a function to see if a list is in ascending order. Test it with these different lists:
    - [1, 3, 6, 9]
    - [4, 7, 2, 5]
    - [1, 4, 4, 8]

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTg3NzM4NDEsLTE3MjExMzMxMzUsLT
YwNDg3ODg4OSwtMTg2MTAxMTc1OSwtMTkyMDAxMTYwMiwtNDE5
ODQ0MzYyLDY5MDE0MzIwOSw2MTQyODkzMjMsLTE1MTc1Njk2OD
QsNzA3NzI2NTMyLC05NjU5NjI3NTgsLTE3NTA1NDM5NzIsLTE0
NTIzNzE1ODksLTIwOTczNDE2MTksMTQxODcxMTUzNSwxNDE4Nz
ExNTM1XX0=
-->