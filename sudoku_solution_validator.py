k = [
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]]


def validSolution(board):
    for line in board:
        if sum(line) != 45 or (0 in line):
            return False

    for i, val in enumerate(board):
        ver_sum = 0
        for j, val in enumerate(board):
            ver_sum += board[j][i]
        if ver_sum != 45:
            return False

    n = 0
    m = 0
    sum_arr = []
    for mi in k[0:3]:
        for li in k:
            n += 1
            sum_arr.append(sum(li[m:m + 3]))
            print(n, li[m:m + 3])

            if n >= 3:
                print(sum(sum_arr))
                if sum(sum_arr) != 45:
                    return False
                sum_arr = []
                n = 0
        m += 3
    return True


print(validSolution(k))



