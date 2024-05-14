This program asks the user for their name and then says hello to them and tells them how many letters are in their name.

```Python
name = input("Enter your name: ")
print("Hello " + name + ". Your name has " + str(len(name)) + " letters in it.")
```

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
Tasks:
1. Write a program that asks the user to enter two words and then tells them how long the longest word that they entered was. If the words are the same length, then it should display an appropriate message along with the length of the words.
1. Write a program that asks the user to enter two words and then prints the longer of the two words. If the words are of the same length it should display an appropriate message along with both words.
