visited = []
queue = []
# def bfs(graph): 

#def largeOutput(largeNum): 
#	base = int(1e9+7)
#	return (largeNum % base)  	



def addEdge(u,v,graph): 
	try: 
		graph[u].append(v) 
	except: 
		graph[u] = [v]
	try: 
		graph[v].append(u)
	except: 
		graph[v] = [u]


graph = {} 
n,m = map(int, input().split())
for _ in range(m): 
	u,v = map(int, input().split())
	addEdge(u,v,graph)

print(graph)











