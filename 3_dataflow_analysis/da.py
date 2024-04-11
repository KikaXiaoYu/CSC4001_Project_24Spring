

g_blocks = []
# D, A, R, B, O

g_branches = []


def readStdInputAsLst():
    res = []
    try:
        while (True):
            res.append(input())
    except:
        pass
    return res


def basicBlockConstruct(r_pig_lines, p_pig_size):
    '''
    based on pig lines, construct basic block info and declare res
    return form: 
    blocks_res = [
        [(start_line, end_line), 
        prev_block (),
        IN [0]^1000 concat [0]^declare_size (low to high),
        OUT [0]^1000 concat [0]^declare_size (low to high)
        ],
        ...
    ] (idx is the block idx)
    declare_res = [
        (line, var),
        ...
    ] (idx is the bit idx)
    '''
    # get leaders, predecessors, and declarations
    leaders_res = {-1, 0}  # all leaders including entry
    predecs_res = dict()  # tar line: {predecs}
    predecs_res[0] = {-1}
    declares_res = dict()  # var: {line: bit_idx}
    bit_idx = 1000
    for i in range(p_pig_size):
        line = r_pig_lines[i]
        tokens_lst = line.strip().split(" ")
        statement_type = tokens_lst[0]
        # Branch adds to predecs_res
        if (statement_type == 'B'):
            tar_line = int(tokens_lst[1], 10)
            leaders_res.add(tar_line)
            leaders_res.add(i + 1)
            if (tar_line not in predecs_res):
                predecs_res[tar_line] = {}
            predecs_res[tar_line].add(i)
            if ((i+1) not in predecs_res):
                predecs_res[i+1] = {i}
            predecs_res[i+1].add(i)
        # declare adds to declares_res
        elif (statement_type == 'D'):
            var_name = tokens_lst[2]
            if var_name not in declares_res:
                declares_res[var_name] = dict()
            declares_res[var_name][i] = bit_idx
            bit_idx += 1
    leaders_res = sorted(leaders_res)  # sorted all leaders

    # construct the blocks
    block_num = len(leaders_res)
    blocks_res = [[None, None, 0, 0]]
    for i in range(block_num):
        single_block_res = [None, None, 0, 0]
        start_line = leaders_res[i]
        end_line = leaders_res[i+1] if (i+1 != block_num) else p_pig_size
        single_block_res[0] = (start_line, end_line)
        single_block_res[1] = tuple([j+1 for j in predecs_res[i]])
        blocks_res.append(single_block_res)
    return blocks_res, declares_res


def doReachingDefAnalysis(r_pig_lines, p_pig_size, r_blocks_res, r_declares_res):
    # initialization
    chg_flag = 1
    block_num = len(r_blocks_res)
    dummy_mask = (1 << (1000)) - 1
    r_blocks_res[0][2] = dummy_mask
    # do update
    while (chg_flag == 1):
        for i in range(1, block_num):
            pass


def doUnDeclareDetection(r_pig_lines, p_pig_size, r_blocks_res, r_declares_res):
    pass


if __name__ == '__main__':
    g_blocks = []
    g_pig_lines = readStdInputAsLst()
    g_pig_size = len(g_pig_lines)
    g_blocks_res, g_declares_res = basicBlockConstruct(g_pig_lines, g_pig_size)
    doReachingDefAnalysis(g_pig_lines, g_pig_size,
                          g_blocks_res, g_declares_res)
    g_undc_lines, undc_num = doUnDeclareDetection(
        g_pig_lines, g_pig_size, g_blocks_res, g_declares_res)
    print(g_undc_lines)
    print(undc_num)
