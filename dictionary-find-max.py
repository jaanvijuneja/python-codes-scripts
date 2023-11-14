list_a = [1,1,1,2,1,3,3,4]
dic = {}
for key in list_a:
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
print(dic)
max_freq = max(list(dic.values()))
for i in dic:
    if dic[i] == max_freq:
        print(i)