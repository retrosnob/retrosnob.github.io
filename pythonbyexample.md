This program asks the user for their name and then says hello to them and tells them how many letters are in their name.

```Python
name = input("Enter your name: ")
print("Hello " + name + ". Your name has " + len(name) + " letters in it.")
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

