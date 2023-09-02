# 0x03 - Python Data Structures
Data structures are simply about organizing data in a way that it can be easily accessible and used efficiently. In this project, we explore some of the data structures avaliable in python.

## What are Sequence Data Types
These are data types that are used to store data in containers. Single storage units that are used to store multiple data items together. Esssentially, it is stored one after the other contiguously in memory. There are three major sequence data types which are Lists, Strings and Tuples

## Lists
A List is a set of comma separated values that are enclosed in square brackets. Tt can be sliced and indexed libe strings. It is mutable unlike strings which are immutable and supports concatenation with the `+` operator. Here are some common [methods](https://docs.python.org/3/tutorial/datastructures.html) associated with lists.

### Note:
* **Stacks**: Last in First Out(**LIFO**)
* **Queues**: First in First Out(**FIFO**)

## The `del` Statement
This can be used to remove an element or a slice from a list

## Tuple
This is a group of data separated by commas and are enclosed with parenthesis. It is of the immutable type. An empty tuple is represented by parenthesis i.e `()`. A tuple with one element is represented by `(elem, )`
### Tuple Unpacking
This is the art of assigning the content of a tuple to ots values
```python
tup = 1, 3, 5
```
### Sequence Unpacking
Sequence unpacking is the reverse of tuple packing
```python
x, y, z= t
```
***NOTE***: In sequence unpacking, the number of variables on the left must be equal to the number of elements in the sequence.
