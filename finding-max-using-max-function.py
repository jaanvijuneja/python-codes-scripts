list_a = [12, 8, 9, 11, 10]
tmp = list_a[0]
for i in range(1, len(list_a)):
    tmp = max(tmp, list_a[i])
print(tmp)