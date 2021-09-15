# 注意点！！
# ・インデックスは０から始まっているのか、１から始まっているのか
# ・ちゃんと入力を受け取れているのか
# def make_list(s):
#     l = s.split("\n")
#     print(l)

# make_list()


# s = "SSSSSS.SSS..SSS.SS.S.S"
# print(s.count("S"))
# if "SS" in s:
#     print("yes")
#     a = s.replace("SS", "..", 1)
#     print(a)
#     s = a

lines = ["6 2",
"S.SSSS"]

n, k = map(int, lines[0].split())
s = lines[1]
for i in range(k):
    if "SSS" in s:
        a = s.replace("SSS", "...", 1)
        s = a
    elif "S.S" in s:
        a = s.replace("S.S", "...", 1)
        s = a
    elif "SS" in s:
        a = s.replace("SS", "..", 1)
        s = a
    elif "S" in s:
        a = s.replace("S", ".", 1)
        s = a
print(s.count("."))