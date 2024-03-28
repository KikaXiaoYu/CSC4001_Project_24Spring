You can run the example codes as follows:

```bash
python3.9 gen.py
python3.9 pig.py
```

It will create two files named ```input.pig``` and ```1.out```

You can use the following instruction to feed your input to the buggy interpreters and compare the results:

```bash
./pig1 < input.pig > 2.out
diff 1.out 2.out -b
```

