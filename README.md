![Logo](/img/banner.png)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Hello and welcome to my programming language. This project represents a simple exploration of how programming languages are made. While not highly advanced, this language covers the fundamentals and includes a basic (albeit imperfect) error-handling system. To install, please refer to the [Installation Instructions](#installation) section below. I hope you enjoy Polaris.

## Features

Key features of Polaris

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
Move the [pol](https://github.com/WithoutTheDot/Polaris/tree/main/pol) folder to the following directory (ensure that it is on the correct user's folder) `~/.vscode/extensions`. Once you have reloaded Visual Studio Code, syntax highlighting will be enabled for `.pol` files

#### Step 3
To enable access to run `.pol` files anywhere on your computer on windows in powershell (run as administrator) execute the following commands (__ensuring that you have edited the path__)

```powershell
$shellDirectory = "C:\Users\PATH\TO\Polaris\Polaris\dist"
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

To start the shell either run [shell.py](https://github.com/WithoutTheDot/Polaris/tree/main/Polaris) from the [Polaris folder](https://github.com/WithoutTheDot/Polaris/tree/main/Polaris) or in powershell
```
polaris.exe
```

### Reading from Files
Files can be directly read from command line inputs, the output will be directly shown in the terminal window you executed the command. To run a file see below:
```
polaris.exe my_file.pol
```
This would execute the my_file.pol program


## Contributing

Contributing is encouraged, if you have an idea please feel free to fork this repository and I test out your improvements and add them.
**A new bugs.txt file has been created in the misc folder please submit any bugs there***


## Breif Showcase
These are some of the examples with correct highlighting from VSCODE 

### Two Sum
![Two Sum]()