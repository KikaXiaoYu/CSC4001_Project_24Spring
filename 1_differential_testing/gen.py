
import random

g_var_type = ("bv8", "bv16", "bv32", "bv64")
g_max_line_num = 700
g_max_iter = 4
g_max_block_dec = 10
g_max_block_output = 10
g_max_sub_block_num = 10


def valueBitToStr(p_value: int, p_bit: int):
    '''
    convert value, bit to str ( for expression )
    '''
    res_str = f"{p_value:0{p_bit}b}"[-p_bit:]
    return res_str


def genExpression(p_value_range: tuple, p_type_range: tuple,
                  p_decis_range: tuple, r_var_dec_set: set, p_rec_iter: int):
    '''
    get expression ramdomly recursively, based on 3 ranges
    p_value_range: from 0 to 2**64-1
    p_type_range: from 0 to 3
    p_decis_range: from 0 to 3
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
        value_str = valueBitToStr(const_value, const_bit)
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


def genOutputBlock(p_cur_line_num: int, r_var_dec_set: set, r_res_lst: list):
    '''
    randomly output lines based on var declared
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0):
        return 0

    # get the output vars
    output_var_count = random.randint(
        0, min(g_max_block_output, cur_max_cap // 2, len(r_var_dec_set)))
    output_var_set = random.sample(list(r_var_dec_set), output_var_count)

    # generate output lines
    for otuput_var_name in output_var_set:
        line_str = f"O {otuput_var_name}"
        r_res_lst.append(line_str)

    return output_var_count


def genAssignBlock(p_cur_line_num: int, r_var_dec_set: set, r_var_frz_set: set,
                   r_res_lst: list):
    '''
    randomly assign lines based on var declared
    new line num depend on number of "A ..." statement
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0):  # no more line can be added
        return 0

    # randomly generate assign number
    assign_var_count = random.randint(
        0, min(g_max_block_output, cur_max_cap // 2, len(r_var_dec_set - r_var_frz_set)))
    assign_var_set = random.sample(
        list(r_var_dec_set - r_var_frz_set), assign_var_count)

    # generate output lines
    for assign_var_name in assign_var_set:
        exp_str = genExpression(
            (0, 2**64-1), (0, 3), (0, 3), r_var_dec_set, 0)
        line_str = f"A {assign_var_name} {exp_str}"
        r_res_lst.append(line_str)

    return assign_var_count


def genIfBlock(p_cur_line_num: int, r_var_dec_set: set, r_var_frz_set: set,
               r_res_lst: list, p_rec_iter: int):
    '''
    if block is formed as:
    D (a random var not exist)
    A (new_var_name) (whether a 01 value or a expression)
    B (tar_line) (new_var_name or the expression)
    [ Basic Block ]
    R (new_var_name)
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap <= 4 or p_rec_iter > g_max_iter):
        return 0

    # determine new variables to be declared
    cur_var_count = 0  # in fact only 1, just for consistence
    new_var_dec_set = set()
    while (cur_var_count < 1):
        new_var_name = f"v{random.randint(0, 999):03d}"
        new_var_dec_set.add(new_var_name)
        if (new_var_name not in r_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_count += 1

    # declare
    new_var_type = g_var_type[random.randint(0, 3)]
    line_str = f"D {new_var_type} {new_var_name}"
    r_res_lst.append(line_str)

    # assign
    decis_dir = random.randint(0, 1)  # 0 for 01, 1 for expression
    if decis_dir == 0:  # 01
        exp_str = genExpression(
            (0, 1), (0, 3), (0, 0), r_var_dec_set, 0)
    else:  # expression
        exp_str = genExpression(
            (0, 2**64-1), (0, 3), (0, 3), r_var_dec_set, 0)
    line_str = f"A {new_var_name} {exp_str}"
    r_res_lst.append(line_str)

    # branch add wait ( need modification after adding basic block )
    # create basic block
    B_line_num = len(r_res_lst)
    r_res_lst.append(" ")
    if_block_line_num = genBasicBlock(
        p_cur_line_num+4, (r_var_dec_set | new_var_dec_set), r_var_frz_set, r_res_lst, p_rec_iter+1)

    # modify branch
    tar_line_num = B_line_num + 1 + if_block_line_num
    # 0 for var, 1 for expression (for testing)
    decis_dir = random.randint(0, 1)
    if decis_dir == 0:  # 01
        r_res_lst[B_line_num] = f"B {tar_line_num:03d} ( {new_var_name} )"
    else:  # expression
        r_res_lst[B_line_num] = f"B {tar_line_num:03d} {exp_str}"
    # add destory
    line_str = f"R {new_var_name}"
    r_res_lst.append(line_str)

    return (4 + if_block_line_num)


def genForBlock(p_cur_line_num: int, r_var_dec_set: set, r_var_frz_set: set,
                r_res_lst: list, p_rec_iter: int):
    '''
    for block is formed as:
    D (a random var not exist)
    A (new_var_name) (perhaps a small number, must > 0 for loop)
    [ Basic Block ]
    A (new_var_name) (new_var_value - 1)
    B (tar_line) (new_var_name) to basic block
    R (new_var_name)
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap <= 5 or p_rec_iter > g_max_iter):
        return 0

    # determine new variables to be declared
    cur_var_count = 0
    new_var_dec_set = set()
    while (cur_var_count < 1):
        new_var_name = f"v{random.randint(0, 999):03d}"
        if (new_var_name not in r_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_count += 1

    # declare
    new_var_type = g_var_type[random.randint(0, 3)]
    line_str = f"D {new_var_type} {new_var_name}"
    r_res_lst.append(line_str)
    r_var_frz_set.add(new_var_name)

    # assign
    exp_str = genExpression(
        (1, 3), (0, 3), (0, 0), r_var_dec_set, 0)
    line_str = f"A {new_var_name} {exp_str}"
    r_res_lst.append(line_str)
    tar_line_num = len(r_res_lst)

    # basic block
    for_block_line_num = genBasicBlock(
        p_cur_line_num+5, (r_var_dec_set | new_var_dec_set), r_var_frz_set, r_res_lst, p_rec_iter+1)

    # add assign minus
    decis_num = random.randint(0, 8)
    if decis_num != 0:
        exp_str = f"( ( {new_var_name} ) - ( 00000001 ) )"
    else:
        ext_exp = genExpression(
            (0, 3), (0, 3), (0, 3), r_var_dec_set, 0)
        exp_str = f"( ( {new_var_name} ) - {ext_exp} )"
    line_str = f"A {new_var_name} {exp_str}"
    r_res_lst.append(line_str)

    # add branch
    line_str = f"B {tar_line_num:03d} ( {new_var_name} )"
    r_res_lst.append(line_str)

    # add destory
    line_str = f"R {new_var_name}"
    r_res_lst.append(line_str)

    r_var_frz_set.remove(new_var_name)

    return (5 + for_block_line_num)


def genBasicBlock(p_cur_line_num: int, r_var_dec_set: set, r_var_frz_set: set,
                  r_res_lst: list, p_rec_iter: int):
    '''
    recursively generate lines saved in res_lst
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0 or p_rec_iter > g_max_iter):
        return 0

    # determine new variables to be declared
    new_var_dec_num = random.randint(
        0, min(g_max_block_dec, cur_max_cap // 2, 1000 - len(r_var_dec_set)))
    cur_var_num = 0
    new_var_dec_set = set()
    while (cur_var_num < new_var_dec_num):
        new_var_name = f"v{random.randint(0, 999):03d}"
        if (new_var_name not in r_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_num += 1
    new_var_dec_num = len(new_var_dec_set)
    # the stage results are dec_set and dec_num (correct)

    new_line_num = 0
    new_line_num += 2 * new_var_dec_num

    # generate declaration lines
    for new_var_name in new_var_dec_set:
        new_var_type = g_var_type[random.randint(0, 3)]
        line_str = f"D {new_var_type} {new_var_name}"
        r_res_lst.append(line_str)

    for _ in range(g_max_sub_block_num):
        decis_dir = random.randint(0, 4)
        if (decis_dir == 0):
            new_line_num += genBasicBlock(p_cur_line_num + new_line_num,
                                          (r_var_dec_set | new_var_dec_set),
                                          r_var_frz_set,
                                          r_res_lst,
                                          p_rec_iter+1)
        elif (decis_dir == 1):
            new_line_num += genOutputBlock(p_cur_line_num + new_line_num,
                                           (r_var_dec_set | new_var_dec_set),
                                           r_res_lst)
        elif (decis_dir == 2):
            new_line_num += genAssignBlock(p_cur_line_num + new_line_num,
                                           (r_var_dec_set | new_var_dec_set),
                                           r_var_frz_set,
                                           r_res_lst)
        elif (decis_dir == 3):
            new_line_num += genIfBlock(p_cur_line_num + new_line_num,
                                       (r_var_dec_set | new_var_dec_set),
                                       r_var_frz_set,
                                       r_res_lst,
                                       p_rec_iter+1)
        elif (decis_dir == 4):
            new_line_num += genForBlock(p_cur_line_num + new_line_num,
                                        (r_var_dec_set | new_var_dec_set),
                                        r_var_frz_set,
                                        r_res_lst,
                                        p_rec_iter+1)

    # generate destory lines
    for new_var_name in new_var_dec_set:
        line_str = f"R {new_var_name}"
        r_res_lst.append(line_str)

    return new_line_num


def genLineStrToLst():
    res_lst = []
    var_dec_set = set()
    var_frz_set = set()
    genBasicBlock(0, var_dec_set, var_frz_set, res_lst, 0)
    return res_lst


if __name__ == '__main__':
    g_file_out = open("input.pig", "w")
    g_lines_lst = genLineStrToLst()
    for line in g_lines_lst:
        print(f"{line}\n", end='', file=g_file_out)
