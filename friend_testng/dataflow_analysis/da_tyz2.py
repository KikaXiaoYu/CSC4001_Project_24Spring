import sys
import re

if __name__ == "__main__":
    
    # global
    states = set()  # store the var states encountered in each branch statement
    idx_record = set()  # store the idx of each line that might contain error
    
    
    def find_vars(lines):
        vars = {}
        for line in lines:
            var_list = re.findall(r'v\d{3}', line)
        for var in var_list:
            vars[var] = 0   # 0 indicates undeclared
        return vars
    
    def da_start(idx, input_vars):
        """ Start dataflow analysis at line idx with vars as the initial state """
        
        vars = input_vars.copy()
        pc = idx
        while pc < len(lines):
            line = lines[pc]
            if line[0] == 'D':
                var = re.findall(r'v\d{3}', line)[0]
                vars[var] = 1
                
                # # redeclaration not counted
                # if vars[var] == 1:
                #     idx_record.add(pc)
                # else:
                #     vars[var] = 1
                
            elif line[0] == 'A':
                var = line[2:6]
                if vars[var] == 0:
                    idx_record.add(pc)
                else:
                    exp = line[7:]
                    var_list = re.findall(r'v\d{3}', exp)
                    found = 0
                    for var in var_list:
                        if vars[var] == 0:
                            idx_record.add(pc)
                            found = 1
                            break
                    if found == 0:
                        vars[var] = 1
            
            elif line[0] == 'O':
                var = line[2:]
                if vars[var] == 0:
                    idx_record.add(pc)
            
            elif line[0] == 'R':
                var = line[2:6]
                if vars[var] == 0:
                    idx_record.add(pc)
                else:
                    vars[var] = 0
            
            elif line[0] == 'B':
                statement, target, exp = line.split(" ", maxsplit=2)
                
                # check validity of expression
                var_list = re.findall(r'v\d{3}', exp)
                for var in var_list:
                    if vars[var] == 0:
                        idx_record.add(pc)
                        break
                
                # generate var state
                state = ""
                for var in sorted(vars):
                    state += str(vars[var])
                
                # branch
                if state + target not in states:
                    states.add(state + target)
                    da_start(int(target), vars)
                
            pc += 1
    
    lines = sys.stdin.read().strip().split("\n")
    init_vars = {}
    for line in lines:
        var_list = re.findall(r'v\d{3}', line)
        for var in var_list:
            init_vars[var] = 0   # 0 indicates undeclared
    da_start(0, init_vars)
    print(len(idx_record), end='')