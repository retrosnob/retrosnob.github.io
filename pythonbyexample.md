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
miles = float(input("Enter distance in miles: "))
print("That's " + str(miles * 1.60934) + " kilometres.")
```
### Program 2
This program does the same as Program 1.
```Python
miles = input("Enter distance in miles: ")
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
This program does the same as Program 1.
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjE0Mjg5MzIzLC0xNTE3NTY5Njg0LDcwNz
cyNjUzMiwtOTY1OTYyNzU4LC0xNzUwNTQzOTcyLC0xNDUyMzcx
NTg5LC0yMDk3MzQxNjE5LC00ODkyNTMxNTksMTQxODcxMTUzNS
wxNDE4NzExNTM1XX0=
-->