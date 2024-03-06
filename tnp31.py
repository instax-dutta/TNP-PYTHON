def solution(maze, sol, x, y):
    if x == len(maze[0]) - 1 and y == len(maze) - 1:
        sol[x][y] = 1
        return True

    if 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[x][y] == 0 and sol[x][y] == 0:
        sol[x][y] = 1

        if solution(maze, sol, x + 1, y): 
            return True
        if solution(maze, sol, x - 1, y): 
            return True
        if solution(maze, sol, x, y + 1): 
            return True
        if solution(maze, sol, x, y - 1):
            return True

        sol[x][y] = 0

    return False

maze = [[1, 1, 1, 0],
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 1]]
sol = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

if solution(maze, sol, 0, 0):
    print("Solution found!")
    for i in sol:
        print(i)
else:
    print("No solution found")
