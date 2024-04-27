

def readStdInputToLst() -> list:
    '''
    Used for reading the Std Input into a list
    '''
    str_lst_res = []
    try:
        while (True):
            str_lst_res.append(input())
    except:
        pass
    return str_lst_res


def basicBlockConstruct(r_pig_lines: list, p_pig_size: int) -> tuple:
    '''
    based on pig lines, construct basic block info and declare res

    return form: 
    blocks_res = [
        [(start_line, end_line), 
        prev_block (),
        OUT [0]^1000 concat [0]^declare_size (low to high)
        ],
        ...
    ] (idx is the block idx)

    declare_res = [
        (line, var),
        ...
    ] (idx is the bit idx)
    '''
    # init leaders, predecessors, and declarations
    leaders_res = set({-1, 0, p_pig_size})
    # denote the entry leader as -1, exit leader as pig_size
    predecs_res = dict()  # form: dict{ tar_line: set{ predecs_line} }
    predecs_res[0] = set({-1})
    declares_res = dict()  # form dict{ var_name: dict{ line: bit_idx} }
    bit_idx_sft = 1000  # 1000 bits shifting reserved for dummy defs

    for i in range(p_pig_size):
        line_str = r_pig_lines[i]
        tokens_lst = line_str.strip().split(" ")
        statement_type = tokens_lst[0]
        # Branch adds to predecs_res
        if (statement_type == 'B'):
            tar_line = int(tokens_lst[1], 10)
            leaders_res.add(tar_line)  # tar_line is leader
            leaders_res.add(i + 1)  # next line is leader
            if (tar_line not in predecs_res):
                predecs_res[tar_line] = set()  # init dict key
            predecs_res[tar_line].add(i)
            if ((i+1) not in predecs_res):
                predecs_res[i+1] = set()  # init dict key
            predecs_res[i+1].add(i)
        # Declare def adds to declares_res
        elif (statement_type == 'D'):
            var_name = tokens_lst[2]
            if var_name not in declares_res:
                declares_res[var_name] = dict()  # init dict key
            declares_res[var_name][i] = bit_idx_sft
            bit_idx_sft += 1
    leaders_res = sorted(leaders_res)  # sorted all leaders
    ends_res = leaders_res[1:]  # get all ends line
    ends_res.append(p_pig_size+1)  # add exit

    ''' 
    Now the form is
    leaders_res = [ -1, 0, x1, ..., xn, p_pig_size ]
    ends_res = [ 0, x1, x2, ..., p_pig_size, p_pig_size+1 ]
    predecs_res = dict{ tar_line: set{ predecs_line} } # only branch now
    declares_res =  dict{ var_name: dict{ line: bit_idx} }
    '''

    # construct the blocks with start line and end line
    block_num = len(leaders_res)
    blocks_res = []
    for i in range(0, block_num):
        single_block_res = [None, None, 0]
        start_line = leaders_res[i]
        end_line = ends_res[i]
        single_block_res[0] = (start_line, end_line)
        blocks_res.append(single_block_res)

    # add prev_blocks except for entry and exit
    for i in range(1, block_num-1):
        single_block_ref = blocks_res[i]
        start_line = single_block_ref[0][0]
        predecs_lines = predecs_res[start_line]  # always end_line - 1
        if (start_line-1 not in predecs_lines):  # prev end line
            predecs_lines.add(start_line-1)
        prev_blocks = tuple([ends_res.index(j+1) for j in predecs_lines])
        # now prev_blocks contains branches and prev_blocks
        single_block_ref[1] = prev_blocks

    return blocks_res, declares_res


def getBlockIn(p_prev_blocks: tuple, r_blocks_res: list) -> int:
    '''
    get the union of the prev_blocks' out
    '''
    res = 0
    for i in p_prev_blocks:
        res = res | r_blocks_res[i][2]
    return res


def doDeclare(p_cur_def: int, p_line_num: int,
              r_tokens_lst: list, r_declares_res: dict) -> int:
    '''
    based on Declare statement, kill dummy and other def
    set the def of cur line and return the def_res
    '''
    var_name = r_tokens_lst[2]
    def_res = p_cur_def
    # kill the dummy
    dummy_idx = int(var_name[1:], 10)
    def_res &= ~(1 << dummy_idx)

    for def_line, bit_idx in r_declares_res[var_name].items():
        # since all declaration statements have been checked
        # var_name is guaranteed to be exist
        if def_line == p_line_num:  # set the definition
            def_res |= 1 << bit_idx
        else:  # kill other definition
            def_res &= ~(1 << bit_idx)
    return def_res


def doDestroy(p_cur_def: int, p_line_num: int,
              r_tokens_lst: list, r_declares_res: dict) -> int:
    '''
    based on Destroy statement, set dummy and kill other def
    return the def_res
    '''
    var_name = r_tokens_lst[1]
    def_res = p_cur_def
    # set the dummy
    dummy_idx = int(var_name[1:], 10)
    def_res |= 1 << dummy_idx
    # kill all definitions
    if (var_name not in r_declares_res):
        # since it may destroy some not exist var
        # need to check the var first and init it
        r_declares_res[var_name] = dict()
    for _, bit_idx in r_declares_res[var_name].items():
        def_res &= ~(1 << bit_idx)
    return def_res


def getBlockOut(p_start_line: int, p_end_line: int, p_block_in: int,
                r_pig_lines: list, r_declares_res: dict) -> int:
    '''
    based on blocks and block in, return the block out
    '''
    block_out_res = p_block_in
    for i in range(p_start_line, p_end_line):
        line = r_pig_lines[i]
        tokens_lst = line.strip().split(" ")
        statement_type = tokens_lst[0]
        if (statement_type == 'D'):
            block_out_res = doDeclare(
                block_out_res, i, tokens_lst, r_declares_res)
        elif (statement_type == 'R'):
            block_out_res = doDestroy(
                block_out_res, i, tokens_lst, r_declares_res)
    return block_out_res


