def bitwise_not_and_convert(binary_string):
    """
    This function inverts each bit in a binary string, converts the result to an integer,
    and then converts it back to a binary string while preserving the original length.
    """
    inverted_string = ''.join('1' if char == '0' else '0' for char in binary_string)

    inverted_number = int(inverted_string, 2)

    formatted_binary = format(inverted_number, f'0{len(binary_string)}b')
    return formatted_binary

def tran_to_bin(var):
    return(bin(var)[2:])

def manual_startswith(main_string, prefix):
    """
    Manually checks if main_string starts with the prefix.
    
    :param main_string: The string to be checked.
    :param prefix: The prefix to look for in the main_string.
    :return: True if main_string starts with prefix, False otherwise.
    """
    if len(prefix) > len(main_string):
        return False  # 如果前缀比主字符串还长，直接返回False

    # 检查主字符串的开始部分是否与前缀相匹配
    for i in range(len(prefix)):
        if main_string[i] != prefix[i]:
            return False  # 一旦发现不匹配，返回False

    return True  # 如果所有对应的字符都匹配，返回True

def replace_substr(main_str, replacement_str, begin, end):
    return main_str[:begin] + replacement_str + main_str[end + 1:]

def remove_spaces(s):
    return s.replace(" ", "")

def string_to_list(input_string):
    return [char for char in input_string]

def list_to_string(lst):
    return ''.join(lst)

def analyze_parentheses(expression):
    stack = []
    paren_pairs = []
    
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                raise ValueError("Invalid expression: mismatched parentheses")
            start_index = stack.pop()
            end_index = i
            paren_pairs.append((start_index, end_index))
    
    if stack:
        raise ValueError("Invalid expression: mismatched parentheses")
    
    return paren_pairs

def subtract_unsigned(a, b, bit_width):
    max_val = (1 << bit_width) - 1

    if a < b:
        overflow = (1 << bit_width)
        result = (overflow + a) - b
    elif a == b:
        result = 0
    else:
        result = a - b
    return result & max_val

def process_var_type(string):
    if string == "bv8":
        return 8
    elif string == "bv16":
        return 16
    elif string == "bv32":
        return 32
    elif string == "bv64":
        return 64
    else:
        return 0
    
undeclared_number = 0
undeclared = 1
undeclared_lines = 0
undeclared_lines_isnot = 1
pc_list = []
def evaluate_expression(expression, vars, varname):
    global undeclared_number, undeclared
    parentheses_list = analyze_parentheses(expression)
    tokens = expression.split()
    result = 0
    if varname != '':
        bit_width = int(vars[varname]['bit_width'])
    else:
        bit_width = 64
    bit_mask = (1 << bit_width) - 1

    for i in range(10000):
        if analyze_parentheses(expression) == []:
            result = sub_result
            break
        else:
            start, end = analyze_parentheses(expression)[0]
            sub_expr = expression[start + 1 : end]
            sub_result, token_len = evaluate_sub_expression(sub_expr, vars, '')
            if len(bin(sub_result)[2:].zfill(token_len)) >= 35:
                expression = replace_substr(expression, bin(sub_result)[2:].zfill(64), start , end)
            else:
                expression = replace_substr(expression, bin(sub_result)[2:].zfill(token_len), start , end)
            parentheses_list = analyze_parentheses(expression)
    if len(bin(result)[2:])>= 50:
        return bin(result)[2:].zfill(64)
    else:
        return bin(result)[2:].zfill(bit_width)



