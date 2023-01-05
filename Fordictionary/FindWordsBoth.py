f_pos = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ReduceRe_en_Negative.txt", "r")  # 打开文件
f_neg = open("/Users/wangsihan/Desktop/SentimentDictionaries/EN/ReduceRe_en_Positive.txt", "r")  # 打开文件
s_pos = set()
s_neg = set()
lines1 = f_pos.readlines()
lines2 = f_neg.readlines()

for i in lines1:
    s_pos.add(i)
for j in lines2:
    s_neg.add(j)

print(len(s_pos))
print(len(s_neg))
f_pos.close()
f_neg.close()

s_both = s_pos & s_neg
print(len(s_both))

with open("test.txt", "w") as f:
    for i in s_both:
        f.write(i)  # 自带文件关闭功能，不需要再写f.close()
        #f.write("\n")
    print("找到交集")