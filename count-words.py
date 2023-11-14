str_var = "Write a program that takes a multi-line string input from the user. The program should count how many times each word appears in the string and print out a dictionary where the keys are words and values are the counts of those words. Treat words as case-insensitive and ignore punctuation."
new_string_list = str_var.replace(".", "").split(" ")
new_dic = {}

for word in new_string_list:
    if word in new_dic:
        new_dic[word] += 1
    else:
        new_dic[word] = 1
print(new_dic)