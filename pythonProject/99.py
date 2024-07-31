print("输入一个整数:")
a = input()

a2 = int(a)
for i in range(1, a2+1):

    for j in range(1, i+1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()