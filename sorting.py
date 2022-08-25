a = [1, 4, 2, 3, 6, 5, 7, 9, 8]

def mergesort(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    if len(left) != 1:
        mergesort(left)

    if len(right) != 1:
        mergesort(right)

    l = r = k = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1

        k += 1

    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        arr[k] = right[r]
        r += 1
        k += 1


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def insertionsort(arr):
    for i in range(len(arr) - 1):
        j = i
        while arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)


def selectionsort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mini]:
                mini = j

        swap(arr, i, mini)
