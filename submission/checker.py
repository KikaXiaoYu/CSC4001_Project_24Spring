
g_ols = (40, 60, 160, 230)


def judgeDsRs(r_lines_1, r_lines_2):
    # declare
    for i in range(0, 1 * g_ols[0] // 4, 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
        if any((ch != '0' for ch in line_content_1)):
            return False
        if any((ch != '0' for ch in line_content_2)):
            return False
    # assign
    for i in range(1 * g_ols[0] // 4, 2 * g_ols[0] // 4, 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
    # declare
    for i in range(2 * g_ols[0] // 4, 3 * g_ols[0] // 4, 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
        if any((ch != '0' for ch in line_content_1)):
            return False
        if any((ch != '0' for ch in line_content_2)):
            return False
    # assign
    for i in range(3 * g_ols[0] // 4, 4 * g_ols[0] // 4, 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
    return True


def judgeOs(r_lines_1, r_lines_2):
    for i in range(g_ols[0], g_ols[1], 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 == line_content_2:
            return False
        if len(line_content_1) == len(line_content_2):
            return False
    return True


def judgeAsExps(r_lines_1, r_lines_2):
    for i in range(g_ols[1], g_ols[2], 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
    return True


def judgeBs(r_lines_1, r_lines_2):
    for i in range(g_ols[2], g_ols[3], 1):
        line_content_1 = r_lines_1[i].strip()
        line_content_2 = r_lines_2[i].strip()

        if line_content_1 != line_content_2:
            return False
    return True


if __name__ == "__main__":
    g_file_1 = open("1.out", "r")
    g_file_2 = open("2.out", "r")
    g_lines_1 = g_file_1.readlines()
    g_lines_2 = g_file_2.readlines()
    if (
        len(g_lines_1) != 230
        or len(g_lines_2) != 230
    ):
        g_check_res = False

    g_out_file = open("res.out", "w")

    g_check_res = (
        judgeDsRs(g_lines_1, g_lines_2)
        and judgeOs(g_lines_1, g_lines_2)
        and judgeAsExps(g_lines_1, g_lines_2)
        and judgeBs(g_lines_1, g_lines_2)
    )

    if g_check_res:
        print(0, file=g_out_file)
    else:
        print(1, file=g_out_file)