def evaluate_sub_expression(sub_expr, vars, varname):
    global undeclared_number, undeclared
    tokens = sub_expr.split()
    token_len = 0
    result = 0
    last_op = None
    token_len_for_cal = 0
    current_value = 0
    bit_width = int(vars[varname]['bit_width']) if varname != '' else 64
    for token in tokens:
        if manual_startswith(token, 'v') and token not in vars :
            undeclared_number += 1
            undeclared = 0
        i=1
        if  token_len_for_cal<= len(token):
            token_len_for_cal = len(token)
        i+=1
    if len(tokens) == 1 and  all(c in '01' for c in tokens[0]):
        current_value = int(token, 2)
        token_len = len(tokens[0])
        result = current_value
        return result, token_len
    
    if len(tokens) == 1 and tokens[0] in list(vars.keys()):
        token_len = vars[tokens[0]]['bit_width']
        result = vars[tokens[0]]['value']
        result = int(result,2)
        return result, token_len

    for token in tokens:
        if  all(c in '01' for c in token):  # Check if it is a binary number
            current_value = int(token, 2)
            len_ = len(token)
            if token_len < len_:
                token_len = len_
        elif token in vars:
            current_value = int(vars[token]['value'], 2)
        elif token in ['+', '-', '&', '|']:
            last_op = token
            continue
        elif token == '!':
            value = tokens[-1]
            if token in vars:
                number = bitwise_not_and_convert(vars[value]['value'])
                token_len = len(number)
                result = int(number,2)
            else:
                number = bitwise_not_and_convert(value)
                token_len = len(number)
                result = int(number,2)
            if last_op is not None:
                raise ValueError("Syntax Error: '!' should not follow another operator directly")
            break  
        if last_op:
            if last_op == '+':
                result = (result + current_value)   # Ensure the result fits within the bit width
            elif last_op == '-':
                result = subtract_unsigned(result, current_value, bit_width)
                result = bin(result)[2:].zfill(bit_width)[-token_len_for_cal:]
                result = int(result,2)
            elif last_op == '&':
                result &= current_value
            elif last_op == '|':
                result |= current_value
            last_op = None
        else:
            result = current_value
    return result, token_len

def tran_to_bin(var, width):
    return bin(var)[2:].zfill(width)

def subtract_unsigned(a, b, bit_width):
    max_val = (1 << bit_width) - 1
    result = (a - b) & max_val  # Perform the subtraction and ensure it fits within the bit width
    return result


def process_line(line, vars, output, pc):
    global undeclared_number, undeclared, undeclared_lines, undeclared_lines_isnot, pc_list
    parts = line.strip().split()
    if not parts:
        return pc + 1  # 忽略空行
    for part in parts:
        if manual_startswith(part, 'v') and part not in vars and parts[0] != 'D':
            undeclared_lines_isnot = 0
    
    if undeclared_lines_isnot == 0:
        undeclared_lines += 1
        pc_list.append(pc)
    cmd = parts[0]

    undeclared_lines_isnot = 1
    if cmd == 'D':
        _, var_type, var_name = parts
        vars[var_name] = {
            'value': '0' * int(var_type[2:]),
            'bit_width': process_var_type(var_type)
        }
    elif cmd == 'A':
        var_name = parts[1]
        if var_name not in vars:
            undeclared_number += 1
            undeclared = 0
            return pc + 1  # 返回-1或其他标记以停止程序
        expr = ' '.join(parts[2:])
        new_value = evaluate_expression(expr, vars, var_name)
        vars[var_name]['value'] = new_value
    elif cmd == 'O':
        var_name = parts[1]
        if var_name not in vars:
            undeclared_number += 1
            undeclared = 0
            return pc + 1
        output.append(vars.get(var_name, {'value': '0'})['value'])
        # with open("1.out", "a") as out_file:
        #     out_file.write(vars.get(var_name, {'value': '0'})['value'] + "\n")
    elif cmd == 'R':
        var_name = parts[1]
        if var_name not in vars:
            undeclared_number += 1
            undeclared = 0
            return pc + 1
        del vars[var_name]
    elif cmd == 'B':
        var_name = parts[1]
        if var_name not in vars:
            undeclared_number += 1
            undeclared = 0
            return pc + 1
        return pc + 1
    return pc + 1


if __name__ == "__main__":
    vars = {}
    output = []
    lines = []
    pc = 0  
    
    with open("./input.pig", "r") as f:
        lines = f.readlines()

    while pc < len(lines):
        if pc >= 5000:
            break
        pc = process_line(lines[pc], vars, output, pc)

    if undeclared == 0:
        print(f'{undeclared_lines}', end='')
