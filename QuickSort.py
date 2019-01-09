"""
快速排序
"""

def quick_sort(array,first,last):
    """
    快速排序的代码实现
    此处采取第一个作为中间值,通过low和high指针寻找中间位置,然后将中间位置赋值,递归排序
    :param array:
    :param first:
    :param last:
    :return:
    """
    if first >= last:
        return

    mid_value = array[first]
    low = first
    high = last
    while low < high:

        while low < high and array[high] > mid_value:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] <= mid_value:
            low += 1
        array[high] = array[low]



    array[low] = mid_value
    quick_sort(array,first,low-1)
    quick_sort(array,low+1,last)

if __name__ == '__main__':
    array = [3,2,14,41,23,23,6,3,7,11]
    first = 0
    last = len(array)-1
    quick_sort(array,first,last)
    print(array)