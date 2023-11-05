a = [2, 7, 8, 2, 2, 9, 6, 6]
tmp = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j] and (len(tmp) == 0 or a[i] != tmp[-1]):
                 tmp.append(a[i])
print(tmp)