"""
插入排序
"""

def insert_sort(array):
    """
    插入排序代码实现
    选择排序的优化
    后一个元素与前一个元素对比,如果满足大小条件则交换,继续与前一个对比,一直到前一个不满足条件停止对比
    此处取第一个元素作为起始比较值
    :param array:
    :return:
    """
    n = len(array)
    for i in range(1,n):

        while i>0:
            if array[i] < array[i-1]:
                array[i],array[i-1] = array[i-1],array[i]
            # 优化
            else:
                break
            i -= 1

if __name__ == '__main__':
    array = [6,2,3,23,15,32,52,25]
    insert_sort(array)
    print(array)