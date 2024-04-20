
import random

'''
Exp -> LP CONSTANT RP
    -> LP VAR RP
    -> LP Exp Bop Exp RP
    -> LP NOT Exp RP

D TYPE VAR
1. wrong type of declaration
2. do not declare or wrong delcare
3. wrong value

A VAR Exp
1. wrong exp calculation
2. wrong variable to give

B Line Exp
1. wrong exp calculation
2. wrong variable to give
3. do not branch or wrong branch

O VAR
1. wrong type of output
2. wrong value

R VAR
1. do not destroy or wrong destroy

'''


g_var_types = ("bv8", "bv16", "bv32", "bv64")


def checkDeclare(r_res_lst_1:list, r_res_lst_2:list):
    var_count = 50
    var_num_lst = random.sample(range(0, 1000), var_count)
    var_type_lst = random.choices(g_var_types, k=var_count)
    idx_lst = [i for i in range(var_count)]
    print(var_count)
    print(var_num_lst)
    print(var_type_lst)

    # D statements
    idx_lst_1 = random.shuffle(idx_lst)
    idx_lst_2 = random.shuffle(idx_lst)
    for i in range(var_count):
        D_var_1 = var_num_lst[idx_lst_1[i]]
        D_type_1 = var_type_lst[idx_lst_1[i]]
        pig_line_1 = f"D {D_type_1} {D_var_1}"
        D_var_2 = var_num_lst[idx_lst_2[i]]
        D_type_2 = var_type_lst[idx_lst_2[i]]
        pig_line_2 = f"D {D_type_2} {D_var_2}"
        r_res_lst_1.append(pig_line_1)
        r_res_lst_2.append(pig_line_2)
        
    # A statements
    


def checkDestroy(p_file_1, p_file_2):
    pass


def checkOutput(p_file_1, p_file_2):
    pass


def checkAssign(p_file_1, p_file_2):
    pass


def checkBranch(p_file_1, p_file_2):
    pass


if __name__ == "__main__":
    g_out_file_1 = open("input1.pig", "w")
    g_out_file_2 = open("input2.pig", "w")
    g_res_lst_1 = []
    g_res_lst_2 = []

    checkDeclare(g_res_lst_1, g_res_lst_2)
    checkDestroy(g_res_lst_1, g_res_lst_2)
    checkOutput(g_res_lst_1, g_res_lst_2)
    checkAssign(g_res_lst_1, g_res_lst_2)
    checkBranch(g_res_lst_1, g_res_lst_2)
