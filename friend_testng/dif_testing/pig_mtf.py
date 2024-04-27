varDict = {}
Program_counter = 0

def binary_string(value, bits):
    return format(value & ((1 << bits) - 1), f'0{bits}b')

def add(x, y):
    # 位数对齐，取最大位数
    max_bits = max(x[0], y[0])
    result = (x[1] + y[1]) & ((1 << max_bits) - 1)
    return [max_bits, result]

def sub(x, y):
    # 位数对齐，取最大位数
    max_bits = max(x[0], y[0])
    result = (x[1] - y[1]) & ((1 << max_bits) - 1)
    return [max_bits, result]

def and_op(x, y):
    # 位数对齐，取最大位数
    max_bits = max(x[0], y[0])
    result = (x[1] & y[1]) & ((1 << max_bits) - 1)
    return [max_bits, result]

def or_op(x, y):
    # 位数对齐，取最大位数
    max_bits = max(x[0], y[0])
    result = (x[1] | y[1]) & ((1 << max_bits) - 1)
    return [max_bits, result]

def not_op(x):
    # 对每一位取反
    result = (~x[1]) & ((1 << x[0]) - 1)
    return [x[0], result]


def evaluate_expression(expression):
    expression = expression.strip()
    # Base case: simple constant or variable within parentheses
    if expression.startswith('(') and expression.endswith(')'):
        inner_exp = expression[1:-1].strip()
        
        # Check if it's a plain number (constant)
        if inner_exp.isdigit():
            return [len(inner_exp), int(inner_exp, 2)]

        # Check if it's a variable
        if inner_exp in varDict:
            return varDict[inner_exp]

        # Recursive case: NOT expression
        if inner_exp.startswith('!'):
            innerExp = evaluate_expression(inner_exp[1:])
            return [innerExp[0], (~innerExp[1]) & ((1 << innerExp[0]) - 1)] 
        
        parenthesis_stack = []
        for i, char in enumerate(inner_exp):
            if char == '(':
                parenthesis_stack.append(char)
            elif char == ')':
                parenthesis_stack.pop()
            elif not parenthesis_stack:
                if char in ['&','|','+','-']:
                    left = inner_exp[:i].strip()
                    right = inner_exp[i+1:].strip()
                    op = char
                    left_value = evaluate_expression(left)
                    right_value = evaluate_expression(right)
                    if op == '&':
                        return and_op(left_value, right_value)
                    elif op == '|':
                        return or_op(left_value, right_value)
                    elif op == '+':
                        return add(left_value, right_value)
                    elif op == '-':
                        return sub(left_value, right_value)
    raise ValueError("Invalid expression format or unknown variable")


def execute_line(line):
    global Program_counter
    parts = line.strip().split()
    if parts == []:
        return
    command = parts[0]
    if command == 'D':
        _, type_str, var_name = parts
        bit_size = int(type_str[2:])
        if var_name in varDict:
            raise Exception("Variable already defined")
        varDict[var_name] = [bit_size, 0]  # 默认值为0
    
    elif command == 'A':
        var_name = parts[1]
        expression = line[line.find('('):]
        if var_name not in varDict:
            raise Exception("Variable not defined")
        assignedValue = evaluate_expression(expression)
        originalType = varDict[var_name][0]
        varDict[var_name][1] = assignedValue[1]  & ((1 << originalType) - 1)
        
    
    elif command == 'B':
        target_line = int(parts[1])
        expression = line[line.find('(') :]
        if evaluate_expression(expression)[1] != 0:
            Program_counter = target_line - 1  # -1 因为for循环会增加
    
    elif command == 'R':
        var_name = parts[1]
        if var_name not in varDict:
            raise Exception("Variable not defined")
        del varDict[var_name]
    
    elif command == 'O':
        var_name = parts[1]
        if var_name not in varDict:
            raise Exception("Variable not defined")
        with open("./1.out", "a") as f:
            f.write(f"{binary_string(varDict[var_name][1], varDict[var_name][0])}\n")

    else:
        raise Exception("Unknown command")



if __name__ == "__main__":
    executedStatements = 0
    with open("./input.pig", "r") as f:
        lines = f.readlines()
    line_num = len(lines)

    with open("1.out","w") as file:
            pass

    try:
        while (Program_counter < line_num):
            if executedStatements >= 5000:
                with open("./1.out","a") as g:
                    g.write("too-many-lines\n")
                break
            
            execute_line(lines[Program_counter])
            executedStatements += 1
            Program_counter += 1 # brach should be target -1

    except Exception as e:
        print("Error:", str(e))

