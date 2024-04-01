if __name__ == "__main__":
    f = open("./1.out", "r")
    g = open("./2.out", "r")
    lines_f = f.readlines()
    lines_g = g.readlines()
    out = open("./res.out", "w")
    if len(lines_f) != len(lines_g):
        print(1, file=out)
        exit(0)
    for i in range(0, len(lines_f)):
        if lines_f[i] != lines_g[i]:
            print(1, file=out)
            exit(0)
    print(0, file=out)