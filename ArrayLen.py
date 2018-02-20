def get_arr_len(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        return 1 + get_arr_len(arr)

a = [1]

f = int(get_arr_len(a))
print(f)