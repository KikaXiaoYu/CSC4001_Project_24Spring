
import random

g_var_types = ("bv8", "bv16", "bv32", "bv64")
g_max_iter = 4


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


def varTypeToBit(p_var_type) -> int:
    return int(p_var_type[2:], 10)


def varNumToName(p_var_num) -> str:
    return f"v{p_var_num:03d}"


def bitValueToStr(p_bit, p_value) -> str:
    res_str = f"{p_value:0{p_bit}b}"[-p_bit:]
    return res_str


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
            raise (SystemExit)


def genExpression(p_value_range: tuple, p_type_range: tuple,
                  p_decis_range: tuple, r_var_dec_set: set, p_rec_iter: int):
    '''
    get expression ramdomly recursively, based on 3 ranges
    p_value_range: from 0 to 2**64-1
    p_type_range: from 0 to 3 (8, 16, 32, 64)
    p_decis_range: from 0 to 3 (cons, var, bop, not)
    '''

    if (p_rec_iter > g_max_iter or len(r_var_dec_set) == 0):
        # max iter, return only a constant
        # no var, can only be constant
        decis_dir = random.randint(0, 0)
    else:  # all decisions
        decis_dir = random.randint(p_decis_range[0], p_decis_range[1])

    value_str = ""

    if (decis_dir == 0):  # constant
        const_value = random.randint(p_value_range[0], p_value_range[1])
        const_bit = 2**random.randint(p_type_range[0], p_type_range[1]) * 8
        value_str = bitValueToStr(const_bit, const_value)
    elif (decis_dir == 1):  # variable
        var_name = random.sample(list(r_var_dec_set), 1)[0]
        value_str = var_name
    elif (decis_dir == 2):  # Bop
        bop_exp = random.sample(["+", "-", "&", "|"], 1)[0]
        exp_1 = genExpression(p_value_range, p_type_range,
                              p_decis_range, r_var_dec_set, p_rec_iter+1)
        exp_2 = genExpression(p_value_range, p_type_range,
                              p_decis_range, r_var_dec_set, p_rec_iter+1)
        value_str = f"{exp_1} {bop_exp} {exp_2}"
    elif (decis_dir == 3):  # NOT
        exp_1 = genExpression(p_value_range, p_type_range,
                              p_decis_range, r_var_dec_set, p_rec_iter+1)
        value_str = f"! {exp_1}"

    return (f"( {value_str} )")


def checkDsRs(r_res_lst_1: list, r_res_lst_2: list) -> None:
    var_count = 10
    var_num_lst_1 = random.sample(range(0, 1000), var_count)
    var_num_lst_2 = random.sample(range(0, 1000), var_count)
    var_name_lst_1 = [varNumToName(var_num_lst_1[i]) for i in range(var_count)]
    var_name_lst_2 = [varNumToName(var_num_lst_2[i]) for i in range(var_count)]
    var_type_lst = random.choices(g_var_types, k=var_count)
    var_bit_lst = [varTypeToBit(var_type_lst[i]) for i in range(var_count)]

    for _ in range(2):
        for i in range(var_count):
            r_res_lst_1.append(f"D {var_type_lst[i]} {var_name_lst_1[i]}")
            r_res_lst_2.append(f"D {var_type_lst[i]} {var_name_lst_2[i]}")

        for i in range(var_count):
            r_res_lst_1.append(f"O {var_name_lst_1[i]}")
            r_res_lst_2.append(f"O {var_name_lst_2[i]}")

        # type and value to be assigned to variables
        assign_type_lst = random.choices(g_var_types, k=var_count)
        assign_bit_lst = [varTypeToBit(assign_type_lst[i])
                          for i in range(var_count)]
        assign_value_lst = [varBitTran(64, assign_bit_lst[i], random.randint(
            0, 2**64-1)) for i in range(var_count)]
        assign_const_str_lst = [bitValueToStr(varTypeToBit(
            assign_type_lst[i]), assign_value_lst[i]) for i in range(var_count)]

        for i in range(var_count):
            r_res_lst_1.append(
                f"A {var_name_lst_1[i]} ( {assign_const_str_lst[i]} )")
            res_value = varBitTran(
                assign_bit_lst[i], var_bit_lst[i], assign_value_lst[i])
            res_value_str = bitValueToStr(var_bit_lst[i], res_value)
            r_res_lst_2.append(f"A {var_name_lst_2[i]} ( {res_value_str} )")

        for i in range(var_count):
            r_res_lst_1.append(f"O {var_name_lst_1[i]}")
            r_res_lst_2.append(f"O {var_name_lst_2[i]}")

        for i in range(var_count):
            r_res_lst_1.append(f"R {var_name_lst_1[i]}")
            r_res_lst_2.append(f"R {var_name_lst_2[i]}")


