"""
小和算法
"""

def small_sum(arr):
    if len(arr)<=1:
        return 0
    return merge_sort(arr,0,len(arr)-1)


def merge_sort(arr, l, r):
    if l==r:
        return 0
    mid = l + ((r - l) >> 1)
    # print(mid)
    return merge_sort(arr,l,mid)+merge_sort(arr,mid+1,r)+merge(arr,l,mid,r)

def merge(arr,l,mid,r):

    left_point = l
    right_point = mid+1
    res = 0
    while left_point <= mid and right_point <= r:
        if arr[left_point] < arr[right_point]:
            res += (r-right_point+1)*arr[left_point]
            left_point += 1
        else:
            right_point += 1

    return res


if __name__ == '__main__':
    array = [2,4,3,5]
    res = small_sum(array)
    print(res)



