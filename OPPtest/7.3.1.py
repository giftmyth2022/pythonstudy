def f(a):
    if a <=2 :
        return 1
    else:
        return f(a-2) + f(a-1)

int = int(input("输入"))

print(f(int))