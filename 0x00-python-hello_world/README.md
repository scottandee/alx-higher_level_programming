# 0x00-Python - Hello, World
Python is a general purpose language that was created by Guido van Rossum. It is mostly popular for its object oriented form. It is an interpreted and not a compiled language. The language is named after the BBC show “Monty Python’s Flying Circus” and is no way related to a reptile

## Why Python?
* It's an interpreted language which means less time spent developing.
* Dynamic typing: The interpreter declares all the variables for you at runtime
* Simplicity
* Takes less lines of Code to solve problems

## Difference Between and Interpreted and a Compiled Language
A compiled Language is a language that is usually converted to machine code before it is then run and executed. An interpreted language is a type of language that is run straight away by the machine and involves no conversion. Compiled languages are typically faster than interpreted languages.

## The Python Interpreter
To open the python interpreter, enter `python3` into the terminal. Here are some useful flags that can be used with `python3`:
* `-c`: run a one liner command
* `-m`: searches sys.path  for the named module and runs the corresponding .py file as a script

Run `man python3` for more.
In order to access the previous output in the python interpreter, we can use the `_` variable. It contains the previous output.

## Python Command Line Args
We have to "import sys" for this. When we do this, the arguments and the script name is stored as an array of strings in the `argv` variable.

### Note
* To write multiple commands on the same line in python, we have to separate each command by a `'; '`.
* A floor division is a type of division in which the answer is usually rounded to a whole number.

## Python Strings
* Strings can be concetenated with the `+` and repeated with the `*`.
* Two string literals next to each other are automatically concatenated
* A string is a series of combined characters which can be indexed starting from `0`
* Indexing allows us to obtain a single character
* The index from the right starts from `[-1]` because `-0` is still equals zero
* A string can also be sliced. Slicing allows us to obtain a substring.
* `string[included:excluded]`
* for more [click](https://realpython.com/python-f-strings/)

## Using the `print` function
This function is used to print to the stdout. There are various ways in which this can be used which include:
* `print(r"some string")`: this is used to print a raw string ie a string that ignores all escaped characters
* `print(f"some atring")`: used to orint a formatted output
* `print("""...""")` or `print('''...''')`: these are string literals that spen multiple lines
* 
  
## What is Source Code and Object Code
Source code is the fundamental components of a computer program. It can beunderstood by programmers. Code witten in C, python or whatever language it might be is called a source code. One Source Code is compiled, it is referred to as Object Code.
* Proprietery: This code is owned by a specific organization and is not accessible to the whole world. 
* Source Code: This is developed with a lisence that allows anyone to view the code 
