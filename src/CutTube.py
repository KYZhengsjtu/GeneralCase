"""
长管切割
"""

# 完全背包：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是c[i]，价值是w[i]。
# 求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
import copy
from matplotlib import pyplot as plt

def complete_pack(num, sum_size, sizes, value):
    K = [[0 for x in range(sum_size + 1)] for x in range(num + 1)]
    g = [[] for x in range(sum_size + 1)]
    # Build table K[][] in bottom up manner
    for i in range(num + 1):
        for w in range(sum_size + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif sizes[i - 1] <= w:
                K[i][w] = uplimit(value[i - 1] + K[i - 1][w - sizes[i - 1]], K[i - 1][w])
                g[w] = g[w - sizes[i - 1]] + [sizes[i]]
            else:
                K[i][w] = K[i - 1][w]

    return g
    # f = [0] * (sum_size + 1)
    # g = [[] for x in range(sum_size + 1)]
    #
    # for i in range(0, num):
    #     for j in range(sizes[i], sum_size + 1, 1):
    #         if f[j - sizes[i]] + value[i] >= f[j]:
    #             g[j] = g[j - sizes[i]] + [sizes[i]]
    #         f[j] = max(f[j], f[j - sizes[i]] + value[i])
    # return g


def devide(a, b):
    x = a % b  # 余数
    y = a // b  # 取整
    return [x, y]


def fun(sum, size, i, d):
    a = devide(sum, size[i])
    d.append([size[i], a[1], a[0]])
    if a[0] > size[-1]:
        fun(a[0], size, i + 1, d)
    return d


def mult(a, b):
    mu = 1
    for i in range(len(a)):
        if i != b - 1:
            mu *= a[i] + 1
    return mu


# [1.2, 2.1, 3.3, 4.2, 6.4, 8.5]
if __name__ == '__main__':
    size = [1.2, 2.1, 3.3, 4.2, 6.4, 8.5]
    q = 10
    size = [int(i * q) for i in size]
    size.reverse()
    sum = 12 * q

    uplimit = [devide(sum, i)[1] for i in size]
    m = [devide(sum, i)[0] for i in size]
    # matrix = [[] for x in range(mult(max, 0))]
    matrix = [[]]
    for i in range(len(uplimit)):
        matrix2 = []
        for j in range(0, uplimit[i] + 1):
            matrix1 = copy.deepcopy(matrix)
            for s in matrix1:
                s.append(j)
            matrix2 += matrix1
        matrix = copy.deepcopy(matrix2)

    # print(matrix)
    matrix3 = []
    for s in matrix:
        sum1 = 0
        for t in range(len(s)):
            sum1 += s[t] * size[t]
        u = sum - sum1
        if max(m) >= u >= 0:
            s.append(u)
            matrix3.append(s)
    matrix3.sort(key=lambda ele: ele[-1])
    l = []
    matrix4 = []
    for q in matrix3:
        for i in range(len(q)-1):
            if q[i] != 0:
                l.append(i)
                pass
            pass
        l=list(set(l))
        matrix4.append(q)
        if len(l) == len(size):
            break
    print(matrix4)
    # matrix5 = []
    # for w in matrix4:
    #     for h in range(w):
    #         if w(h) != 0:
    #             for g



# plt.style.use('seaborn')
# plt.figure(figsize=(15,9))
# plt.rcParams.update({'font.family': "Microsoft YaHei"})
# plt.title("管材切割方案")
# plt.bar(cnbodfgbsort.index,cnbodfgbsort.PERSONS)
# plt.bar(cnbodfgbsort.index,cnbodfgbsort.PRICE)
# plt.bar(cnbodfgbsort.index,cnbodfgbsort.points)
# plt.show()