def doReachingDefAnalysis(r_pig_lines: list, r_blocks_res: list,
                          r_declares_res: dict) -> None:
    '''
    Do Reaching Definition analysis and update the blocks_res OUT
    '''
    # initialization
    chg_flag = 1
    block_num = len(r_blocks_res)
    dummy_mask = (1 << (1000)) - 1
    r_blocks_res[0][2] = dummy_mask
    # do update
    while (chg_flag == 1):
        chg_flag = 0
        for i in range(1, block_num-1):
            # get current block
            single_block_ref = r_blocks_res[i]
            start_line, end_line = single_block_ref[0]
            # get previous blocks
            prev_blocks = single_block_ref[1]
            prev_block_out = single_block_ref[2]
            # get current block in
            new_block_in = getBlockIn(
                prev_blocks, r_blocks_res)
            # get block out
            new_block_out = getBlockOut(
                start_line, end_line, new_block_in,
                r_pig_lines, r_declares_res)

            if (new_block_out != prev_block_out):
                chg_flag = 1
                single_block_ref[2] = new_block_out


def expVarDetect(r_tokens_lst: list, res: list) -> None:
    '''
    Detect the variables used in the exp (recursively)
    The result is automatically saved in res list
    '''
    # end condition
    if (len(r_tokens_lst) == 3):
        str1 = r_tokens_lst[1]
        if (str1[0] == "v"):  # variable condition
            res.append(str1)
        else:  # constant condition
            return
    # recursive condition (containing EXP)
    elif (r_tokens_lst[1] == "!"):  # not condition
        expVarDetect(r_tokens_lst[2:-1], res)
        return
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
        expVarDetect(
            r_tokens_lst[1:cur_idx], res)
        expVarDetect(
            r_tokens_lst[cur_idx+1:-1], res)
        return


def getAssignVar(r_tokens_lst: list) -> list:
    '''
    Get Assign Statement's variable used
    '''
    res = []
    var_name = r_tokens_lst[1]
    res.append(var_name)
    expVarDetect(r_tokens_lst[2:], res)
    return res


def getBranchVar(r_tokens_lst: list) -> list:
    '''
    Get Branch Statement's variable used
    '''
    res = []
    expVarDetect(r_tokens_lst[2:], res)
    return res


def getOutputVar(r_tokens_lst: list) -> list:
    '''
    Get Output Statement's variable used
    '''
    res = []
    var_name = r_tokens_lst[1]
    res.append(var_name)
    return res


def getDestroyVar(r_tokens_lst: list) -> list:
    res = []
    '''
    Get Destroy Statement's variable used
    '''
    var_name = r_tokens_lst[1]
    res.append(var_name)
    return res


def isLineUndeclared(r_used_var_lst: list, p_cur_def: int) -> bool:
    '''
    Judge whether the line has undeclared var or not
    if has, return True, else return False
    '''
    for var_name in r_used_var_lst:
        dummy_idx = int(var_name[1:], 10)
        if (p_cur_def & (1 << dummy_idx)):
            return True
    return False


def doUnDeclareDetection(r_pig_lines: list, r_blocks_res: list,
                         r_declares_res: dict) -> tuple:
    '''
    detect the undeclared lines
    return lines undeclared list and undclared number
    '''
    block_num = len(r_blocks_res)
    undc_lines_res = []  # record the lines undeclared
    undc_num = 0  # record the number of lines undeclared
    for i in range(1, block_num-1):
        single_block_ref = r_blocks_res[i]
        start_line, end_line = single_block_ref[0]
        prev_blocks = single_block_ref[1]
        cur_def = getBlockIn(prev_blocks, r_blocks_res)
        # detect undeclared
        for i in range(start_line, end_line):
            line = r_pig_lines[i]
            tokens_lst = line.strip().split(" ")
            statement_type = tokens_lst[0]
            used_var_lst = []
            if (statement_type == 'D'):
                cur_def = doDeclare(
                    cur_def, i, tokens_lst, r_declares_res)
            elif (statement_type == 'R'):
                used_var_lst = getDestroyVar(tokens_lst)
                if (isLineUndeclared(used_var_lst, cur_def)):
                    undc_lines_res.append(i)
                    undc_num += 1
                cur_def = doDestroy(
                    cur_def, i, tokens_lst, r_declares_res)
            else:
                flg = 0
                if (statement_type == 'A'):
                    used_var_lst = getAssignVar(tokens_lst)
                    flg = 1
                elif (statement_type == 'B'):
                    used_var_lst = getBranchVar(tokens_lst)
                    flg = 1
                elif (statement_type == 'O'):
                    used_var_lst = getOutputVar(tokens_lst)
                    flg = 1
                if (flg == 1 and isLineUndeclared(used_var_lst, cur_def)):
                    undc_lines_res.append(i)
                    undc_num += 1
    return undc_lines_res, undc_num


if __name__ == '__main__':
    g_pig_lines = readStdInputToLst()
    g_pig_size = len(g_pig_lines)
    # construct basic blocks
    g_blocks_res, g_declares_res = basicBlockConstruct(
        g_pig_lines, g_pig_size)
    # do reaching def analysis
    doReachingDefAnalysis(
        g_pig_lines, g_blocks_res, g_declares_res)
    # detect undelcared variables
    g_undc_lines, g_undc_num = doUnDeclareDetection(
        g_pig_lines, g_blocks_res, g_declares_res)
    # print(g_undc_lines)
    print(g_undc_num, end='')
