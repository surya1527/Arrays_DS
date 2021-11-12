def pivot_place(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right


def quickSort(arr, first, last):
    if first < last:
        p = pivot_place(arr, first, last)
        quickSort(arr, first, p-1)
        quickSort(arr, p+1, last)


# main
arr = list(map(int, input().split()))
n = len(arr)
first = 0
last = n - 1
quickSort(arr, 0, last)
print(arr)
