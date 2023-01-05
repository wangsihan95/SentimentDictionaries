f_pos = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ALL_EN_Positive.txt", "r")  # 打开文件
f_neg = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/All_EN_Negative.txt", "r")  # 打开文件
f_both = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/Both.txt", "r")  # 打开文件
lines_pos = f_pos.readlines()
lines_neg = f_neg.readlines()
lines_both = f_both.readlines()

'''
1.需要统计Both词分别在f1和f2中出现的次数,最多的是2
2.如果f1中出现的次数比f2中出现的次数多，那么这个词属于f1
3.这个比例可以设置，2/3(66%)，或者3/4(75%)
'''

# 这个程序有bug
pos = {}
neg = {}
all = {}

pos_list = []
neg_list = []
for j in lines_pos:
    # j = j.rstrip('\n')
    j = j.lstrip(" ")
    j = j.rstrip(" ")
    pos_list.append(j)

for k in lines_neg:
    # k = k.rstrip('\n')
    k = k.lstrip(" ")
    k = k.rstrip(" ")
    neg_list.append(k)


for i in lines_both:
    # i = i.rstrip('\n')
    i = i.lstrip(" ")
    i = i.rstrip(" ")
    # replace('\n','')
    pos[i] = 0
    neg[i] = 0

    pos[i] = pos_list.count(i)
    neg[i] = neg_list.count(i)


res_pos = []
res_neg = []
for i in pos:
    if pos[i] == neg[i]:
        pass
    elif pos[i] > neg[i]:
        res_pos.append(i)
    else:
        res_neg.append(i)


# for i in res_pos:
#     print(i)
#     #all[i] = pos[i] + neg[i]

with open("pos.txt", "w") as f:
    for i in res_pos:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("找到posMore")

with open("neg.txt", "w") as f:
    for i in res_neg:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("找到negMore")


# for i in res_pos:
#     print(i)
#
# with open("test.txt", "w") as f:
#     for i in res_pos:
#         f.write(i)  # 自带文件关闭功能，不需要再写f.close()
#         #f.write("\n")
#     print("找到兼性词的偏向")