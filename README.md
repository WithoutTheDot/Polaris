# My Programming Language



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Hello and welcome to my programming language. This project represents a simple exploration of how programming languages are made. While not highly advanced, this language covers the fundamentals and includes a basic (albeit imperfect) error-handling system. To install, please refer to the [Installation Instructions](#installation) section below. I hope you enjoy my language.

## Features

Key features of my language

- Basic Arithmetic including logical operations
- A variety of data structures
- Variables
- Conditional Statements
- Iteration (Conditional and definite)
- Functions

## Getting Started

### Installation

#### Step 1
Clone the git

#### Step 2 
Move the [myl](https://github.com/WithoutTheDot/MyLanguage/tree/main/myl) folder to the following directory (ensure that it is on the correct user's folder) `~/.vscode/extensions`. Once you have reloaded Visual Studio Code, syntax highlighting will be enabled for `.myl` files

#### Step 3
To enable access to run `.myl` files anywhere on your computer on windows in powershell (run as administrator) execute the following commands (__ensuring that you have edited the path__)

```powershell
$shellDirectory = "C:\Users\PATH\TO\MyLanguage\dist"
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$shellDirectory", [EnvironmentVariableTarget]::Machine)
```
This will allow you to directly run programms which are not in the path of `shell.py`.
You should now be able to move onto the next steps

## Usage

After completing the instructions from the installation section you can use the language in 2 ways:

- Via the Shell
- Reading from Files

### Via the Shell
The shell provides a simple way to execute code directly and is useful for debugging. It is important to note that multiline statements can be inputed into the shell by using ; to seperate lines. 

To start the shell either run [shell.py](https://github.com/WithoutTheDot/MyLanguage/tree/main/MyLanguage) from the [Mylanguage folder](https://github.com/WithoutTheDot/MyLanguage/tree/main/MyLanguage) or in powershell
```
shell.exe
```

### Reading from Files
Files can be directly read from command line inputs, the output will be directly shown in the terminal window you executed the command. To run a file see below:
```
shell.exe my_file.myl
```
This would execute the my_file.myl program


## Contributing

Contributing is recommended, if you have an idea please feel free to fork this repository and I test out your improvements and add them.

