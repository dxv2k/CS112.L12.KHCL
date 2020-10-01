def H_Index_Calc(n, arr):
    arr.sort(reverse = True)
    h_index = 0
    for i, num_paper in enumerate(arr):
        if num_paper >= i+1:
            h_index = i+1
        else:
            break
    return h_index

def main():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(H_Index_Calc(n, arr))

if __name__ == "__main__":
    main()