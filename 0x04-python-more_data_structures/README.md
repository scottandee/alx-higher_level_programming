# 0x04 - More on Data Structures
Continuation from the previous project

## Sets
A set is a set of unordered collection with no duplicate elements. A set contains a comma separated values enclosed by curly braces.`set(content)` can be used to create a set. An empty set can be created by using `set()`. The set here is very similar to the set in algebra. Wecan perform difference, union, intersection

## Dictionary
A dictionary is a set of comma separated key value pairs that are enclosed by curly braces. Unlike sequence types which are indexed with numbers starting from zero, dictionaries are indexed by the keys. A pair of braces create an empty dictionary.

### Looping techniques:
* with `dic.items()`
* with `enumerate(list/dict/tuple)`

## Lambda, Map, Filter, Reduce
1. Lamba is used to create an anonymous function `lambda params: code`
2. Map is used to apply a function to a set of iterables `map(func, sequence)`
3. Filter is used to filter all of the elements of a function for which the function returns true `filter(func, sequence)`
4. Reduce is used to continuously apply the function to a sequence. It returns a single value `reduce(func, sequence)`
