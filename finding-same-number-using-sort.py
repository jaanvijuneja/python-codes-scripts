a = [2, 7, 8, 2, 2, 9, 10, 10]
a.sort()
tmp = []
for i in range(len(a)-1):
    if a[i] == a[i+1] and (len(tmp) == 0 or a[i] != tmp[-1]):
                 tmp.append(a[i])
print(tmp)