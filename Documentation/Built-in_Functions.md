# Built in functions

**The following is a list of all built in functions, their parameters, returns and uses**
--------------------------------------------------------------------------------------
| **Function Name** | **parameters**               | **Return**      | **Use**            |
|-------------------|------------------------------|-----------------|--------------------|
| PRINT()           | 1, what to output: any type  |     0           |  Output To Display |
| PRINT_RET()       | 1, to return: any type       | parameter as String |  Used to output to terminal
| INPUT() | 0 | The input from user as a string | Used for basic user input |     
| INPUT_INT() | 0 | Input as int| Get integer inputs eg age |
| INPUT_FLOAT() | 0 | Input as float | Get float input eg height |
| CLEAR()/CLS() | 0 | 0 | Clears the screen |
| IS_NUM() | 1, what to check: any type | boolean value of if parameter is num | Test if something is a number|
| IS_STR() | 1, what to check: any type | boolean value of if parameter is str | Test if something is a string|
| IS_LIST() | 1, what to check: any type | boolean value of if parameter is list | Test if something is a list|
| IS_FUN() | 1, what to check: any type | boolean value of if parameter is func | Test if something is a function|
| LEN() | 1, what to check: list or string | integer value of the length |
| RUN() | 1, filename to run: string | 0 | Run files |
| STR() | 1, to convert: number | parameter converted to string | converting numbers to string|
| INT() | 1, to convert: valid string, float | parameter converted to int | converting numbers to int|
| FLOAT() | 1, to convert: number, valid string | parameter converted to float | converting to float |
| RANDINT() | 2, range: int | random int within the range | generating random numbers |
| DEBUG() | 0 | 0 | Entering debug mode: DANGEROUS |
| TIME() | 0 | Current time | Benchmarking |
| QUIT() | 0 | 0 | Quiting | 
| APPEND() | 2, list: list, item: any | 0 | Used to appened an item to a list |
| POP() | 2, list:,  list, index: int | The popped element | used to remove an element from a list |
| EXTEND() | 2, list to extend: list, other: list | 0 | Used to extend a list |
| EDIT() | 3, list:list, index: integer, value: any | 0 | Used to edit an element at a certain index |
| INSERT() | 3, list:list, index: integer, value: any | 0 | Used to insert an item at a certain index |
| REPLACE() | 3, string:string, from:string, to:string | New string | Used to replace a substring with another substring |
| SPLIT() | 2, string:string, delimiter:string | list of split string | used to split a string by a substring |
--------------------------------------------------------------------------------------
