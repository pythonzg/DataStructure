

def partition(array,left,right):
    i=left
    j=right
    compare = array[right]
    while i<j:
        if array[i]<compare:
            i+=1
        if array[j]>compare:
            j-=1
        if array[i]>array[j]:
            array[i],array[j] = array[j],array[i]
    return i


def quicksort(array,left,right):
    middle = partition(array,left,right)
    if middle>left:
        quicksort(array,left,middle-1)
        quicksort(array,middle,right)



if __name__ == '__main__':
    array = [2,3,9,8,4,6,5,7]
    quicksort(array,0,len(array)-1)
    print(array)