# f_pos = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ALL_EN_Positive.txt", "r")  # 打开文件
f_neg = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/neg2.txt", "r")  # 打开文件
lines_neg = f_neg.readlines()
# lines_pos = f_pos.readlines()
# pos = set()
neg = set()
# for i in lines_pos:
#     # pos.add(i)
#     i = i.lstrip(" ")
#     if i.isupper():
#         i = i.lower()
#     pos.add(i)

for j in lines_neg:
    # neg.add(j)
    j = j.lstrip(" ")
    j = j.rstrip(" ")
    if j.isupper():
        j = j.lower()

    neg.add(j)

# f_pos.close()
f_neg.close()
# print(len(pos))
print(len(neg))

# arr_pos = []
arr_neg = []
# for i in pos:
#     arr_pos.append(i.lstrip(" "))
# arr_pos = sorted(arr_pos)

for i in neg:
    arr_neg.append(i.lstrip(" "))
arr_neg = sorted(arr_neg)

# with open("pos.txt", "w") as f:
#     for i in arr_pos:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("去重完成")

with open("neg.txt", "w") as f:
    for i in arr_neg:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("去重完成")