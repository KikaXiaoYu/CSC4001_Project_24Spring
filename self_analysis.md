# CSC4001 Project Draft

## PIG Language

### Tokens

| token    | expression          | statement    | example               |
| -------- | ------------------- | ------------ | --------------------- |
| D        | D                   | `D TYPE VAR` | `D bv8 v001`          |
| A        | A                   | `A VAR Exp`  | `A v001 ( 00000101 )` |
| B        | B                   | `B LINE Exp` | `B 001 ( v000 )`      |
| O        | O                   | `O VAR`      | `O v001`              |
| R        | R                   | `R VAR`      | `R v001`              |
| ADD      | +                   |              |                       |
| SUB      | -                   |              |                       |
| AND      | &                   |              |                       |
| OR       | \|                  |              |                       |
| NOT      | !                   |              |                       |
| LINE     | $[0-9]^3$           |              |                       |
| CONSTANT | $[01]^{8|16|32|64}$ |              |                       |
| LP       | (                   |              |                       |
| RP       | )                   |              |                       |
| TYPE     | bv(8\|16\|32\|64)   |              |                       |
| VAR      | v$[0-9]^3$          |              |                       |

## Testing

### Differential Testing (50pts)

#### Overview

- Write a generator for the PIG language and a correct version of PIG-interpreter.
- For each buggy interpreter, repeat the testing process with 100 iterations.
  1. Run your generator "gen.py", which should save the program output to a file named "input.pig" under the same directory.
  2. Use "input.pig" as input and run your interpreter "pig.py", then save the output to a file named "1.out" under the same directory.
  3.  Use "input.pig" as input again, this time with the buggy PIG interpreter, and save the output to a file named "2.out" under the same directory.
  4. Compare "1.out" and "2.out". Any inconsistency between them will serve as a bug report for your testing.

> `gen.py` 生成文件 `input.pig`, `pig.py` 读取它并且生成 `1.out`, 同时使用 buggy PIG interpreter 生成 `2.out`, 最后比较 `1.out` 和 `2.out`. 
>
> - 比较的过程是否需要我们书写脚本或代码？bug report 我们是否需要书写？

#### Grading (40pts for code, 10 pts for report)

We have 8 buggy interpreters in total, where 3 of them are released (without source code) and the remaining are hidden. For each interpreter, the task has **5 pts** in total:

- Test case validity (**1 pts**): you will receive (number of successful testing iterations / 100) pts.

- Bug detection (**2 pts**): you will receive 2 pts if there is a TP bug report in the 100 testing iterations.

- No false alarms (**1 pts**): you will receive (number of successful testing iterations / 100) pt if there is no FP bug report in the 100 testing iterations and there is at least one TP bug report.

- No missing bugs (**1 pts**): you will receive (number of successful testing iterations / 100) pt if there is no FN bug report in the 100 testing iterations and there is at least one TP bug report.

> - TP: 错误解释器的结果跟我的和标准的都不同.
> - TN: 错误解释器的结果跟我的和标准的都相同.
> - FN: 错误解释器的结果跟我的相同, 但和标准的不同. (自己的有bug)
> - FP: 错误解释器的结果跟我的不相同, 但和标准的相同. (误杀)
>
> Test case validity: 指的应该是生成的代码正确，即没有出现任何报错或者超时.
>
> Bug detection: 只要在100次迭代中出现一次 bug 被找出的情况(TP), 即可.
>
> No false alarms: 100次迭代中均不出现 bug 找错了的情况(FP).
>
> No missing bugs: 100次迭代中均不出现 bug 没找出的情况.

#### Hints

- 可以把test case放到错误解释器里去看他们是否会报错.
- 可以测试一下在我自己的解释器上的 code coverage.

### Metamorphic Testing (bonus 20pts)

#### Overview

 In this part, we have 4 buggy interpreters. For each buggy interpreter, we’ll repeat the testing process with 100 iterations.

1. Run your generator "gen_meta.py", which should save two files named "input1.pig" and "input2.pig".

2. Use "input1.pig" as input and run the buggy PIG-interpreter, then save the output to a file named "1.out".
3. Use "input2.pig" as input and run the buggy PIG-interpreter, then save the output to a file named "2.out".
4. Run your checker, which should read "1.out" and "2.out" and then write a single integer in {0*,* 1} to the file "res.out", where 1 indicates the buggy-interpreter output at least one incorrect result for the two inputs.

> `gen_meta.py` 生成两个文件 `input1.pig` 和 `input2.pig`, 用错误解释器去分别运行这两个文件. 之后运行 `checker.py` 去读取 `1.out` 和 `2.out` 并且生成 `res.out` 去表示错误解释器至少运行了一个不正确的结果.
>
> - 问题来了, checker究竟是起到了什么作用呢?

#### Grading (16pts for coding and 4pts for report)

We have 4 buggy interpreters in total, where 1 of them is released (withhout source code) and the remaining are hidden. For each interpreter, the task has **4 pts** in total:

- Test case validity (**1 pts**): you will receive (number of successful testing iterations / 100) pts.
- Bug detection (**2 pts**): you will receive 2 pts if there is a TP bug report in the 100 testing iterations.
- No false alarms (**1 pts**): you will receive (number of successful testing iterations / 100) pt if there is no FP bug report in the 100 testing iterations there is at least one TP bug report.

> Test case validity: 正确不出错就能拿分.
>
> Bug detection: TP bug report, 即 错误解释器的某一个结果和你的以及标准解释器的都不同, 并且checker返回1. 
>
> No false alarms: 没有FP, 即两个结果均和标准代码生成的一致, 但 check返回1.

#### Hint

同等意义的代码用不同的方式去书写.

## Dataflow Analysis

### Use of Undefined Variable in PIG Code (50pts)

#### Overview

Your program should read a *PIG* code from standard input. The input is a string representing a *PIG* code. Each input code contains up to 1,000 lines with each line containing up to 1,000 characters. Besides, we guarantee the syntax correctness of the input code. However, there may exist systematic errors in the input code (i.e. redefining of existing variables or use of undefined variables). The output is simply an integer indicating the number of lines that may use undeclared variables. Your code should output this integer to the standard output.

#### Grading (40pts for coding and 10pts for reports)

We have 10 manually written or machine-generated *PIG* codes, where 7 of them are released and the remaining are hidden. The hidden test case may have a more complex structure and longer length compared with the released test cases. For each *PIG* code, the task has **4 pts**. We will use automatic tools to test your code. Note that, your Python code should avoid importing any third-party libraries, which may cause you to get **0 pts**. You will receive grades for each test case if your program outputs the correct result. You will not receive grades for a test case if your program:

- Crashes or raises an error
- Have no output or output an incorrect result
- Can not finish within 10 seconds
- Use more than 1GB of memory

#### Hints

- 把代码构建成 CFG
- 给输入和输出状态一个合适的定义，并且确定他们的关系
- 使用dataflow analysis的结果去计算输出