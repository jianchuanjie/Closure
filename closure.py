import matrix

# 单位矩阵
def E(a):
    ans = [[0 for i in range(len(a))] for i in range(len(a))]
    for i in range(len(a)):
        ans[i][i] = 1
    return ans


# 求自反闭包
def reflexive_closure(a):
    ans = matrix.matrix_logical_or(a, E(a))
    return ans


# 求对称闭包
def symmetric_closure(a):
    ans = [[0 for i in range(len(a))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1 or a[j][i] == 1:
                ans[i][j] = 1
            else:
                ans[i][j] = 0

    return ans


# 求传递闭包     此处并没有使用warshall算法！！！
def transitive_closure(a):
    ans = [[0 for i in range(len(a))] for i in range(len(a))]
    m = a
    for i in range(len(a)):
        m = matrix.matrix_multiple(a, m)
        ans = matrix.matrix_logical_or(ans, m)
    return ans


if __name__ == '__main__':
    a = [[1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
    b = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
    print("自反闭包：")
    print(reflexive_closure(a))
    print(reflexive_closure(b))
    print("对称闭包： ")
    print(symmetric_closure(a))
    print(symmetric_closure(b))
    print("自反闭包：")
    print(transitive_closure(a))
    print(transitive_closure(b))

