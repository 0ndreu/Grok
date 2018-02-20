def get_sum_arr(arr):
    if len(arr) == 3:
        return 0
    else:
        newarr = []
        for i in range(len(arr)):
            newarr.append(arr[i])
        newarr.pop(0)
        return arr[0] + get_sum_arr(newarr)

a = [1, 3, 4, 7]

f = int(get_sum_arr(a))
print(f)