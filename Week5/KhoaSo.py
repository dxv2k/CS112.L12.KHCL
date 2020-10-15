s = input()
a = list(s)
int_s = int(s)
a.sort()

# Nếu dãy chia hết cho 3 thì sx dãy giảm gần, in dãy -> thoát
if int_s % 3 == 0:
    a.reverse()
    print(''.join(a))
    exit()

x = int(int_s % 3)

# Hàm trả về vị trí i trong a sao cho a[i] % 3 = x, nếu không trả về -1
def ind1(a, x):
    ind = -1
    if str(x) in a:
        ind = a.index(str(x))
    elif str(x + 3) in a:
        ind = a.index(str(x+3))
    elif str(x + 6) in a:
        ind = a.index(str(x+6))
    return ind

# Hàm trả về vị trí i, j trong a sao cho a[i] % 3 = x, a[j] % 3 = x, nếu không trả về -1, -1
def ind2(a, x):
    i1 = ind1(a, x)
    i2 = ind1(a[i1+1:], x) + i1 + 1
    return i1, i2

# Tìm và xóa vị trí không thỏa mãn điều kiện, sắp xếp lại dãy giảm dần, in dãy
ind = ind1(a, x)
if ind == -1:
    i1, i2 = ind2(a, (x*2)%3)
    if i1 != -1 and i2 != -1:
        a.remove(a[i1])
        a.remove(a[i2-1])

        a.reverse()

        if len(a) == 1:
            print(str(a[0]))
            exit()
        else:
            print(''.join(a))
            exit()
else:
    a.remove(a[ind])
    a.reverse()
    if a != []:
        print(''.join(a))
        exit()