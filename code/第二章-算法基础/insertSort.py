def insertSort(list):
    #遍历数组从第二个数开始，因为第一个数前没有可比较的数字，list从0开始
    for j in range(1,len(list)):
        #取出key值
        print(j)
        key = list[j]
        print("key:",key)
        #找到key前方数字
        i = j - 1
        #当key前方有大于key的数字则前移
        while i >=0 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        #大于key的数字前移会留出一个空位，key值放入
        list[i+1] = key
    return list
if __name__ == '__main__':
    list = [5, 2, 4, 6, 1, 3]
    list = insertSort(list)
    print(list)