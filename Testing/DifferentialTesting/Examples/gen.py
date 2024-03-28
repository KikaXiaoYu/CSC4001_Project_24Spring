import random

if __name__ == "__main__":
    f = open("./input.pig", "w")
    var_types = ["bv8", "bv16", "bv32", "bv64"]
    var_nums = random.randint(1, 5)
    for i in range(0, var_nums):
        var_name = f"v00{i}"
        var_type = random.choice(var_types)
        bits = int(var_type[2:])
        stmt = f"D {var_type} {var_name}"
        print(stmt, file=f)
        val = random.choice(["0", "1"]) * bits
        stmt = f"A {var_name} ( {val} )"
        print(stmt, file=f)
    for i in range(0, var_nums):
        var_name = f"v00{i}"
        stmt = f"O {var_name}"
        print(stmt, file=f)

    