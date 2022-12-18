# Nowata

My first Lisp like programming language

## Installation

* clone the repo
* cd into root directory of repo
* run `pip install .`
* now you have nowata installed and you can run files with `nowata your-file.nv`

## Syntax

A nowata program consits of expressions

### Expression

`(SYMBOL ARGS...)`

AN expression is enclosed in braces, where `SYMBOL` is either a keyword or function name and `ARGS...` are any number of expressions or Atoms

#### Example

`(print (str Hello World!))`

### If Else Conditionals

`(if TEST ON_TRUE ON_FALSE)`

#### Example

`(if (== 1 1) (print (str one is equal to one)) (oops))`

### Variable assignment

`(var NAME VALUE)`

#### Example

`(var my-number 128)`

### Output

`(print WHAT)`

#### Example

`(print (str Hello))`

### Input

`(input)` - returns string value

#### Example

`(var user-name (input))`

### User Defined Functions

`(func NAME EXPRESSIONS...)`

#### Example

`(func print-hello (print (str Hello There!)))`