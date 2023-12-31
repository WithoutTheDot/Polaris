# Basic Arithmetic and Operators

## Arithmetic

Arithmetic can be directly entered into the shell and the output will be returned. Integers and floats can be mixed and can be positive or negative

#### Addition

```
basic > 1 + 2
3
```
#### Subtraction

```
basic > 5 - 10.5
-5.5
```
#### Multiplication

```Polaris
basic > 5 * 10
50
```
#### Division
```Polaris
basic > 5/4
1.25
```
#### Raising to a power
```Polaris
basic > 16^(1/2)
```
## Brackets
It is important to note that brackets can change the order of operation in arithmetic. See example below:
```
basic > 16^1/2
8
basic > 16^(1/2)
4
```
## Logical Operators
The 3 main logical operators are implemented in this language but return integers (1 or 0) rather than booleans and only work with numbers.
#### AND
```
basic > 1 AND 0
0
```
#### OR
```
basic > 1 OR 0
1
```
#### NOT
```
basic > NOT 0
1
```

## Comparison Operators

All comparison operators work between integers and floats but `==` and `!=` work between strings and strings and lists and lists

#### Is equal to

```
basic > 1==200
0
```
#### Is not equal to

```
basic > 1!=200
1
```
#### Greater than
```
basic > 1>200
0
```
#### Greater than or equal to
```
basic > 1000>=200
1
```
#### Less than
```
basic > 1<200
1
```
#### Less than or equal to 
```
basic > 1>=200
0
```

