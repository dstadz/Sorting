# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []

    while len(arrA) > 0  and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
        print(arrA,arrB)
        print(merged_arr)

    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA = arrA[1:]

        print(arrA,arrB)
        print(merged_arr)

    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB = arrB[1:]

        print(arrA,arrB)
        print(merged_arr)

    # TO-DO
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr;
    x = arr[:len(arr)//2]
    y = arr[len(arr)//2:]
    print(x,y)
    x = merge_sort(x)
    y = merge_sort(y)
    print(x,y)
    return merge(x,y)


print(merge_sort([1,5,8,7,6,4,3,9,2]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr




x = []
print(len(x))




# TO-DO: complete the helpe function below to merge 2 sorted arrays

