f_pos = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ReduceRe_en_Positive.txt", "r")  # 打开文件
f_neg = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ReduceRe_en_Negative.txt", "r")  # 打开文件
f_both = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/Both.txt", "r")  # 打开文件
lines_pos = f_pos.readlines()
lines_neg = f_neg.readlines()
lines_both = f_both.readlines()
pos = set()
neg = set()
res_pos = set()
res_neg = set()

for i in lines_pos:
    pos.add(i)
for i in lines_neg:
    neg.add(i)
both = pos & neg

res_pos = pos - both
res_neg = neg - both
print(len(pos))
print(len(neg))
print(len(both))
print(len(res_pos))
print(len(res_neg))

f_both.close()
f_pos.close()
f_neg.close()


with open("pos.txt", "w") as f:
    for i in res_pos:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("去兼有词完成")

with open("neg.txt", "w") as f:
    for i in res_neg:
        if i:
            f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("去兼有词完成")


