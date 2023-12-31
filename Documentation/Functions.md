# Functions

Functions in Polaris are used to wrap up blocks of code to be reused and provide more readability. Note functions and procedures are the same in Polaris and do not have to have a specific return type. Functions themselfves when created return themselves eg `VAR a = FUNC test(a,b) -> PRINT(a+b)` on a new line I could call the test function by using the variable a `a(10, 20)`

## Defining Functions
### Single Line Functions (useful for the shell)
```
FUNC test(a, b) -> PRINT(a*b)
```
In this case the function test is created with 2 parameters (a and b) and will print a*b. Note the `->` is required
### Multiline Functions
```
FUNC another_test(a,b)
  PRINT(a)
  VAR b = b^9
  PRINT(b)
  RETURN a*1^b
END
```
This function spans across many lines and is marked by the `END` keyword

## Calling Functions

Functions can be called using brackets and inside the brackets any parameters are passed into the functions.
```
another_test(7,2)
```
Parameters can also be other functions (called or uncalled) or variables. Functions can also be anonymous if defined without a name and are labelled `<anonymous>` 

## RETURN
`RETURN` is used to pass back a return value from a function. See the example below
```
FUNC add(a,b)
  RETURN a+b
END

VAR a = add(2,3)
PRINT(a)
```
The output would be `5`
