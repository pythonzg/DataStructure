"""
选择排序
"""

def choice_sort(array):
    """
    选择排序的代码实现
    选择最后一个元素作为最小或最大值
    此处选择第一个作为最小值
    :param array:
    :return:
    """

    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if array[min_index] > array[j]:
                min_index = j
            array[i],array[min_index] = array[min_index],array[i]


if __name__ == '__main__':

    array = [6,3,2,15,34,57,46,1]
    choice_sort(array)
    print(array)