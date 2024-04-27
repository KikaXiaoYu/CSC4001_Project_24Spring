'''
True是1，False是0
'''
def find_leaders(instructions):
    leaders = set()
    n = len(instructions)
    leaders.add(0)  # 第一条指令总是领导者
    for i in range(n):
        if 'B' in instructions[i]:  # 假设'B'表示分支
            target = int(instructions[i].split()[1])-1
            leaders.add(target)
            if i + 1 < n:#这里要不要哦+1呢不确定
                leaders.add(i+1)
    return sorted(leaders)

def build_blocks(instructions, leaders):
    blocks = {}
    leader_iter = iter(leaders)
    current_leader = next(leader_iter)
    current_block = []

    for i, instr in enumerate(instructions):
        if i in leaders and current_block:
            blocks[current_leader] = current_block
            current_block = []
            current_leader = i
        current_block.append(instr)
    if current_block:
        blocks[current_leader] = current_block
    return blocks

def build_cfg(blocks, instructions):
    # cfg = {'entry': {'next': [], 'predecessors': []}, 'exit': {'next': [], 'predecessors': []}}
    cfg = {}
    block_ends = list(blocks.keys())
    for start in block_ends:
        cfg[start] = {'next': [], 'predecessors': []}
    
    # if blocks:
    #     cfg['entry']['next'].append(0)  # 从最小的领导者开始
    #     cfg[0]['predecessors'].append('entry')

    for start in block_ends:
        last_instr = blocks[start][-1]
        next_index = start + len(blocks[start])
        
        if 'B' in last_instr:  # 检查是否为分支指令
            target = int(last_instr.split()[1])
            if target not in cfg:
                cfg[target] = {'next': [], 'predecessors': []}  # 初始化目标块
            cfg[start]['next'].append(target)  # 添加到目标块
            cfg[target]['predecessors'].append(start)
            if next_index in blocks and next_index not in cfg[start]['next'] and start not in cfg[next_index]['predecessors']:  # 检查是否还有下一个块
                cfg[start]['next'].append(next_index)
                cfg[next_index]['predecessors'].append(start)
        elif next_index in blocks and next_index not in cfg[start]['next'] and start not in cfg[next_index]['predecessors']:  # 如果不是分支指令，流向下一个块
            cfg[start]['next'].append(next_index)
            cfg[next_index]['predecessors'].append(start)
        
        # if not cfg[start]['next']:  # 如果没有下一个块，连接到exit
        #     cfg[start]['next'].append('exit')
        #     # cfg['exit']['predecessors'].append(start)
    return cfg

def compute_gen_kill(blocks, definitions):
    # 计算每个基本块的 GEN 和 KILL 集合，并更新定义状态
    gen_kill = {}
    for block, instrs in blocks.items():
        # gen, kill = set(), set()
        local_defs = definitions.copy()  # 复制当前的定义状态
        for instr in instrs:
            parts = instr.split()
            command= parts[0]
            if command == 'D':
                var = parts[2]
                local_defs[var] = True
                # if var and local_defs[var] == False:
                #     gen.add(var)  # 新定义
            elif command == 'R':
                var = parts[1]
                if parts[1] in local_defs:
                    local_defs[var] = False
                    # if local_defs[var] == True:
                    #     kill.add(var)  # 删除定义
        gen_kill[block] = {'out': local_defs}
    return gen_kill

def analyze_dataflow(blocks, cfg, definitions):
    # 分析数据流，计算每个基本块的 IN 和 OUT 集合
    in_out = {block: {'in': None, 'out': None} for block in blocks}
    # 初始化第一个block的IN集为全0状态
    in_out[next(iter(blocks))]['in'] = {var: False for var in definitions}

    changed = True
    while changed:
        changed = False
        for block in blocks:
            # 计算IN集
            if block != next(iter(blocks)):  # 如果不是第一个块
                in_sets = [in_out[pred]['out'] for pred in cfg[block]['predecessors'] if in_out[pred]['out'] is not None]
                in_set = {var: all(local_defs[var] for local_defs in in_sets) for var in definitions} if in_sets else {var: False for var in definitions}
            else:
                in_set = in_out[block]['in']

            # 更新OUT集
            gen_kill_block = compute_gen_kill({block: blocks[block]}, in_set)
            out_set = gen_kill_block[block]['out']

            if in_out[block]['in'] != in_set or in_out[block]['out'] != out_set:
                in_out[block]['in'], in_out[block]['out'] = in_set, out_set
                changed = True

    return in_out

