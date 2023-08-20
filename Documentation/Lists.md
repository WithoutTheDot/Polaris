# Lists

## Declaration
In Polaris lists have a variable length, can contain many types and are mutable unlike strings. They are defined using `[]` with elements inside for example `VAR a = [1,2,"three"]`. 

## Multidimensional lists
In Polaris lists can be multidimensional by having list elements be other lists. To access an element in a multidimensional list see the example below:
```
VAR a = [[1,2,3],[4,3,2]]
a/0/2 #This would return 2
```
You can nest lists many times to create more dimensions

## Operations
### Mathmatical
The following mathmatical operations can be applied to lists: `+`, `-`, `/`

#### `+` Append
`+` Can be used to quickly append an element to the end of a list 
```
VAR a = [1,2,3]
PRINT(a+4)
# Output: [1,2,3,4]
```
#### `-` Remove
`-` Can be used to quickly remove an element at a certain index:
```
VAR a = [1,2,3]
PRINT(a-1)
# Output: [1,3]
```

#### `/` Index
`/` Is used to get an element at a certain index in a list
```
VAR a = [1,2,3]
PRINT(a/2)
# Output: 3
```

### Comparisons
Only two comparisons can be used on lists, `==` and `!=`.
#### `==` Equal to
This is used to directly compare the list and will only return true if all elements at all indexes are the same
```
[1,2] == [2,1]
0
```
#### `!=` Not equal to
This is the opposite of equal to and will return true if the lists re not the same
```
[1,2] == [2,1]
1
```

## Built-in Functions
The following functions are specific to lists


operations,comparisons, built in functions
