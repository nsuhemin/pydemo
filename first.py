def move(num, fro, temp, to):
    if num == 0:
        return
    move(num - 1, fro, to, temp)
    print("从{}柱移动{}号盘到{}柱".format(fro, num, to))
    move(num - 1, temp, fro, to)

move(4, 'A', 'B', 'C')