def count_undeclared_variables(blocks, in_out):
    # 计算可能使用了未声明变量的行数
    undefined_use_count = 0
    undeclared_uses = set()
    

    for block in blocks:
        local_defs = in_out[block]['in'].copy()  # 复制IN集作为当前的定义状态
        
        for i, instr in enumerate(blocks[block]):

            parts = instr.split(maxsplit=2)  # 按最多分割两次来处理指令
            
            command = parts[0]
            if command == 'A':
                target_var = parts[1]
                expr = parts[2]
                tokens = []
                for j in range(len(expr)):
                    if expr[j] == 'v':
                        tokens.append(expr[j:j+4])
                        j = j+3
                if target_var not in tokens:
                    tokens.append(target_var)
                for token in tokens:
                    # if token.startswith('v'):
                    if token not in local_defs or local_defs[token] == False:
                        undefined_use_count += 1
                        undeclared_uses.add((instr, block))
                        break

            elif command == 'B':  # 条件跳转
                # print(block,"localB",local_defs)
                expr = parts[2]
                tokens = []
                for j in range(len(expr)):
                    if expr[j] == 'v':
                        tokens.append(expr[j:j+4])
                        j = j+3
                # print(block,":",tokens)
                for token in tokens:
                    # if token.startswith('v'):
                    if token not in local_defs or local_defs[token] == False:
                        undefined_use_count += 1
                        undeclared_uses.add((instr, block))
                        
                        break
            
            elif command == 'O':
                token = parts[1]
                if token not in local_defs or local_defs[token] == False:
                        undefined_use_count += 1
                        undeclared_uses.add((instr, block))
                        
            # 根据指令更新定义状态
            elif command == 'D':
                local_defs[parts[2]] = True

            elif command == 'R' :
                # print(block,"localR",local_defs)
                if token not in local_defs or local_defs[parts[1]] == False:
                    undefined_use_count += 1
                    undeclared_uses.add((instr, block))
                elif local_defs[parts[1]] == True:
                    local_defs[parts[1]] = False
                    
    sorted_tuples = sorted(undeclared_uses, key=sort_by_block)
    # for line, block in sorted_tuples:
        # print(block,":",line)
    return len(undeclared_uses)

def sort_by_block(element):
    return element[1]

def initialize_definitions(instructions):
    # 初始化一个字典来追踪所有变量的定义状态
    definitions = {}
    for instr in instructions:
        parts = instr.split()
        if parts[0] == 'D':
            # 对于每个定义（D），将变量名作为键，初始值设为0
            definitions[parts[2]] = False
    return definitions

def main():
    try:
        instructions = []
        while True:
            line = input().strip()
            if line:  # 确保不处理空行
                instructions.append(line)
    except EOFError:
        pass
    
    definitions = initialize_definitions(instructions)

    # 执行您提供的函数来构建领导者，基本块和CFG
    leaders = find_leaders(instructions)
    # print(leaders)
    blocks = build_blocks(instructions, leaders)
    cfg = build_cfg(blocks, instructions)
    # print(cfg)

    # # 计算 GEN 和 KILL 集合
    # gen_kill = compute_gen_kill(blocks,definitions)

    # 进行数据流分析，得到每个基本块的IN和OUT集
    in_out = analyze_dataflow(blocks, cfg, definitions)
    # print(in_out)
    # 计算使用了未声明变量的行数
    undeclared_count = count_undeclared_variables(blocks, in_out)
    # print("Number of lines with undeclared variable use:", undeclared_count)

    # 输出结果
    print(undeclared_count, end='')

if __name__ == '__main__':
    main()