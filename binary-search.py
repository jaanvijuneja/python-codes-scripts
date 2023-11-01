list = [-1, 0, 3, 5, 9, 12, 19, 22, 7]
target = 9
left, right = 0, len(list) - 1
while (left <= right):
    mid = (left + right) // 2
    if (list[mid] < target):
        left = mid + 1
    elif (list[mid] > target):
        right = mid - 1
    else:
        print(mid)
        break