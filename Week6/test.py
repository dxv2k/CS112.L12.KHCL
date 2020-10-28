# mask = (1 << 12) - 1

# def number_bit_zero(x,mask):
#     cnt = 0
#     for pos in range(12):
#         if (x >> pos) & 1 == 0 and (mask >> pos) & 1 == 1:
#             cnt += 1
#     return cnt


# x = int(input())
# print(number_bit_zero(x,mask))

n,k = map(int, input().split())
arr = tuple(map(bin, map(int, input().split() )))

count = [0] * 12 

print(arr)


