

def varBitTran(p_value, p_org_bitn, p_tar_bitn):
    if (p_org_bitn >= p_tar_bitn):
        # larger bit num to smaller bit num
        return p_value & (1 << (p_tar_bitn-1))
    else:
        # smaller bit num to larger bit num
        # firstly guarantee the org bit num valid
        return (p_value & (1 << (p_org_bitn-1))) & (1 << (p_tar_bitn-1))


def expADD(p_value1, p_bitn1, p_value2, P_bitn2):
    pass


def expSUB():
    pass


def expCalculation(r_tokens_lst, r_vars):
    # ending condition
    if (len(r_tokens_lst) == 1):
        str1 = r_tokens_lst[0]
        if (str1[0] == "v"):
            return r_vars[str1][0], r_vars[str1][1]
        else:
            return len(str1), int(str1, 2)
    # recursive condition
    else:
        pass


def doDeclare(r_tokens_lst, r_vars):
    var_type = r_tokens_lst[1]
    var_bitn = int(var_type[2:], 10)
    var_name = r_tokens_lst[2]
    r_vars[var_name] = (var_bitn, 0b0)


def doAssign(r_tokens_lst, r_vars):
    var_type = r_vars[var_name][0]
    var_bitn = int(var_type[2:], 10)
    var_name = r_tokens_lst[1]
    exp_bitn, exp_value = expCalculation(r_tokens_lst[2:], r_vars)
    r_vars[var_name] = (var_bitn, varBitTran(exp_value, exp_bitn, var_bitn))


def doBranch(r_tokens_lst, r_vars, p_pc):
    tar_line = int(r_tokens_lst[1], 10)
    exp_bitn, exp_value = expCalculation(r_tokens_lst[2:], r_vars)
    # guarantee overflow is omitted, using vsrBitTran
    if (varBitTran(exp_value, exp_bitn, exp_bitn) != 0b0):
        return tar_line - 1
    else:
        return p_pc


def doOutput(r_tokens_lst, r_vars, r_file_out):
    var_name = r_tokens_lst[1]
    _, var_value = r_vars[var_name]
    # variable is guaranteed to be varBitTran first
    print(bin(var_value)[2:], file=r_file_out)


def doDestory(r_tokens_lst, r_vars):
    var_name = r_tokens_lst[1]
    del r_vars[var_name]


if __name__ == "__main__":
    # read the pig file into lst pig_lines
    g_file_in = open("input.pig", "r")
    g_pig_lines = g_file_in.readlines()
    g_file_in.close()
    # prepare the out stream, vars and pc
    g_file_out = open("1.out", "w")
    g_vars = dict()
    g_pc = 0
    # start interpreting
    g_line = g_pig_lines[g_pc]
    while (g_line and not (g_line.isspace())):
        # detecting statement type
        gw_tokens_lst = g_line.split(" ")
        gw_statement_type = g_line[0]

        if (gw_statement_type == 'D'):
            doDeclare(gw_tokens_lst, g_vars)
        elif (gw_statement_type == 'A'):
            doAssign(gw_tokens_lst, g_vars)
        elif (gw_statement_type == 'B'):
            g_pc = doBranch(gw_tokens_lst, g_vars, g_pc)
        elif (gw_statement_type == 'O'):
            doOutput(gw_tokens_lst, g_vars, g_file_out)
        elif (gw_statement_type == 'R'):
            doDestory(gw_tokens_lst, g_vars)
        else:
            break
        g_pc += 1
        g_line = g_pig_lines[g_pc]
