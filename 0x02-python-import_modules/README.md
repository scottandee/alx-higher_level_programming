# 0x02 - Python Import & Modules
A python [module](https://docs.python.org/3/tutorial/modules.html) is a file that contains python definitions and statements that can be reused. The filename is coined by combining the module name and `.py`. The module name in the module is usually stored in the global variable `__name__`.

## What is a Namespace?
This is a container which contains a mapping of variable names to a container. It's a way to organize and manage identifiers in order to avoid conflict.

## What is a Scope?
A scope is a region in a program where a namespace is directly accessible. There are four types which are

* Local Scope: this is a scope within a function. To tell python that the variable we want to work with is in the local scope, we can use `global var_name` 
* Enclosing Scope: This occurs in cases where we have a function nested in another function. The local scope of the enclosing function can be accessed by using `nonlocal var_name`
* Global Scope: The glocal scope is the scope which is accessible when a variable is declared in the main body of a module
* Builtin Scope: This contains variables that are predefined by python

## What is `import`
This is a way to tell python that you want to have access to the functions and definitions in another module.

### Ways to `import`
1. `import mod_name`: This adds the module to the current namespace but doesn't add all of the functions included in it. Using the module name, you can access the functions with the dot notation
2. `from mod_name import var_name, var_name...`: This imports specific names from a particular module. Note that the module itself will not be imported.
3. `from mod_name import *`: This imports all names from a function
4. `import mod_name as alias_name`
5. `from mod_name import var_name as alias_name`
