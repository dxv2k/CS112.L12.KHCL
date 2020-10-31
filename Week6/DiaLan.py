MAX_LENGTH = 12

def count_zero_bit(x,mask):
    # count zero bit by compare x with mask
    cnt = 0
    for pos in range(MAX_LENGTH):
        if (x >> pos) & 1 == 0 and (mask >> pos) & 1 == 1:
            cnt += 1
    return cnt

def solution(n,k,a): 
    mask = (1 << 12) - 1 # bin(4095) 
    cnt = 0 
    for pos in range(MAX_LENGTH):
        if (mask >> pos) & 1 == 1:
            tmp = -1
            for x in a:
                if (x >> pos) & 1 == 0 :
                    tmp_zero = count_zero_bit(mask & x,mask)
                    if tmp_zero > tmp:
                        tmp = tmp_zero
                        arg = x

            if (tmp == -1):
                print('NO')
                quit()

            cnt += 1
            mask &= arg
            if (mask == 0): break
    if cnt <= k: 
        print("YES")
    else: 
        print("NO")

n,k = map(int, input().split())
arr = list(map(int,input().split()))
solution(n,k,arr)


