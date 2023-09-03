# 0x06 - Python Classes and Objects
Python is popularly known as an Object Oriented Programming Language. An object oriented programming language is one that wraps data and functionality into an object

## Types of Programming Languages
There are five major types of programming languages
1. **Procedural Programming Languages**: These are languages that contain a series of steps or procedure(functions) that guide the computer to the desired output. Examples are C,Java(it can also be used in this way)
2. **Functional Programming Languages**: [Functional](https://www.tutorialspoint.com/functional_programming/functional_programming_introduction.htm) Programming focuses on the output of mathematical functions. Each function produces a specific output depending on the input that is given. Exmples are Scala, and Haskell
3. **Objeect Oriented Programming Languages**: In this language, data is treated as objects which contain attributes and methods. Some exaples are Java, Python and C++.
4. **Scripting Languages**: These are languages that help to automate repititive tasks. Examples are python, bash, Node.js, and PHP
5. **Logic programming Languages**: Here, instead of telling the computer what to do, we're telling the computer how to make decisions. Examples are Absys and Prolog.

## OOP Concepts
* Data Encapsulation: It is the bundling of data with the methods that operate on those methods. This is acheived by producing getters and setters
* Information Hiding: data is hidden so it won't be sccidentally changed
* Data Abstraction: This is the combination of both data hiding and data encapsulation.
* Public Attribute: Used by anyone
* Protected Attribute: Used at ones rist
* Private: Should only be used by the owner. This is usually used in situations where we have to monitor the value of the atrribute and avoid accidentally changing that value. Private attributes usually have getters and setters. In the setter method of a private attribute, validation can be made in order to ensure that the right input goes into the private attribute.

## Terms Related to OOP
* **Class**: This is a new type.
* **Object**: This is an instance of a class.
* **Field**: This is a variable that belogs to an object.
* **Method**: This is function that belong to a class. This is usally defined within a class and has it's first parameter to be self
* **Attributes**: This is the collective name for functions and methods. There can be instace and class attributes. Instance attributes belong to an object/instance of a class and Class attributes belong to the class.
* **Self**: This is used to refer to the instance of an object.

## The `__init__` method
This method runs as soon as an instance of an object is created.

## Class and object Variables
[Fields](https://python.swaroopch.com/oop.html), are nothing but ordinary variables that are bound to the namespaces of the classes and objects. Class variables can be accessed by all instaces while Instace variables are specific to each instance. Note that an object variable with the same name as a class variable will hide the class variable!. We can dynamically create new class and instance attributes by doing `class/instance.attr`.  
## Some Note-worthy methods
* `.getattr`
* 
## Note
* `self.__class__` refers to the name of the class.
* We can access method and class docstrings by using `Class.__doc__` or `Class.method.__doc__`.
* To see all information about instances, we can use the `instance.__dict__` which returns a dictionary of the instance.
* Functions in python can also be attribute. They can serve as static functions like the one in C
* `__str__`: used to produce a nicely printed string representation.
* `__repr__`: used to produce an internal representation of an object. With `__repr__`, obj == eval(repr(obj))
* If `__str__` exists and `__str__` or print is called, it'll be applied. It won't be applied in the case that `__repr__` is called.
* If only `__repr__` exists, if print, `__str__` or `__repr__` is called, then it'll be called.
