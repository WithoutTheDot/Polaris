# Strings

## Declaration
As in most languages strings are declared with `""` but it is important to note that single quotes are not recognised so are free to use within the file without [Escape Characters](#escape_chars). For example `"This is a 'valid' string"`. 


## Escape Characters <a name = "escape_chars"></a>

Escape Characters allow a character (previously reserved) to escape and is escaped by the `\` character. There are also two preset escape characters. Shown below:

- `"\n"` new line
- `"\t"` tab

This can result in multiline strings see the example below:
```
"\t Menu \n---------------------\n \t Play \n\t Quit \n---------------------"
```
Would result in
```
"        Menu
---------------------
         Play
         Quit
---------------------"
```
## Operations
### Mathmatical
The following symbols can be applied to a string `+`,`*`,`/`.

#### +
This concatonates two strings to create a larger one. Note no space is added.
```
"Hello" + " World"
"Hello World"
```
#### *
This multiplies a string and repeats it an integer number.
```
"Hello " * 3
"Hello Hello Hello"
```
#### / 
This gets the character at the index (integer).
```
"Hello World"/3
"l"
```
### Comparisons
Two comprisons can be applied between two strings `==` and `!=`
#### ==
Checks if the value of both strings are the same
```
"Hello" == "Hello"
1
```
#### != 
Checks if the value of both strings are not equal
```
"Hello" != "World"
1
```
## Built in functions
The following built in functions are specific to strings

| Function | Parameters | Return | Use |
|----------|------------|--------|-----|
| REPLACE() | string: string, from: string, to:string | New replaced string | Replacing substring with another string |
| SPLIT() | string:string, delimiter: string | Arr of split string | Used to split a string by a substring |
-----------------------------------------
