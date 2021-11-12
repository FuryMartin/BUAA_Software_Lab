#线性探测法：https://www.cnblogs.com/longerQiu/p/11703441.html
#平均查找长度ASL计算：https://www.cnblogs.com/ygsworld/p/10238729.html
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
        for index in range(H,len(hash_table)):
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
            index = hash_mod(H + pow(i,2))
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

    hash_table, suc_count, err_count = get_hash_table(hash_length, key_list, hash_type)

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

if __name__ == '__main__':
    global hash_key

    # TEST 1
    hash_key = 13

    keys_1 = [24,30,23,41,51,68,46,11,14,61,35]
    length_11 = 15
    length_12 = 13

    print("------------------------")
    print("TEST 1:")
    print_hash_ASL(keys_1, length_11, hash_type='linear') 
    print("------------------------")
    print_hash_ASL(keys_1, length_12, hash_type='linear') 

    # TEST 2
    hash_key = 11

    keys_2 = [46, 25, 40, 15, 67, 34, 6, 21]
    length_2 = 11
    print("------------------------")
    print("TEST 2:")
    print_hash_ASL(keys_2, length_2, hash_type='linear')
    print("------------------------")
    print_hash_ASL(keys_2, length_2, hash_type='square')

    print("------------------------")

    '''
    1.实验结果：
    ------------------------
    TEST 1:
    哈希表：        [-1, 14, 41, 68, 30, -1, -1, 46, -1, 61, 23, 24, 51, 11, 35]
    装填系数：      0.73
    查找成功ASL:    1.64
    查找失败ASL:    3.13
    ------------------------
    哈希表：        [-1, 14, 41, 68, 30, -1, -1, 46, -1, 61, 23, 24, 51]
    装填系数：      0.85
    查找成功ASL:    1.36
    查找失败ASL:    2.62
    ------------------------
    TEST 2:
    哈希表：        [-1, 67, 46, 25, 15, 34, 6, 40, -1, -1, 21]
    装填系数：      0.73
    查找成功ASL:    1.50
    查找失败ASL:    3.64
    ------------------------
    哈希表：        [34, 67, 46, 25, 15, -1, 6, 40, -1, -1, 21]
    装填系数：      0.73
    查找成功ASL:    1.25
    查找失败ASL:    3.18
    ------------------------
    2.实验结论
    装填系数越大，ASL越小；装填系数相同，二次探测ASL更小
    '''
