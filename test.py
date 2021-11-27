import math


def hash_mod(key):
    return key % hash_key


def get_hash_table(length, key_list, hash_type):

    #按照线性探测法生成哈希表，返回查找成功长度
    if hash_type == "linear":
        hash_table, suc_count = linear_hash(key_list, length)
    elif hash_type == "square":
        hash_table, suc_count = square_hash(key_list, length)
    else:
        print("Hash Type ERROR: use linear or square as parameters")

    #计算查找不成功长度
    err_count = 0
    for i in range(length):
        temp_hash = hash_table[i:length] + hash_table[0:i]
        err_count += temp_hash.index(-1)+1

    return hash_table, suc_count, err_count


def linear_hash(key_list, length):
    hash_table = [-1 for i in range(length)]
    suc_count = 0
    for key in key_list:
        H = hash_mod(key)
        for i in range(len(hash_table)):
            index = (i + H) % length
            suc_count += 1
            if hash_table[index] == -1:
                hash_table[index] = key
                break
    return hash_table, suc_count


def square_hash(key_list, length):
    hash_table = [-1 for i in range(length)]
    suc_count = 0
    for key in key_list:
        H = hash_mod(key)
        i = 0
        while True:
            index = hash_mod(H + pow(i, 2))
            suc_count += 1
            #print("{} + {}".format(H,pow(i,2)))
            if hash_table[index] == -1:
                hash_table[index] = key
                break
            if(i != 0):
                index = hash_mod(H - pow(i, 2))
                suc_count += 1
                #print("{} - {}".format(H, pow(i, 2)))
                if hash_table[index] == -1:
                    hash_table[index] = key
                    break
            i += 1
    return hash_table, suc_count


def print_hash_ASL(keys, length, hash_type):
    key_list = keys
    hash_length = length

    hash_table, suc_count, err_count = get_hash_table(
        hash_length, key_list, hash_type)

    #打印哈希表
    print("哈希表：\t{}".format(hash_table))

    #打印装填系数
    print("装填系数：\t{:.2f}".format(len(key_list)/len(hash_table)))

    #计算查找成功和不成功的平均查找长度
    SUC_ASL = suc_count/len(key_list)
    ERR_ASL = err_count/len(hash_table)

    #打印平均查找长度
    print("查找成功ASL: \t{:.2f}".format(suc_count/len(key_list)))
    print("查找失败ASL: \t{:.2f}".format(err_count/len(hash_table)))


global hash_key

# TEST 1
hash_key = 13

keys_1 = [24, 30, 23, 41, 51, 68, 46, 11, 14, 61, 35]
length_11 = 15
length_12 = 13

print("TEST 1:")
print_hash_ASL(keys_1, length_11, hash_type='linear')
print("------------------------")
print_hash_ASL(keys_1, length_12, hash_type='linear')


# TEST 2
hash_key = 11

keys_2 = [46, 25, 40, 15, 67, 34, 6, 21]
length_2 = 11
print("TEST 2:")
print_hash_ASL(keys_2, length_2, hash_type='linear')
print("------------------------")
print_hash_ASL(keys_2, length_2, hash_type='square')
