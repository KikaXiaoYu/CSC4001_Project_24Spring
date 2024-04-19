# CSC4001 Project Report

> **Author:** Ziyu XIE (谢子钰)	**Student ID:** 121090642	

## Differential Testing

### Differential Testing Overview

Differential testing is a **black-box technique** that works well when **systems implement the same behavior**.

The Project requires us to use differential testing to detect bugs of some buggy interpreters. If we give the same input (`input.pig`) into the interpreters, and the interpreters are of no bugs, then the outputs of all the interpreters should be the same. Then, since there are some bugs in the given interpreters, we can use our own correct interpreter (`pig.py`) to detect the bugs. If the buggy interpreters have the different output with our interpreter's result, we conclude that this interpreter contains bug.

In this testing, we need to firstly use `gen.py` to randomly generate non-empty PIG program, and we need to guarantee that this PIG program has no bug. Then we use `pig.py` to give the correct result `1.out` and use the buggy interpreter to give the result `2.out`, and finally we compare them to detect bug. This will go 100 times for one buggy interpreter.

Then, the problem is converted to how to implement `gen.py` and `pig.py`.

### Implementing Generator

In order to generate a correct PIG code, I raise up an idea called **"Snowflake Block Generation Method"**. We let one basic block generate multiple blocks, and then let these blocks continue to generate more blocks, spreading like snowflakes until our maximum file length requirement (1000) is met.

Since the PIG language contains five kinds of statement "D", "A", "B", "O", "R", we can define five kinds of basic blocks (not exactly corresponding to statements but five basic functions), called "BASIC Block", "ASSIGN Block", "OUTPUT Block", "IF Block", and "FOR Block".

#### BASIC BLOCK Structure

The BASIC Block is structured as below:

```python
BASIC_BLOCK (
    ''' declare many variables '''
    D TYPE VARx1
    # ... multiple lines
    D TYPE VARxn
    
    for _ in range(iter_num):
    	# randomly choose one block to generate:
    	( BASIC_BLOCK or 
         	IF_BLOCK or 
         	FOR_BLOCK or 
         	ASSIGN_BLOCK or 
         	OUTPUT_BLOCK
        )
	''' destroy these variables '''
    R TYPE VARx1
    # ... multiple lines
    D TYPE VARxn
)
```

The BASIC Block will know (passed by parameters):

1. how many lines have been generated (should not exceed maximum number),
2. which variables have been declared (should not redeclare), 
3. which variables should not be used here (because some other blocks may not want some variables to be modified, e.g. FOR Block),
4. the iteration number of this function has been used (to guarantee that it can be stopped and will not reach to the maximum recursion times of Python).

If all the steps inside the BASIC Block are correct, then this block is guaranteed to not redeclare or undeclare variables before usage.

#### OUTPUT BLOCK Structure

The OUTPUT Block is structured as below:

```python
OUTPUT_BLOCK (
    ''' output many variables '''
    O VARx1
    # ... multiple lines
    O VARxn
)
```

The OUTPUT Block will know (passed by parameters):

1. how many lines have been generated,
2. which variables have been declared.

#### ASSIGN BLOCK Structure

The ASSIGN Block is structured as below:

```python
ASSIGN_BLOCK (
    ''' assign many variables '''
    A VARx1 Exp
    # ... multiple lines
    A VARxn Exp
)
```

The ASSIGN Block will know (passed by parameters):

1. how many lines have been generated,
2. which variables have been declared,
3. which variables should not be used here.

#### IF BLOCK Structure

The IF Block is structured as below:

```python
IF_BLOCK (
    ''' creating conditonal variablen '''
    D TYPE VAR1
    A VAR1 Exp
    B tar_line VAR1
    ''' generate BASIC block inside the IF block '''
    BASIC_BLOCK
    ''' destroy conditional variable '''
    R VAR1
)
```

The IF Block will know (passed by parameters):

1. how many lines have been generated,
2. which variables have been declared,
3. which variables should not be used here.

#### FOR BLOCK Structure

The FOR Block is structured as below:

```python
IF_BLOCK (
    ''' creating iteration variable '''
    D TYPE VAR1
    A VAR1 Exp
    ''' generate BASIC block inside the FOR block '''
    BASIC_BLOCK
    ''' next iteration '''
    A VAR1 ( VAR - 1 )
    B tar_line VAR1
    ''' destroy conditional variable '''
    R VAR1
)
```

The IF Block will know (passed by parameters):

1. how many lines have been generated,
2. which variables have been declared,
3. which variables should not be used here.

#### Expression Structure

Similar to the blocks, the expression can also be generated using recursion. The concept of this part is omitted here because it is simple and in fact it is just the inverse process of the calculating the expression values in the `pig.py`, which we will talk about later. (In my project, I firstly did the `pig.py`, and then did the `gen.py`)

#### Conclusion

Based on all the structures below, we just need to set some hyper-parameter such as max_line_num, max_iteration_num, block_iter_num, etc. Finally the `gen.py` can work properly. 

### Implementing Interpreter

Since the PIG language contains five kinds of statement "D", "A", "B", "O", "R", we need to firstly judge the statement type, then do interpreting. For "D" and "R", we simply use a dictionary in Python to store all the variables declared and destroyed. For "O", we just output the value of the variable based on corresponding variable types.

Then the remain things is to do "A" and "B" statement. For "A" statement, we need to give the variable the corresponding expression values, and for "B" statement, we need to decide whether to branch based on the expression given (branching is just changing the global pc value). Therefore, if we implement how to calculate the expression correctly, we can easily finish the interpreter.

#### Calculate Expression

Based on the given listing forms of the Exp:

```python
Exp -> LP CONSTANT RP
	-> LP VAR RP
	-> LP Exp Bop Exp RP
	-> LP NOT Exp RP
```

We conclude that the expression is calculated in a recursive way, and the stopping criterion is encountering "CONSTANT" or "VAR".

In order to simplify our explanation, we simply say "CONSTANT" and "VAR" types have 3 tokens, "Bop" type has >= 5 tokens, and "NOT" type has >= 4 tokens.

Firstly, we judge whether the tokens number is equal to 3. If yes, then it must be a CONSTANT or VAR, this judgement is easy, and we return the value based on CONSTANT value or VAR value.

Secondly, 



## 

