def matrixmulti(a, b):
    ans = [[0] * len(b[0])] * len(a)
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


if __name__ == '__main__':
    a = [[1] * 4] * 4
    b = [[1, 2, 1], [2, 2, 1], [2, 3, 1], [0, 2, 1]]
    print(matrixmulti(a, b))
