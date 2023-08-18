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

### Accessing Variables
Variables can be accessed with the identifier and no other syntax
```
VAR b = a+10
```

## Numbers
In Polaris floats and integers are under the same type, numbers, and can be used interchangeably. Built in methods and functions are based around numbers for example `IS_NUM(20)` would return `1` for true as there are not booleans in this language.
The example below shows how to assign a variable a number.
```
VAR c = 100
```

## Strings
In Polaris strings are identified with `""` and are assigned in the same way. To learn more about strings visit the [String documentation](https://github.com/WithoutTheDot/Polaris/edit/main/Documentation/Strings.md)
```
VAR str = "Hello, World!"
```
## Lists
Lists are of variable length in Polaris and are defined using []. Lists can have multiple types within them including other lists to create multidimensional lists. For more information of Lists visit the [List documentation](https://github.com/WithoutTheDot/Polaris/edit/main/Documentation/Strings.md)
```
VAR list = ["This", "is", "a", "list", 1,2,3, [4,5]]
```
