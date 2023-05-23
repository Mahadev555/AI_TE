graph = {
    '2' : ['3','5'],
    '3' : ['4' , '8'],
    '5' : ['6'],
    '4' : ['7'],
    '8' : [],
    '6' : [],
    '7' : []
}

visit = []
queue = []

def bfs(visit,graph,node):
    visit.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m , end=" ")
        
        for i in graph[m]:
            if i not in visit:
                visit.append(i)
                queue.append(i)
                
bfs(visit,graph,'2')
                
    
