def MP(a):
    if a == 1:
        return 1
    else:
        return a*MP(a-1)

int = int(input("请输入："))
d=MP(int)
print(d)