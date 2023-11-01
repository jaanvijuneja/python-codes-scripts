list_a = [12, 8, 9, 11, 10]
tmp = float('-inf')
tmp2 = float('-inf')

for val in list_a:
    tmp=max(tmp, val)

for val in list_a:
    if(val != tmp):
        tmp2=max(tmp2, val)

print(tmp2)