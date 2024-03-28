You can run the example codes as follows:

```bash
python3.9 gen.py
```

It will create two files named ```input1.pig``` and ```input2.pig```

You can use the following instruction to feed your inputs to the buggy interpreters:

```bash
./pig1 < input1.pig > 1.out
./pig1 < input2.pig > 2.out
```

Leveraging metamorphic testing, You should use your ```checker.py``` to examine the two outputs

```bash
python3.9 checker.py
```

It will read ```1.out``` and ```2.out```, and then give a integer 0 or 1 in the file ```res.out```.
