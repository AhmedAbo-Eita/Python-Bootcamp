# Group Value Types
### Implement a function which takes a List a parameter and groups them according to their data types (integer or string) and return dictionary.

#### Hint :

* Use `isinstance()` function to check data type.

* Use `fromkeys()` method to solve this challenge

#### Example

```
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
group_types(custom_list)
```

Output

```{
 10: 'Integer', 
 'one' : 'String', 
 'two' : 'String', 
 'ten' : 'String', 
 20 : 'Integer', 
 30 : 'Integer', 
 'five' : 'String', 
 40 : 'Integer', 
 'nine' : 'String', 
 50 : 'Integer'
}
```