"""
归并排序
"""
def merge_sort(array):
    """
    归并排序代码实现,又称折半排序
    分为左右两个列表直到不可再分为止,递归排序
    左指针与右指针都从零开始,一直比较,然后单个移动,直到一方移动到最后一个元素所在的索引,然后添加进新列表
    :param array:
    :return:
    """
    n = len(array)
    if n <= 1 :
        return array
    mid = n//2
    # 分为左右两个列表递归排序
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])


    left_point = 0
    right_point = 0
    res = []
    while left_point != len(left_array) and right_point != len(right_array):
        if left_array[left_point] >= right_array[right_point]:
            res.append(right_array[right_point])
            right_point += 1

        else:
            res.append(left_array[left_point])
            left_point += 1


    res+=left_array[left_point:]
    res+=right_array[right_point:]


    return res



if __name__ == '__main__':

    array = [32,23,2,5,6,1,7,3,36,27,11]
    res = merge_sort(array)
    print(res)
