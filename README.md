# Arithmetic-expressions-compiler
Interpret arithmetic expressions to English


## Description
Implemented 3 phases for the arithmetic expressions compiler:
- Lexical analysis
- Syntax analysis
- Intermediate code generation

The compiler is written in python using **[PLY, an implementation of lex and yacc parsing tools for Python](https://www.dabeaz.com/ply/ply.html)**.


**Interpretation is done based on below table:**

Eng | num |   | Eng |  num   |   | Eng | num
--- | --- | - | --- | -----  | - | --- | ---
Zer |  0  |   | Sev |    7   |   | Plu |  +
One |  1  |   | Eig |    8   |   | Min |  - 
Two |  2  |   | Nin |    9   |   | Mul |  * 
Thr |  3  |   | Ten |   10   |   | Div |  / 
Fou |  4  |   | Hun |  100   |   |     |   
Fiv |  5  |   | Tou | 1000   |   |     |   
Six |  6  |   |     |        |   |     |     


## Use
To run the program, you can install PLY usinf below command:
  ``` python
  pip install ply
  ```
or copy the ply folder next to *calculator.py* code and import its packages:
  ``` python
  import ply.lex as lex
  import ply.yacc as yacc
  ```
  
## Example
Example of output is:
``` bash
interpret >> 12850
Assign (OneTen_Two)Tou_EigHun_FivTen_Zer to t1
Print  t1
interpret >> (16*390)-8
Assign OneTen_Six Mul ThrHun_NinTen_Zer to t1
Assign t1 Min Eig to t2
Print  t2
```
