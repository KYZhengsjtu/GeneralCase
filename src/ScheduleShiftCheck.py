"""
排班防止用户填写错误
"""


def printTime(time):
    a = time % 24
    b = time // 24
    st = "第%s日%s点" % (b + 1, a)
    return st


'''
输入班次
'''
a1 = [8, 8]
a2 = [16, 24]
a3 = [0, 8]
a = [a1, a2, a3]
if __name__ == '__main__':
    if len(a) == 1:  # 单班次无需考虑
        if a[0][0] >= a[0][1]:
            print('班次一：当日%s点至次日%s点' % (a[0][0], a[0][1]))
        else:
            print('班次一：当日%s点至当日%s点' % (a[0][0], a[0][1]))
    else:  # 多班次校验24H和前后班次首尾无重叠
        for i in range(len(a) - 1):
            if a[i][0] >= a[i][1]:  # 当班次出现跨天，后续时间依次增加24H
                a[i][1] += 24
            if a[i + 1][0] < a[i][1]:  # 当班次间出现跨天，后续时间依次增加24H
                for j in range(i + 1, len(a)):
                    a[j][0] += 24
                    a[j][1] += 24
        # 开始判断
        # if a[-1][1] - a[0][0] > 24:
        #     exit("班次1开始时间%s，班次%d结束时间%s，排班跨度超过24H" % (printTime(a[0][0]), len(a), printTime(a[-1][1])))
        for i in range(len(a)):
            print('班次%d开始时间' % (i + 1), printTime(a[i][0]), '结束时间', printTime(a[i][1]))
            if a[i][1] - a[0][0] > 24:
                exit("班次1至班次%d跨度超过24H，问题班次--班次%s" % (i + 1, i + 1))
