"""
背包问题   动态规划
"""


# 01背包：有N件物品和一个容量为V的背包，每种物品均只有一件。第i件物品的费用是c[i]，价值是w[i]。
# 求解将哪些物品装入背包可使价值总和最大。
def zero_one_pack(num, sum_size, sizes, value):
    f = [0] * (sum_size + 1)
    g = [[] for x in range(sum_size + 1)]
    for i in range(0, num):
        for j in range(sum_size, sizes[i] - 1, -1):
            if f[j - sizes[i]] + value[i] >= f[j]:
                g[j] = g[j - sizes[i]]+[sizes[i]]
            f[j] = max(f[j], f[j - sizes[i]] + value[i])
    return f[-1]


# 完全背包：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是c[i]，价值是w[i]。
# 求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
def complete_pack(num, sum_size, sizes, value):
    f = [0] * (sum_size + 1)
    g = [[] for x in range(sum_size + 1)]

    for i in range(0, num):
        for j in range(sizes[i], sum_size + 1, 1):
            if f[j - sizes[i]] + value[i] >= f[j]:
                g[j] = g[j - sizes[i]]+[sizes[i]]
            f[j] = max(f[j], f[j - sizes[i]] + value[i])

    # print(g[-1])
    return f[-1]


if __name__ == '__main__':
    size = [1.2, 2.1, 3.3, 4.2, 6.4, 8.5]
    q = 10
    size = [int(i * q) for i in size]
    sum = [12]
    sum = [int(i * q) for i in sum]
    for i in range(len(sum)):
        print(complete_pack(len(size), sum[i], size, [1, 1, 1, 1, 1, 1]))
