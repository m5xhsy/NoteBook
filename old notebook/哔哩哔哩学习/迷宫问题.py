"""
maze = [  # <-----y轴
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # x轴
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # |
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # |
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],  # |
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],  # V
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y + 1),  # 右
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x, y - 1)  # 左
]


def solve_maze(x1, y1, x2, y2):
    stack=[]
    stack.append((x1, y1))
    maze[x1][y1] = 2
    while len(stack) > 0:
        cur_node = stack[-1]
        if cur_node == (x2, y2):
            return stack
        for d in dirs:
            nx, ny = d(*cur_node)
            if maze[nx][ny] == 0:
                stack.append((nx, ny))
                maze[nx][ny] = 2
                break
        else:
            stack.pop()
    return False


print(solve_maze(1, 1, 8, 8))
"""

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y + 1),  # 右
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x, y - 1)  # 左
]

from queue import Queue


def solve_maze(x1, y1, x2, y2):
    q = Queue()
    q.put((x1, y1, -1))
    maze[x1][y1] = 2
    traceback = list()
    while q.qsize() > 0:
        cur_node = q.get()
        traceback.append(cur_node)
        if cur_node[:-1] == (x2, y2):
            path = []
            flag = len(traceback) - 1
            while flag >= 0:
                path.append(traceback[flag][0:2])
                flag = traceback[flag][2]

            return path[::-1]

        for d in dirs:
            nx, ny = d(cur_node[0], cur_node[1])
            if maze[nx][ny] == 0:
                q.put((nx, ny, len(traceback) - 1))
                maze[nx][ny] = 2
    else:
        return False


print(solve_maze(1, 1, 8, 8))