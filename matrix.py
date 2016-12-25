def matrix_multiple(a, b):
    ans = [[0 for i in range(len(a))] for i in range(len(b[0]))]
    # print(ans)
    if not len(a[0]) == len(b):
        print("They can not be multiplication!")
        return 0

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ans[i][j] += a[i][k] * b[k][j]
            # print(ans[i][j])

    return ans


def matrix_logical_or(a, b):
    if not len(a) == len(b) or not len(a[0]) == len(b[0]):
        return "They can not be added!"
    else:
        ans = [[0 for i in range(len(a))] for i in range(len(a[0]))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                if a[i][j] == 1 or b[i][j] == 1:
                    ans[i][j] = 1
                else:
                    ans[i][j] = 0
        return ans


if __name__ == '__main__':
    a = [[1] * 4] * 4
    b = [[1, 2, 1, 0], [2, 2, 1, 0], [2, 3, 1, 0], [0, 2, 1, 0]]
    print(matrix_multiple(a, b))
    print(matrix_logical_or(a, b))
