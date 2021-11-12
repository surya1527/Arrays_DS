# Python program of above implementation

# structure is used to return two values from minMax()

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair:
    c = pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        c.max = arr[0]
        c.min = arr[0]
        return c

    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        c.max = arr[0]
        c.min = arr[1]
    else:
        c.max = arr[1]
        c.min = arr[0]

    for i in range(2, n):
        if arr[i] > c.max:
            c.max = arr[i]
        elif arr[i] < c.min:
            c.min = arr[i]

    return c


# Driver Code
arr = list(map(int, input().split()))
n = len(arr)
c = getMinMax(arr, n)
print(c.min)
print(c.max)
