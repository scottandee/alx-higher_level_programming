# 0x05 - Python Exceptions
There are two major types of errors you might eencounter in python; syntax and exception errors. Syntax errors are errors that are encountered when you're fairly new to the python syntax. Exceptions are simply errors that are encountered in execution and are typically not as fatal as syntax errors.

# Handling Exceptions
`try` and `except` blocks are the mechanism put into place to handle exceptions.
* `try` : The code that might raise an exception is placed in here
* `except ExceptionName`: The exception you're trying to catch will be specified here. And the code you plan to execute will be indented within this. The exception can be aliased like so: `except ExceptionName as e`
* `else`: This block runs if no exception is raised in the try block
* `finally`: This code runs regardless of if an exception is raised. It is usually referred to as a clean up action

# Raising Exceptions
* `raise ExceptionName`
