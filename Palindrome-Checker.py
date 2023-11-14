name_str = "ana"
rev_str = []
for i in range(len(name_str)-1, -1, -1):
    rev_str.append(name_str[i])
up_str = ''.join(rev_str)
if up_str == name_str:
    print("Given String is Palindrome!!")
else:
    print("Given String is not a Palindrome!!")