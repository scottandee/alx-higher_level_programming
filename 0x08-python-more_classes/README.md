# 0x08 - More Classes and Objects
Continuation from 0x06

## Class and Object Attributes
Class attributes belong to the class and are common to all instances. Object attributes belong to each instance and are differrent in all instances. Class and object arrtibutes are usually declared in different namespaces. If you try to access the value of an attribute of an ojbect (be it class/intance), the interpreter will forst check through the namespace of the object before it goes to check the namespace of the class itself. If it actually exists, you will get the correct value.

Class attributes can be accessed bu using the `cls.attr` or the `instance.attr`, any one will work fine. In the case that you want to change the value of the class attribute, using the `instance.attr` won't work correctly. It will declare a new instance attribute instead of changing the class variable.

## Static Methods
This solves the problem of accessing a private class attribute. It can be very useful in the case that we want a method that can be called by both the class and the instance without necessarily passing the reference to a class to it. It can return the private class attribute. If you try to use an instance method as a substitute for this, there'll be two problems. First, the instace has nothing to do with the method and then another problem will be you can't access the method without creating a new instance. If we omit `self`, we then cannot access it via instance, but we can access it via class name.

## Class Methods
These methods are bound to classes unlike static methods which are not bound to anything. They can be called via the instance or the class name. They are often used in the cases where we are declaring a factory method and also in the case where we have a static method calling another static method. It is also very helpful in inheritance in order to specify the action to take depending on the class.
