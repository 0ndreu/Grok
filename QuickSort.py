def quicksort (arr):
    if len(arr) < 2:
        return arr
    else:
        mainElem = arr[0]

        less = [i for i in arr[1:] if i <= mainElem]
        more = [i for i in arr[1:] if i > mainElem]

        return (quicksort(less) + [mainElem] + quicksort(more))

a = [1, 3, 4, 7, 5, 5]

f = quicksort(a)
print(f)