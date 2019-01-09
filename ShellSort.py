"""
希尔排序
"""
def shell_sort(array):
    n = len(array)
    gap = n // 4
    while gap>0:
        for j in range(gap,n):
            i = j
            while i >0 :
                if array[i] < array[i-gap]:
                    array[i],array[i-gap] = array[i-gap],array[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    array = [23,1,4,3,32,14,35,53,5]
    shell_sort(array)
    print(array)