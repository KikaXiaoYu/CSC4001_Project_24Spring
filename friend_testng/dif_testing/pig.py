

def varBitTran(p_org_bit: int, p_tar_bit:
               int, p_value: int) -> int:
    '''
    Given original bit number and target bit number
    return the transferred value w.r.t. bit
    '''
    org_mask = (1 << (p_org_bit)) - 1
    tar_mask = (1 << (p_tar_bit)) - 1
    if (p_org_bit >= p_tar_bit):
        # larger bit num to smaller bit num, just mask
        return p_value & tar_mask
    else:
        # smaller bit num to larger bit num
        # firstly guarantee the org bit num valid using mask
        # then do mask
        return (p_value & org_mask) & tar_mask


def expADD(p_bit1: int, p_value1: int,
           p_bit2: int, p_value2: int) -> tuple:
    '''
    Given two values with bits
    return the ADD result bit and value
    '''
    max_bit = max(p_bit1, p_bit2)
    # varBitTran to guarantee bit
    return max_bit, varBitTran(max_bit, max_bit, (p_value1 + p_value2))


def expSUB(p_bit1: int, p_value1: int,
           p_bit2: int, p_value2: int) -> tuple:
    '''
    Given two values with bits
    return the SUB result bit and value
    '''
    max_bit = max(p_bit1, p_bit2)
    # varBitTran to guarantee bit
    return max_bit, varBitTran(max_bit, max_bit, (p_value1 - p_value2))


def expAND(p_bit1: int, p_value1: int,
           p_bit2: int, p_value2: int) -> tuple:
    '''
    Given two values with bits
    return the AND result bit and value
    '''
    max_bit = max(p_bit1, p_bit2)
    # no need to guarantee bit
    return max_bit, (p_value1 & p_value2)


def expOR(p_bit1: int, p_value1: int,
          p_bit2: int, p_value2: int) -> tuple:
    '''
    Given two values with bits
    return the OR result bit and value
    '''
    max_bit = max(p_bit1, p_bit2)
    # no need to guarantee bit
    return max_bit, (p_value1 | p_value2)


def expNOT(p_bit: int, p_value: int) -> tuple:
    '''
    Given two values with bits
    return the NOT result bit and value
    '''
    # varBitTran to guarantee bit
    return p_bit, varBitTran(p_bit, p_bit, ~p_value)


def expCalculation(r_tokens_lst: list, r_vars: dict) -> int:
    '''
    given tokens lst and variables
    return the result bit and value
    '''
    # this function should guarantee prior no overflow
    # ending condition (only LP VAL|CONS RP)
    if (len(r_tokens_lst) == 3):
        str1 = r_tokens_lst[1]
        if (str1[0] == "v"):  # variable condition
            if (str1 not in r_vars):
                print(f"Line {g_pc}: variable {str1} has not been declared.")
                raise (SystemExit)
            return r_vars[str1][0], r_vars[str1][1]
        else:  # constant condition
            return len(str1), int(str1, 2)
    # recursive condition (containing EXP)
    elif (r_tokens_lst[1] == "!"):  # not condition
        exp_bit, exp_value = expCalculation(r_tokens_lst[2:-1], r_vars)
        return expNOT(exp_bit, exp_value)
    else:  # exp bop exp condition
        bracket_balance = 0
        cur_idx = 1
        # catch the Bop index into cur_idx
        while (True):
            if (r_tokens_lst[cur_idx] == "("):
                bracket_balance += 1
            elif (r_tokens_lst[cur_idx] == ")"):
                bracket_balance -= 1
            cur_idx += 1
            if (bracket_balance == 0):
                break
        # catch bop and two expressions
        bop_str = r_tokens_lst[cur_idx]
        exp_bit1, exp_value1 = expCalculation(
            r_tokens_lst[1:cur_idx], r_vars)
        exp_bit2, exp_value2 = expCalculation(
            r_tokens_lst[cur_idx+1:-1], r_vars)
        # do exp bop calculation
        if (bop_str == "+"):
            return expADD(exp_bit1, exp_value1, exp_bit2, exp_value2)
        elif (bop_str == "-"):
            return expSUB(exp_bit1, exp_value1, exp_bit2, exp_value2)
        elif (bop_str == "&"):
            return expAND(exp_bit1, exp_value1, exp_bit2, exp_value2)
        elif (bop_str == "|"):
            return expOR(exp_bit1, exp_value1, exp_bit2, exp_value2)
        else:
            print(f"Line {g_pc}: invalid statement.")
            raise (SystemExit)


