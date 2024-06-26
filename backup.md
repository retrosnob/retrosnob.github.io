=== Program 1

This program asks the user for a distance in miles and converts it to kilometres.

```Python
miles = float(input("Enter distance in miles: "))
print("That's " + str(miles * 1.60934) + " kilometres.")
```

=== Program 2

This program does the same as Program 1.

```Python
miles = float(input("Enter distance in miles: "))
print("That's {} kilometres.".format(miles * 1.60934))
```

=== Program 3

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

=== Program 1

This program asks the user for their name and then says hello to them and tells them how many letters are in their name.

```Python
name = input("Enter your name: ")
print("Hello " + name + ". Your name has " + str(len(name)) + " letters in it.")
```

=== Program 2

This program does the same as Program 1.

```Python
name = input("Enter your name: ")
print("Hello {}. Your name has {} letters in it.".format(name, len(name)))
```

=== Program 3

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
