def bitwise_not_and_convert(binary_string):
    """
    This function inverts each bit in a binary string, converts the result to an integer,
    and then converts it back to a binary string while preserving the original length.
    """
    # Invert each character: '0' becomes '1', and '1' becomes '0'
    inverted_string = ''.join('1' if char == '0' else '0' for char in binary_string)

    # Convert the inverted binary string to an integer
    inverted_number = int(inverted_string, 2)

    # Convert back to binary string, preserving the original length and including leading zeros
    formatted_binary = format(inverted_number, f'0{len(binary_string)}b')
    return formatted_binary

def tran_to_bin(var):
    return(bin(var)[2:])

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
    

def evaluate_expression(expression, vars, varname):
    parentheses_list = analyze_parentheses(expression)
    # print(f'parentheses_list {parentheses_list}')
    tokens = expression.split()
    result = 0
    if varname != '':
        bit_width = int(vars[varname]['bit_width'])
    else:
        bit_width = 64
    bit_mask = (1 << bit_width) - 1

    
    # 处理括号列表中的每对括号
    # print(tokens)
    for i in range(10000):
        if analyze_parentheses(expression) == []:
            result = sub_result
            # print(f'result 确定了：{bin(result)[2:]}')
            break
        else:
            # print(f'expression:{expression}')
            start, end = analyze_parentheses(expression)[0]
            # print(f'start: {start}, end:{end}')
            sub_expr = expression[start + 1 : end]
            # print(f'sub_expr:{sub_expr}')
            sub_result, token_len = evaluate_sub_expression(sub_expr, vars, '')
            # print(f'token_len 用于补充的是：{token_len}')
            # print('东西是：', replace_substr(expression, str(tran_to_bin(sub_result)), start, end))
            if len(bin(sub_result)[2:].zfill(token_len)) >= 35:
                expression = replace_substr(expression, bin(sub_result)[2:].zfill(64), start , end)
                # print(f'被替换的内容是(补充到64位了):{bin(sub_result)[2:].zfill(64)} bit_width : {bit_width}, len:{len(bin(sub_result)[2:].zfill(64))}')
            else:
                expression = replace_substr(expression, bin(sub_result)[2:].zfill(token_len), start , end)
                # print(f'被替换的内容是：{bin(sub_result)[2:].zfill(token_len)} bit_width : {bit_width}, len:{len(bin(sub_result)[2:].zfill(token_len))}')
            # expression = replace_substr(expression, bin(sub_result)[2:].zfill(bit_width), start , end)
            parentheses_list = analyze_parentheses(expression)
            # print(f'new parenthese_list : {parentheses_list}')
            # print(f'new_expression:{expression}')
            # print(string_to_list(expression)[start:end + 1])
    # print(f'这个一个表达式的bit_width是:{bit_width}')
    if len(bin(result)[2:])>= 50:
        return bin(result)[2:].zfill(64)
    else:
        return bin(result)[2:].zfill(bit_width)



def evaluate_sub_expression(sub_expr, vars, varname):
    # print(sub_expr)
    tokens = sub_expr.split()
    # print(f'子处理的token:{tokens}')
    token_len = 0
    result = 0
    last_op = None
    token_len_for_cal = 0
    current_value = 0
    bit_width = int(vars[varname]['bit_width']) if varname != '' else 64
    for token in tokens:
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
            # print(f'value:{value}')
            if token in vars:
                number = bitwise_not_and_convert(vars[value]['value'])
                token_len = len(number)
                result = int(number,2)
                # print(f'result:{len(bin(result)[2:].zfill(token_len))}')
            else:
                number = bitwise_not_and_convert(value)
                token_len = len(number)
                result = int(number,2)
                # print(f'result:{len(bin(result)[2:].zfill(token_len))}')
            if last_op is not None:
                raise ValueError("Syntax Error: '!' should not follow another operator directly")
            # print(result)
            # print(f'value:{value}')
            # print(type(result))
            break  
        if last_op:
            if last_op == '+':
                result = (result + current_value)   # Ensure the result fits within the bit width
            elif last_op == '-':
                result = subtract_unsigned(result, current_value, bit_width)
                result = bin(result)[2:].zfill(bit_width)[-token_len_for_cal:]
                result = int(result,2)
            elif last_op == '&':
                # print(f'result:{result}')
                # print(f'current_value:{current_value}')
                result &= current_value
            elif last_op == '|':
                result |= current_value
            last_op = None
        else:
            result = current_value
    # print(f'result:{bin(result)[2:]}')
    # print(type(result))
    # print(f'这一次运算的result是:{bin(result)[2:]} len:{len(bin(result)[2:])}')
    # print(f'传递过去的result是:{result}')
    return result, token_len

def tran_to_bin(var, width):
    return bin(var)[2:].zfill(width)

def subtract_unsigned(a, b, bit_width):
    max_val = (1 << bit_width) - 1
    result = (a - b) & max_val  # Perform the subtraction and ensure it fits within the bit width
    return result

output_content = ''
def process_line(line, vars, output, pc):
    global output_content
    parts = line.strip().split()
    # print (f'parts {parts}')
    if not parts:
        return pc + 1  

    cmd = parts[0]

    if cmd == 'D':
        _, var_type, var_name = parts
        vars[var_name] = {
            'value': '0' * int(var_type[2:]),
            'bit_width': process_var_type(var_type)
        }
    elif cmd == 'A':
        var_name = parts[1]
        expr = ' '.join(parts[2:])
        # new_value = evaluate_expression(expr, vars, var_name)
        # print(f'即将导入进去的内容是：{new_value}')
        # print(f'导入的位置是：{vars[var_name]}')
        vars[var_name]['value'] = evaluate_expression(expr, vars, var_name)[-int(vars[var_name]['bit_width']):]
    elif cmd == 'O':
        var_name = parts[1]
        output_content += vars.get(var_name, {'value': '0'})['value'] + "\n"
    elif cmd == 'R':
        var_name = parts[1]
        if var_name in vars:
            vars[var_name]['value'] = ('0' * vars[var_name]['bit_width'])
    elif cmd == 'B':
        line_target = int(parts[1])
        # print(f'尝试执行B, 表达式位: {' '.join(parts[2:])}')
        condition = evaluate_expression(' '.join(parts[2:]), vars, '')
        if int(condition, 2) != 0:
            return line_target
    return pc + 1


if __name__ == "__main__":
    vars = {}
    output = []
    lines = []
    pc = 0  
    processed_lines = 0
    with open("./input.pig", "r") as f:
        lines = f.readlines()

    while pc < len(lines):
        processed_lines += 1
        if processed_lines > 5000:
            with open("1.out", "a") as out_file:
                output_content += "too-many-lines\n"
            # print("too-many-lines")
            break
        # print(f'current_pc = {pc}')
        # print(f'vars = {vars}')
        # print(f'----------------------------------------------')
        pc = process_line(lines[pc], vars, output, pc)
        # print(f'next_pc = {pc}')
    # print(vars)

    with open("1.out", "w") as out_file:
        out_file.write(output_content)