def doDeclare(r_tokens_lst: list, r_vars: dict) -> None:
    '''
    declare a var with bit saved to r_vars
    '''
    var_type = r_tokens_lst[1]
    var_bit = int(var_type[2:], 10)
    var_name = r_tokens_lst[2]
    if (var_name in r_vars):
        print(f"Line {g_pc}: variable {var_name} has been redeclared.")
        raise (SystemExit)
    r_vars[var_name] = (var_bit, 0b0)


def doAssign(r_tokens_lst: list, r_vars: dict) -> None:
    '''
    assign a var with bit and values, saved in r_vars
    '''
    var_name = r_tokens_lst[1]
    if (var_name not in r_vars):
        print(f"Line {g_pc}: variable {var_name} has not been declared.")
        raise (SystemExit)
    var_bit = r_vars[var_name][0]
    exp_bit, exp_value = expCalculation(r_tokens_lst[2:], r_vars)
    r_vars[var_name] = (var_bit, varBitTran(exp_bit, var_bit, exp_value))


def doBranch(r_tokens_lst: list, r_vars: dict, p_pc: int, p_pig_size) -> int:
    '''
    branch with exp and return the pc (prev, then should be add by 1)
    '''
    tar_line = int(r_tokens_lst[1], 10)
    if (tar_line >= p_pig_size):
        print(f"Line {g_pc}: branching line {tar_line} is output of bound.")
        raise (SystemExit)
    _, exp_value = expCalculation(r_tokens_lst[2:], r_vars)
    if (exp_value != 0b0):
        return tar_line - 1
    else:
        return p_pc


def doOutput(r_tokens_lst: list, r_vars: dict, r_file_out) -> None:
    '''
    output variable to r_file_out
    '''
    var_name = r_tokens_lst[1]
    if (var_name not in r_vars):
        print(f"Line {g_pc}: variable {var_name} has not been declared.")
        raise (SystemExit)
    var_bit, var_value = r_vars[var_name]
    # variable is guaranteed to be varBitTran first
    print(f"{var_value:0{var_bit}b}", file=r_file_out)


def doDestory(r_tokens_lst: list, r_vars: dict) -> None:
    '''
    destory a variable, removed from r_vars
    '''
    var_name = r_tokens_lst[1]
    if (var_name not in r_vars):
        print(f"Line {g_pc}: variable {var_name} has not been declared.")
        raise (SystemExit)
    del r_vars[var_name]


if __name__ == "__main__":
    try:
        # read the pig file into lst pig_lines
        g_file_in = open("input.pig", "r")
        g_pig_lines = g_file_in.readlines()
        g_pig_size = len(g_pig_lines)
        g_file_in.close()
        # prepare the out stream, vars and pc
        g_file_out = open("1.out", "w")
        g_vars = dict()
        g_pc = 0
        g_output_count = 0
        g_statement_count = 0
        # start interpreting
        if (g_pc < g_pig_size):
            g_line = g_pig_lines[g_pc]
        while (g_line and not (g_line.isspace())):
            g_statement_count += 1
            if (g_statement_count == 5001):
                print("too-many-lines", file=g_file_out)
                raise (SystemExit)
            # detecting statement type
            gw_tokens_lst = g_line.strip().split(" ")
            gw_statement_type = gw_tokens_lst[0]
            if (gw_statement_type == 'D'):
                doDeclare(gw_tokens_lst, g_vars)
            elif (gw_statement_type == 'A'):
                doAssign(gw_tokens_lst, g_vars)
            elif (gw_statement_type == 'B'):
                g_pc = doBranch(gw_tokens_lst, g_vars, g_pc, g_pig_size)
            elif (gw_statement_type == 'O'):
                doOutput(gw_tokens_lst, g_vars, g_file_out)
            elif (gw_statement_type == 'R'):
                doDestory(gw_tokens_lst, g_vars)
            else:
                raise (SystemExit)
            g_pc += 1
            if (g_pc < g_pig_size):
                g_line = g_pig_lines[g_pc]
            else:
                raise (SystemExit)
    except:
        # print(f"Invalid Input")
        raise (SystemExit)
