low = 0
high = int(input("Введите максимальное число "))
search = int(input("Число, которое ищите "))
count = 1
a = high / 2
while search != a:
    if search > a:
        low = a
    else:
        high = a
    a = (high - low) / 2
    count += 1
print (count)