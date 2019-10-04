# Choose good test data

## A numeric example

Problem:

> Ask the user to input two numbers.  Print the sum of the two numbers.

### Think about your test data
Choose test numbers that:
* You will know the answer
* Are different from each other
* Are not too simple--make them complex enough that you might uncover irregularities.  I avoid 0, 1, and 2 for most problems.

#### You know the answer to the problem
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

#### The numbers are complex enough
```python
number1 = 1
number2 = 0

print(number1 ** number2)

# The answer is right but because of the test data how can you find the error?
```
#### Discuss: What are some good choices?

## Adlibs/strings example

Problem:
> Ask the user for their name, a plural noun, and a place.  Then print out their values in a sentence "My name is [name].  I am taking [plural noun] to [place]."

### Pick something you know the answer to
```python
name = "asf;kljsdaf;kjasdf;lkjasdf"
pluralnoun = "oisernnxdoijaesrtijsef"
place = "34ohrkjnsdgkjndrg;iergs"

print("My name is " + pluralnoun + ".  I am taking " + name + " to " + place + ".")

# How will you find the error?
```

### Pick different values
```python
name = "blarg"
pluralnoun = "blarg"
place = "blarg"

print("My name is " + pluralnoun + ".  I am taking " + name + " to " + place + ".")

# How will you find the error?
```

### Pick something reasonably complex
```python
name = "n"
pluralnoun = "pn"
place = "p"

print("My name is " + pluralnoun + ".  I am taking " + name + " to " + place + ".")

# How will you find the error?
```

#### Discuss: What are some good choices?
