# Other
This aims to cover anything that does not fall under the categories of the other documentation.

## Semi colons
Semi colons can be used to create multiline statements on one single line which is useful for the shell. They can also be used in a file but are not neccassery and are for more code readability and line efficiency.
```
VAR a = 10^4 # This is a valid line
VAR b = 10^5; # This is also a valid line
```

## Comments
In Polaris single line comments are made using `#` and all other text to the end of the line is ignored. Multiline comments do not exist in Polaris.
```
#This is a comment
```
## END
`END` is one of the most important keywords in Polaris as it is used to end a block of code this applies to the following and is only required inside files and is optional in the terminal (most of the time). 
It is required for the following codeblocks
- Functions
- While loops
- For loops
- If statements

```
VAR a = 0
WHILE TRUE DO
  IF a == 8 THEN
    PRINT("Hello")
  END
  VAR a = a+1
END
```

Semi colon,
END,
RUN and functions,
Comments
