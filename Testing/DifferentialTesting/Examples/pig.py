if __name__ == "__main__":
    with open("./input.pig", "r") as f:
        g = open("./1.out", "w") 
        vars = dict()
        lines = f.readlines()
        for line in lines:
            if line[0] == 'D':
                continue
            if line[0] == 'A':
                vars[line[2:6]] = line[9:-2]
            if line[0] == 'O':
                print(vars[line[2:6]], file=g)
