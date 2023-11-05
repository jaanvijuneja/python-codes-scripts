a = [2, 7, 8, 2, 9, 6, 6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            print(a[i])