def checkOs(r_res_lst_1: list, r_res_lst_2: list) -> None:
    test_count = 20
    for _ in range(test_count):
        var_types = random.sample(g_var_types, 2)
        r_res_lst_1.append(f"D {var_types[0]} v001")
        r_res_lst_2.append(f"D {var_types[1]} v001")
        random_value = random.randint(0, 2**64-1)
        r_res_lst_1.append(f"A v001 ( {bitValueToStr(64, random_value)} )")
        r_res_lst_2.append(f"A v001 ( {bitValueToStr(64, random_value)} )")
        r_res_lst_1.append(f"O v001")
        r_res_lst_2.append(f"O v001")
        r_res_lst_1.append(f"R v001")
        r_res_lst_2.append(f"R v001")


def checkAsExps(r_res_lst_1: list, r_res_lst_2: list) -> None:

    test_count = 20
    var_used_count = 50
    cur_var_num = 0
    new_var_dec_set = set()
    var_value_dict = dict()

    while (cur_var_num < var_used_count):
        new_var_name = f"v{random.randint(0, 999):03d}"
        if (new_var_name not in new_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_num += 1

    for new_var_name in new_var_dec_set:
        new_var_type = g_var_types[random.randint(0, 3)]
        line_str = f"D {new_var_type} {new_var_name}"
        r_res_lst_1.append(line_str)
        r_res_lst_2.append(line_str)
        random_value = random.randint(0, 2**64-1)
        r_res_lst_1.append(
            f"A {new_var_name} ( {bitValueToStr(64, random_value)} )")
        r_res_lst_2.append(
            f"A {new_var_name} ( {bitValueToStr(64, random_value)} )")
        var_value_dict[new_var_name] = int(new_var_type[2:]), varBitTran(
            64, int(new_var_type[2:]), random_value)

    var_name = f"v{random.randint(0, 999):03d}"
    while (var_name in new_var_dec_set):
        var_name = f"v{random.randint(0, 999):03d}"
    var_type = g_var_types[random.randint(0, 3)]
    r_res_lst_1.append(f"D {var_type} {var_name}")
    r_res_lst_2.append(f"D {var_type} {var_name}")

    for _ in range(test_count):

        # ADD testing
        Exp1 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        Exp2 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        r_res_lst_1.append(f"A {var_name} ( {Exp1} + {Exp2} )")
        bit_num, result_value = expCalculation(
            f"( {Exp1} + {Exp2} )".split(" "), var_value_dict)
        r_res_lst_2.append(
            f"A {var_name} ( {bitValueToStr(bit_num, result_value)} )")

        r_res_lst_1.append(f"O {var_name}")
        r_res_lst_2.append(f"O {var_name}")

        # SUB testing
        Exp1 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        Exp2 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        r_res_lst_1.append(f"A {var_name} ( {Exp1} - {Exp2} )")
        bit_num, result_value = expCalculation(
            f"( {Exp1} - {Exp2} )".split(" "), var_value_dict)
        r_res_lst_2.append(
            f"A {var_name} ( {bitValueToStr(bit_num, result_value)} )")

        r_res_lst_1.append(f"O {var_name}")
        r_res_lst_2.append(f"O {var_name}")

        # AND testing
        Exp1 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        Exp2 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        r_res_lst_1.append(f"A {var_name} ( {Exp1} & {Exp2} )")
        bit_num, result_value = expCalculation(
            f"( {Exp1} & {Exp2} )".split(" "), var_value_dict)
        r_res_lst_2.append(
            f"A {var_name} ( {bitValueToStr(bit_num, result_value)} )")

        r_res_lst_1.append(f"O {var_name}")
        r_res_lst_2.append(f"O {var_name}")

        # OR testing
        Exp1 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        Exp2 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        r_res_lst_1.append(f"A {var_name} ( {Exp1} | {Exp2} )")
        bit_num, result_value = expCalculation(
            f"( {Exp1} | {Exp2} )".split(" "), var_value_dict)
        r_res_lst_2.append(
            f"A {var_name} ( {bitValueToStr(bit_num, result_value)} )")

        r_res_lst_1.append(f"O {var_name}")
        r_res_lst_2.append(f"O {var_name}")

        # NOT testing
        Exp1 = genExpression((0, 2*64-1), (0, 3), (0, 3), new_var_dec_set, 0)
        r_res_lst_1.append(f"A {var_name} ( ! {Exp1} )")
        bit_num, result_value = expCalculation(
            f"( ! {Exp1} )".split(" "), var_value_dict)
        r_res_lst_2.append(
            f"A {var_name} ( {bitValueToStr(bit_num, result_value)} )")

        r_res_lst_1.append(f"O {var_name}")
        r_res_lst_2.append(f"O {var_name}")

    r_res_lst_1.append(f"R {var_name}")
    r_res_lst_2.append(f"R {var_name}")

    for new_var_name in new_var_dec_set:
        line_str = f"R {new_var_name}"
        r_res_lst_1.append(line_str)
        r_res_lst_2.append(line_str)


def checkBs(r_res_lst_1: list, r_res_lst_2: list) -> None:

    test_count = 70
    var_used_count = 50
    cur_var_num = 0
    new_var_dec_set = set()
    var_value_dict = dict()

    while (cur_var_num < var_used_count):
        new_var_name = f"v{random.randint(0, 999):03d}"
        if (new_var_name not in new_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_num += 1

    for new_var_name in new_var_dec_set:
        new_var_type = g_var_types[random.randint(0, 3)]
        line_str = f"D {new_var_type} {new_var_name}"
        r_res_lst_1.append(line_str)
        r_res_lst_2.append(line_str)
        random_value = random.randint(0, 2**64-1)
        r_res_lst_1.append(
            f"A {new_var_name} ( {bitValueToStr(64, random_value)} )")
        r_res_lst_2.append(
            f"A {new_var_name} ( {bitValueToStr(64, random_value)} )")
        var_value_dict[new_var_name] = int(new_var_type[2:]), varBitTran(
            64, int(new_var_type[2:]), random_value)

    var_name = f"v{random.randint(0, 999):03d}"
    while (var_name in new_var_dec_set):
        var_name = f"v{random.randint(0, 999):03d}"
    var_type = g_var_types[random.randint(0, 3)]
    r_res_lst_1.append(f"D {var_type} {var_name}")
    r_res_lst_2.append(f"D {var_type} {var_name}")

    for _ in range(test_count):
        cur_line = len(r_res_lst_1)
        decis_num = random.randint(0, 1)
        Exp = f"( 00000000 )"
        if (decis_num == 0):
            Exp = genExpression((0, 0), (0, 3), (0, 0), new_var_dec_set, 0)
        else:
            Exp = genExpression((0, 2**64-1), (0, 3),
                                (0, 3), new_var_dec_set, 0)
        A_pre_str = f"A {var_name} ( 00000000 )"
        B_str = f"B {(cur_line+3):03d} {Exp}"
        new_exp = genExpression((0, 2**64-1), (0, 3),
                                (0, 3), new_var_dec_set, 0)
        A_str = f"A {var_name} {new_exp}"
        O_str = f"O {var_name}"

        r_res_lst_1.append(A_pre_str)
        r_res_lst_1.append(B_str)
        r_res_lst_1.append(A_str)
        r_res_lst_1.append(O_str)

        r_res_lst_2.append(A_pre_str)
        _, value_res = expCalculation(Exp.split(" "), var_value_dict)
        if (value_res == 0):
            r_res_lst_2.append(A_str)
        r_res_lst_2.append(O_str)

    r_res_lst_1.append(f"R {var_name}")
    r_res_lst_2.append(f"R {var_name}")

    for new_var_name in new_var_dec_set:
        line_str = f"R {new_var_name}"
        r_res_lst_1.append(line_str)
        r_res_lst_2.append(line_str)


if __name__ == "__main__":
    g_out_file_1 = open("input1.pig", "w")
    g_out_file_2 = open("input2.pig", "w")
    g_res_lst_1 = []
    g_res_lst_2 = []

    checkDsRs(g_res_lst_1, g_res_lst_2)
    checkOs(g_res_lst_1, g_res_lst_2)
    checkAsExps(g_res_lst_1, g_res_lst_2)
    checkBs(g_res_lst_1, g_res_lst_2)

    for line in g_res_lst_1:
        print(f"{line}\n", end='', file=g_out_file_1)
    for line in g_res_lst_2:
        print(f"{line}\n", end='', file=g_out_file_2)
