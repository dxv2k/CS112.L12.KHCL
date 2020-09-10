def solution(n,arr): 
	p,q = 0,0 # p: start, q: end of the given part of the track  
	sum, result = arr[0], arr[0] # return on investment with p,q part	
	# for i in range(n): 
	# 	sum = max(arr[i], sum + arr[i])
	# 	result = max(result,sum) 
	# return result 
	for i in range(n): 
		if arr[i] >= sum+arr[i]:
			sum = arr[i]
			p = i+1
			print(arr[p])
		else:  
			sum = sum + arr[i] 
			q = i
			print(arr[q])
		result = max(result,sum)
	return p,q,result

def main(): 
	# test case 1 
	n = 16 
	arr = [2,-4,5,-8,4,-1,-1,1,1,1,-2,2,4,-6,9,-4] 
	# answered: 5 15 12 
	print(solution(n,arr))

if __name__ == "__main__": 
	main()





