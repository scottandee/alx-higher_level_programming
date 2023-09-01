# 0x01 - Python If/Else, Loops and Functions
In this project, we explore the various tools used to make decisions i.e conditionals, iterate over a range of values and the art of function creation.

## if, elif, else
## for
This is quite different for the for loop in C. It can help you iterate over any sequence ie list or strings
```python
words = ["Hi", "I'm", "Scott"]
for word in words:
    print(word)
```

## range()
The range function helps you to itereate over a number of arithmetic progressions
```python
for i in range(start, end, step):
    # code
```

## break and continue
The `break` statement breaks out of the most innermost `for` or `while` loop. `continue` goes to the next itereration immediately.

## pass statement
The pass statement is used as a placeholder for future code. This avoids receiving error messages when empty code is not allowed.

## match statement
This is very similar to the switch statement in C

## Defining Functions
Functions can be defined by using the `def` keyword followed by the function name and parameters in brackets

## Specifying Type for String Formatter
To do this, we have to specify `{field_or_index_number:conversion}`. Where conversion is the type of variable we want to print
```python
print("{:f}".format(76.828))   # 76.828
print("{:.2f}".format(76.828)) # 76.82
```
For more, [click](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)

## What is a Traceback
A [traceback](https://realpython.com/python-traceback/) is a report containing the function calls that you made in your code at a specific point which resulted into an exception error message. It's usually helpful to read this message from the bottom-up.
