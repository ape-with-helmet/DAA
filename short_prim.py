def short_path(graph,n):
    for x in range(10):
        for i in range(n):
            for j in range(i,n):
                for k in range(n):
                    if k==i or k==j:
                        continue
                    if graph[i][k]+graph[k][j]<graph[i][j]:
                        graph[i][j]=graph[i][k]+graph[k][j]
                        graph[j][i]=graph[i][k]+graph[k][j]
    for i in range(n):
        for j in range(i,n):
            if i==j:
                continue
            print(f"Cost of electrification between {i} and {j} is: ",graph[i][j])
n=int(input("Enter the no of power plants: "))
graph=[[0 for i in range(n)]for j in range(n)]
print("Enter the costs of electrification: ")
for i in range(n):
    for j in range(i,n):
        if i==j:
            continue
        x=int(input(f"Cost of electrification between {i} and {j}: "))
        graph[i][j]=x
        graph[j][i]=x
short_path(graph,n)
