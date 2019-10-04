# Choose good test data

Problem:

> Ask the user to input two numbers.  Print the sum of the two numbers.

### Think about your test data
Choose test numbers that:
* You will know the answer
* Are different from each other
* Are not too simple--make them complex enough that you might uncover irregularities.  I avoid 0, 1, and 2 for most problems.

#### You know the answer
```python
number1 = 2348234832
number2 = 58813121

print(number1 + number1)

# Do you really know what to expect?
```

#### The numbers are different
```python
number1 = 4
number2 = 4

print(number1 + number1)

# How will you find the error?
```

#### The numbers are complex
```python
number1 = 1
number2 = 0

print(number1 ** number2)

# The answer is right but because of the test data how can you find the error?
```
