# Variables

Variables come in 3 types in this language listed below
- Numbers
- Strings
- Lists

## Defining Variables
To define a variable use the `VAR` keyword followed by an identifier, equals then a value, see example below
```
VAR a = 10
```
When executing in the shell the return value of assigning a variable is printed
```
polaris > VAR b = 100
100
```
This can lead to multiple variables being assigned the same value at once:
```
VAR a = VAR b = 10
```
This would result in both `a` and `b` being assigned `10`


### Reassignment 
Variables can be reasigned with the `VAR` keyword, see example below
```
VAR a = a + 10
```

## Numbers
In Polaris floats and integers are under the same type, numbers, and can be used interchangeably. Built in methods and functions are based around numbers for example `IS_NUM(20)` would return `1` for true as there are not booleans in this language.
