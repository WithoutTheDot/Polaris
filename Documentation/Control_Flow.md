# Control Flow

In Polaris the flow can be controlled using `IF` statements. Note these will be needed to be closed with the `END` keyword if on multiple lines

## IF
An `IF` statement takes in a condition followed by `THEN` and executes the following code:

```
IF 10 == 5 THEN 
    PRINT("Maths is broken")
END
```
In this case nothing will be outputed as 10 is not equal to 5

## ELIF

`ELIF`, short for else if, can provide additional statements to control flow and the condition is also followed by `THEN` see example below:

```
IF 10 == 5 THEN 
    PRINT("Maths is broken")
ELIF 2 == 3 THEN
    PRINT("Math is still broken")
END
```
Both conditions are not true so no output will be seen

## ELSE
Else code is executed if no condition is true.

```
IF 10 == 5 THEN 
    PRINT("Maths is broken")
ELIF 2 == 3 THEN
    PRINT("Maths is still broken")
ELSE
    PRINT("Maths works!")
END
```
In this case the output will be `Maths works!` as 2==3 is false and 10==5 is false.

## Useful Example
A more useful example to using if statements is the following:
```
VAR pass = "password"
VAR user = "Bob_Smith23"

PRINT("Enter Username:")
VAR attempted_user = INPUT()
PRINT("Enter Password:")
VAR attempted_pass = INPUT()

IF attempted_user == user AND attempted_pass == pass THEN
    PRINT("Access granted")
ELSE 
    PRINT("Access Denied")
END
```
