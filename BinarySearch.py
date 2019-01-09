"""
二分查找
"""

def binary_search(array,value):
    """
    递归实现二分查找
    :param array:
    :param value:
    :return:
    """
    n = len(array)
    mid = n // 2
    if n<=0:
        return False
    if array[mid] == value:
        return True
    elif array[mid] > value:
        return binary_search(array[:mid],value)
    else:
        return binary_search(array[mid+1:],value)

    # return False

def binary_search2(array,value):
    """
    非递归实现二分查找
    :param array:
    :param value:
    :return:
    """
    n = len(array)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2

        if array[mid] == value:
            return True
        elif array[mid] > value:
            last = mid-1
        else:
            first = mid+1
    return False

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,11,22,33,44,55,66]
    # print(binary_search(array,8))
    print(binary_search2(array,11))