import re
f_pos = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/pos.txt", "r")  # 打开文件
f_neg = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/neg.txt", "r")  # 打开文件
lines_neg = f_neg.readlines()
lines_pos = f_pos.readlines()
pos = []
neg = []
with_num_pos = []
with_num_neg = []

for i in lines_pos:
    i = i.rstrip(" ")
    i = i.lstrip(" ")
    pos.append(i)

for i in lines_neg:
    i = i.rstrip(" ")
    i = i.lstrip(" ")
    neg.append(i)

with open("pos.txt", "w") as f:
    for i in pos:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("去掉右边空格")

with open("neg.txt", "w") as f:
    for i in neg:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("去掉右边空格")


# for i in lines_pos:
#     i = i.lstrip(" ")
#     if bool(re.search(r'\d', i)):
#         with_num_pos.append(i)
#     else:
#         pos.append(i)
#
# for i in lines_neg:
#     i = i.lstrip(" ")
#     if bool(re.search(r'\d', i)):
#         with_num_neg.append(i)
#     else:
#         neg.append(i)
#
#
#
# with open("pos.txt", "w") as f:
#     for i in pos:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("去除带数字的")
#
# with open("withnum_pos.txt", "w") as f:
#     for i in with_num_pos:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("pos_withnum")
#
# with open("neg.txt", "w") as f:
#     for i in neg:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("去除带数字的")
#
# with open("withnum_neg.txt", "w") as f:
#     for i in with_num_neg:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("neg_withnum")