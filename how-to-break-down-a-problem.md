# How to break down a problem

Problem:

> Ask the user to input two numbers.  Print the sum of the two numbers.

What are the two parts of this problem?

1. Ask the user to input two numbers
2. Print the sum of two numbers

I suggest always skipping asking for input (part 1) and going directly to the other half of the problem (part 2).  
This avoids you having to manually type in values on every run AND gives you consistent values to work with every time.

#### Discuss: Why would this be faster?

```python
number1 = 5
number2 = 7

print(number1 + number1)

# Will you be able to spot the error?
```

### Asking for input

You can create a new program that just asks for input
```python
number1 = input("Enter a number:")
number2 = input("Enter a number:")
```

### Putting them together
When you combine the two pieces, you'll often encounter some errors:
```python
number1 = input("Enter a number:")
number2 = input("Enter a number:")

number1 = 5
number2 = 7

print(number1 + number1)

# What is the error?
```

After fixing the overlapping code:

```python
number1 = input("Enter a number:")
number2 = input("Enter a number:")

print(number1 + number1)

# What is the error?
```
