import sys

if __name__ == "__main__":
    edges = [] #
    statementNum = 0 #
    RDlist = [] #
    leaders = [0] #

    BBnum = 0 #
    isUpdate = True

    lines = [] #original statememts
    for line in sys.stdin:
        processed_line = line.strip()
        if processed_line == '':
            continue
        
        if processed_line[0] == 'D':
            variable = processed_line.split()[2]
            RDlist.append((statementNum,'D',int(variable[1:]))) # add D cmd to RDlist
        elif processed_line[0] == 'R':
            variable = processed_line.split()[1]
            RDlist.append((statementNum,'R',int(variable[1:]))) # add R cmd to RDlist
        elif processed_line[0] == 'B':
            target = int(processed_line[2:5])
            if target not in leaders:
                leaders.append(target) #add leaders
            if statementNum+1 not in leaders:
                leaders.append(statementNum+1) #add leaders
            if target != statementNum + 1:
                edges.append((statementNum, target)) # add edge
            # if target != statementNum + 1:
                # edges.append((statementNum, statementNum+1)) # add edge
            
        lines.append(processed_line)
        statementNum += 1
    
    if leaders[-1] == statementNum: #remove exceeding index
        leaders.pop()
        # edges.pop()

    leaders.sort()
    BBnum = len(leaders) # the number of Basic Blocks

    BBlist = [] # (head, tail)
    for i in range(BBnum):
        if i != BBnum-1:
            BBlist.append((leaders[i],leaders[i+1]-1)) # head, tail
        else:
            BBlist.append((leaders[i],statementNum-1))

    #initialize OUTlist and INlist
    OUTlist = [0 for _ in range(BBnum+1)] # entry has OUT
    OUTlist[0] = (1 << 1000) -1
    INlist = [[] for _ in range(BBnum)] # BBnum []s
    for edge in edges:
        for i in range(BBnum): # srcBlock == targetBlock ?
            if BBlist[i][1] == edge[0]:
                srcBlock = i
            if BBlist[i][0] == edge[1]:
                targetBlock = i
        INlist[targetBlock].append(srcBlock)
    # INlist[0].append(-1) # entry output -> BB0
    for i in range(BBnum):
        INlist[i].append(i-1)

    # print("IN:",INlist) # test

    # construct abstract BBlist (i.e. only contains 'R' and 'D')
    abstractBBlist = [[] for _ in range(BBnum)]
    BBindex = 0
    for RDcmd in RDlist:
        for i in range(BBnum):
            if BBlist[i][1] >= RDcmd[0] >= BBlist[i][0]:
                abstractBBlist[i].append(RDcmd)
                # BBindex = i
                break
            # else:
            #     BBindex += 1
            #     abstractBBlist[BBindex].append(RDcmd)

    # print("abstractBBlist:", abstractBBlist) # test


    # Reaching Definition algo
    while(isUpdate):
        isUpdate = False
        for i in range(BBnum):
            unionInput = 0
            for inp in INlist[i]:
                unionInput |= OUTlist[inp+1]
            
            output = unionInput
            for cmd in abstractBBlist[i]: # transfer function
                if cmd[1] == 'R':
                    output |= (1 << cmd[2])
                if cmd[1] == 'D':
                    output &= ~(1 << cmd[2]) # 
            
            if output != OUTlist[i+1]:
                isUpdate = True
                OUTlist[i+1] = output
    # for i in range(BBnum+1): # test
    #     print("OUT:",~OUTlist[i] + 2**1000)
    # print(OUTlist) # test

    # find invalid statements for each BB
    invalidStatementNum = 0
    for i in range(BBnum):
        head, tail = BBlist[i]
        declaredVar = 0
        for inp in INlist[i]:
            declaredVar |= OUTlist[inp+1]

        # if i == 2: # test
        #     print("declared:",declaredVar)
        #     print("IN:", INlist[i])

        for offset in range(tail-head+1):
            components = lines[head+offset].strip().split()
            if components[0] == 'D':
                declaredVar &= ~(1 << int(components[2][1:]))
            elif components[0] == 'A':
                for c in components:
                    if c[0] == 'v':
                        if (declaredVar & (1 << int(c[1:]))) == (1 << int(c[1:])):
                            invalidStatementNum += 1
                            break
            elif components[0] == 'B':
                for c in components:
                    if c[0] == 'v':
                        if (declaredVar & (1 << int(c[1:]))) == (1 << int(c[1:])):
                            invalidStatementNum += 1
                            break
            elif components[0] == 'O':
                varNum = int(components[1][1:])
                if (declaredVar & (1 << varNum) == (1 << varNum)):
                    invalidStatementNum += 1
            elif components[0] == 'R':
                varNum = int(components[1][1:])
                if (declaredVar & (1 << varNum)) != (1 << varNum):
                    declaredVar |= (1 << varNum)
                else:
                    invalidStatementNum += 1

            else:
                print('invalid cmd', components)
                print("statement: ",head+offset) # test
    # test
    # x = sys.argv[1]
    # filename = f"./xiaoyu_{x}.pig"
    with open("1.out", "w") as f:
        f.write(str(invalidStatementNum))
        
    # test

    # print(invalidStatementNum) # right
                
            


    
    


