#线性探测法：https://www.cnblogs.com/longerQiu/p/11703441.html
#平均查找长度ASL计算：https://www.cnblogs.com/ygsworld/p/10238729.html

def get_hash_table(length, key_list):
    
    #按照线性探测法生成哈希表，返回查找成功长度
    hash_table, suc_count = linear_hash(key_list, length)

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
        H = key % 13
        for index in range(H,len(hash_table)):
            suc_count += 1 
            if hash_table[index] == -1:
                hash_table[index] = key
                break
    return hash_table, suc_count

def print_hash_ASL(keys, length):
    key_list = keys
    hash_length = length

    hash_table, suc_count, err_count = get_hash_table(hash_length, key_list)

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
    keys = [24,30,23,41,51,68,46,11,14,61,35]
    length_1 = 15
    length_2 = 13
    print("------------------------")
    print_hash_ASL(keys ,length_1) 
    print("------------------------")
    print_hash_ASL(keys ,length_2) 


