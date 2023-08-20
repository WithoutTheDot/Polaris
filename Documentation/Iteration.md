# Iteration

Iteration in Polaris comes in two forms definite and conditional.

## Definite (FOR)

Definite iteration in Polaris comes in the form of a `FOR` statement this will happen a set number of times.
For statements are constructed in the following way `FOR VAR <identifier> = <number> TO <number> DO`
optionally the step keyword can be used to change the step value of the loop, this is optional. The numbers can be replaced with variables with a number value
```
FOR VAR i = 0 TO 10 DO
    PRINT(i)
END
```
This would output
```
0
1
2
3
4
5
6
8
9
```
### Step Value

`STEP` can be used to change the step value of the loop it can be positive or negative and the loop will count to the last value before the end value is reached. See example below.
```
FOR VAR i = 0 TO 11 STEP 2 DO
    PRINT(i)
```
This would output
```
0
2
4
6
8
10
```

## Conditional Iteration

In Polaris conditional iteration is implemented using a `WHILE` statement. This will take in an operation and completed the code if the condition is true. See the example below:
```
WHILE NOT INPUT() == "super secret password" DO
    PRINT("Try again")
END
```

## Break, Continue
These keywords can be used to control a loop at any point

### Break
`BREAK` is used to exit the current loop
```
FOR VAR i=0 TO 10 DO
    IF i == 8 THEN
        BREAK
    PRINT(i)
    END
END
```
The output would be
```
0
1
2
3
4
5
6
7
```

### Continue 
`CONTINUE` is used to move onto the next iteration of a loop
```
FOR VAR i=0 TO 10 DO
    IF i == 8 THEN
        CONTINUE
    PRINT(i)
    END
END
```
This would output
```
0
1
2
3
4
5
6
7
9
```
