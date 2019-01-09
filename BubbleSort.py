"""
冒泡排序
"""

def bubble_sort(array):

    """
    冒泡排序的实现代码
    :param array:
    :return:
    """
    n = len(array)
    sort_border = n-1

    for i in range(n):
        is_sorted = 0
        for j in range(sort_border):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                # 判断此次是否进行交换
                is_sorted = 1
                # 获取最后一个交换的位置
                last_exchange_index = j
            # 交换的边界值,用来下次遍历交换的阀值sort_border-1
            sort_border = last_exchange_index
        # 如果没有交换说明排序完毕
        if is_sorted == 0:
            break

if __name__ == '__main__':

    array = [6,3,2,15,34,57,46,1]
    bubble_sort(array)
    print(array)