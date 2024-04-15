
import random

g_var_type = ("bv8", "bv16", "bv32", "bv64")
g_max_line_num = 900
g_max_iter = 4
g_max_block_dec = 10
g_max_block_output = 10
g_max_sub_block_num = 10


def genOutputBlock(p_cur_line_num: int, r_var_dec_set: set, r_res_lst: list):
    '''
    randomly output lines based on var declared
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0):
        return 0
    var_output_num = random.randint(
        0, min(g_max_block_output, cur_max_cap // 2, len(r_var_dec_set)))
    new_line_num = 0
    var_output_set = random.sample(list(r_var_dec_set), var_output_num)

    # generate output lines
    for var_output_name in var_output_set:
        line_str = f"O {var_output_name}"
        r_res_lst.append(line_str)
    new_line_num += var_output_num

    return new_line_num


def genExpression(r_var_dec_set: set, p_rec_iter: int):
    if (p_rec_iter > g_max_iter):
        return 0
    var_value = random.randint(0, 2**64-1)
    var_bit = random.randint(1, 4) * 8
    inner_exp = f"{var_value:0{var_bit}b}"[-var_bit:]
    return (f"( {inner_exp} )")


def genAssignBlock(p_cur_line_num: int, r_var_dec_set: set, r_res_lst: list):
    '''
    randomly assign lines based on var declared
    '''
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0):
        return 0
    var_output_num = random.randint(
        0, min(g_max_block_output, cur_max_cap // 2, len(r_var_dec_set)))
    new_line_num = 0
    var_output_set = random.sample(list(r_var_dec_set), var_output_num)

    # generate output lines
    for var_output_name in var_output_set:
        expression = genExpression(r_var_dec_set, 0)
        line_str = f"A {var_output_name} {expression}"
        r_res_lst.append(line_str)
    new_line_num += var_output_num

    return new_line_num


def genBasicBlock(p_cur_line_num: int, r_var_dec_set: set, r_res_lst: list, p_rec_iter: int):
    '''
    recursively generate lines saved in res_lst
    '''
    # determine new variables to be declared
    cur_max_cap = max(0, g_max_line_num - p_cur_line_num)
    if (cur_max_cap == 0 or p_rec_iter > g_max_iter):
        return 0
    new_var_dec_num = random.randint(
        0, min(g_max_block_dec, cur_max_cap // 2, 1000 - len(r_var_dec_set)))
    new_line_num = 0
    cur_var_num = 0
    new_var_dec_set = set()
    while (cur_var_num < new_var_dec_num):
        new_var_name = f"v{random.randint(0, 999):03d}"
        if (new_var_name not in r_var_dec_set):
            new_var_dec_set.add(new_var_name)
            cur_var_num += 1
    # generate declaration lines
    for new_var_name in new_var_dec_set:
        new_var_type = g_var_type[random.randint(0, 3)]
        line_str = f"D {new_var_type} {new_var_name}"
        r_res_lst.append(line_str)
    new_line_num += 2 * new_var_dec_num

    for _ in range(g_max_sub_block_num):
        decis_num = random.randint(0, 4)
        if (decis_num == 0):
            new_line_num += genBasicBlock(p_cur_line_num + new_line_num,
                                          (r_var_dec_set | new_var_dec_set), r_res_lst, p_rec_iter+1)
        elif (decis_num == 1):
            new_line_num += genOutputBlock(p_cur_line_num + new_line_num,
                                           (r_var_dec_set | new_var_dec_set), r_res_lst)
        elif (decis_num == 2):
            new_line_num += genAssignBlock(p_cur_line_num + new_line_num,
                                           (r_var_dec_set | new_var_dec_set), r_res_lst)

    # generate destory lines
    for new_var_name in new_var_dec_set:
        line_str = f"R {new_var_name}"
        r_res_lst.append(line_str)

    return new_line_num


def genLineStrToLst():
    res_lst = []
    var_dec_set = set()
    genBasicBlock(0, var_dec_set, res_lst, 0)
    return res_lst


if __name__ == '__main__':
    g_file_out = open("input.pig", "w")
    g_lines_lst = genLineStrToLst()
    for line in g_lines_lst:
        print(f"{line}\n", end='', file=g_file_out)