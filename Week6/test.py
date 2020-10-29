mask = (1 << 12) - 1

# count number of 1 bits and see how much left with
# 12 bit in the mask  
def number_bit_zero(x,mask):
    cnt = 0
    for pos in range(12):
        if (x >> pos) & 1 == 0 and (mask >> pos) & 1 == 1:
            cnt += 1
    return cnt

print(number_bit_zero(mask&4,mask))

# n, k = map(int,input().split())
# a = list(map(int,input().split()))


# cnt = 0
# for pos in range(12):
#     if (mask >> pos) & 1 == 1:
#         tmp = -1
#         for x in a:
#             if (x >> pos) & 1 == 0 :
#                 #print(x)
#                 #print('------------------------------')
#                 tmp_zero = number_bit_zero(mask & x,mask)
#         #print(tmp_zero)
#                 if tmp_zero > tmp:
#                     tmp = tmp_zero
#                     arg = x
#         if (tmp == -1):
#             print('NO')
#             quit()

#         cnt += 1
#         mask &= arg
#     #print(mask)
#         if (mask == 0): break

# if cnt <= k:
#     print('YES')
# else:
#     print('NO')


