#Adjacency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


#DFS implementaion using stack 
def DFS(graph, start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

#DFS implementation using recursion 
def DFS(graph, start, visited = None)
	if visited is None:
		visited = set()	
	else:
		if start not in visited:
			visited.add(start)
			for next in (graph[start] - visited):
				DFS(graph, next, visited)
	return visited 

#BFS implementation usinf queue
def BFS(graph, start):
	visited = set()
	queue = [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited 


