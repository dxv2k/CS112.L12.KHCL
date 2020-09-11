def BOT(n, arr):
    p, q, maximum = 0, 0, 0
    total = [] # Calculate total score and store into a list
    result = [p,q,0]
    for p in range(n):
        for q in range(n):
            if q > p:
                total.append(sum(arr[p:q+1]))
                m = max(total)
                if maximum != m:
                    maximum = m
                    result[0] = p+1
                    result[1] = q+1
                    result[2] = m
    return result
def main(): 
	# test case 1 
	n = 16
	arr = [2,-4,5,-8,4,-1,-1,1,1,1,-2,2,4,-6,9,-4] 
	# answered: 5 15 12 
	print(BOT(n,arr))

if __name__ == "__main__": 
	main()