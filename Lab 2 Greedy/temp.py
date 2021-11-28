def partible_backpack(names, weights, values):
    unit_values = []
    for weight, value in list(zip(weights, values)):
        unit_value = value/weight
        unit_values.append(unit_value)
    priority_list = sorted(
        list(zip(names, weights, unit_values)), key=lambda x: x[1], reverse=True)
    sum_weight = 0
    sum_value = 0
    result_list = []
    #print(priority_list)
    for name, weight, unit_value in priority_list:
        if sum_weight + weight < limit:
            value = weight*unit_value
        elif sum_weight + weight >= limit:
            weight = limit-sum_weight
            value = weight*unit_value
        sum_value += value
        sum_weight += weight
        result_list.append(tuple((name, weight, value)))
        if sum_weight >= limit:
            break

    result_list = (sorted(result_list, key=lambda x: x[0]))
    print("---------------------------------------------------")
    print("物品可分: 贪心算法\t总价值：{}".format(sum_value))
    formated_print(result_list)


def unpartible_backpack(names, weights, values):
    priority_list = sorted(list(zip(names, weights, values)),
                           key=lambda x: x[2], reverse=True)
    result_list = []
    sum_value = 0
    sum_weight = 0
    for name, weight, value in priority_list:
        if sum_weight+weight >= limit:
            break
        sum_weight += weight
        sum_value += value
        result_list.append(tuple((name, weight, value)))
    result_list = (sorted(result_list, key=lambda x: x[0]))
    print("---------------------------------------------------")
    print("物品不可分 贪心算法:\t总价值：{}".format(sum_value))
    formated_print(result_list)


def dp_pack(names, weights, values):
    back_pack_list = list(zip(names, weights, values))
    dp = [[0 for j in range(limit+1)] for i in range(len(names))]
    for i in range(limit-1, weights[0]-1, -1):
        dp[0][i] = dp[0][i-weights[0]] + values[0]
    for i in range(1, len(names)):
        for j in range(limit+1):
            if(j < weights[i]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
    j = limit
    selected = []
    for i in range(len(names)-1, -1, -1):
        if i == 0 and dp[i][j] != 0:
            selected.append(back_pack_list[i])
        if i >= 1 and dp[i][j] > dp[i-1][j]:
            selected.append(back_pack_list[i])
            j = j - weights[i]
    print("---------------------------------------------------")
    print("物品不可分 动态规划:\t总价值：{}".format(max(max(dp))))
    formated_print(sorted(selected, key=lambda x: x[0]))


def formated_print(para_list):
    names = []
    weights = []
    values = []
    for name, weight, value in para_list:
        names.append(name)
        weights.append(weight)
        values.append(value)
    print("名称\t", end="")
    for name in names:
        print("{}\t".format(name), end="")
    print("合计\t")
    print("重量\t", end="")
    for weight in weights:
        print("{}\t".format(weight), end="")
    print("{}\t".format(sum(weights)))
    print("价值\t", end="")
    for value in values:
        print("{:.1f}\t".format(value), end="")
    print("{}\t".format(sum(values)))


global limit
limit = 150
names = [1, 2, 3, 4, 5, 6, 7]
weights = [35, 30, 60, 50, 40, 10, 25]
values = [10, 40, 30, 50, 35, 40, 30]
partible_backpack(names, weights, values)
unpartible_backpack(names, weights, values)
dp_pack(names, weights, values)
