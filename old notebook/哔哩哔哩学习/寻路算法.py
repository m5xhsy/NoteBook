# A*寻路算法
from queue import PriorityQueue


def heuristic(a, b):  # 曼哈顿距离
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()  # 存放这一轮探索过的所有边界方块，是一个优先队列，可用通过代价排序，并取出代价最低的方块
    frontier.put(start, 0)  # 先存放一个元素，也就是起点
    came_from = {}  # 当前方块到之前方块的映射，代表路径的来向
    cost_so_far = {}  # 代表方块的当前代价
    came_from[start] = None  # 起点came_from置空
    cost_so_far[start] = 0  # 当前代价置0
    while not frontier.empty():  # 队列不为空，循环一直进行
        current = frontier.get()  # 每次循环算法会从优先队列取出代价最低的方块

        if current == goal:  # 检测是不是终端点块
            break

        for next in graph.neighbors(current):  # 对方块上下左右也就是next进行操作
            new_cost = cost_so_far[current] + graph.cost(current, next)  # 计算新代价，之前的代价加上current到next的代价
            if next not in cost_so_far or new_cost < cost_so_far[next]:  # next没被探测过或者当前代价比之前找的更加低
                cost_so_far[next] = new_cost
                property = new_cost + heuristic(goal, next)  # 总代价等于当前代价加上预估代价
                frontier.put(next, property)  # 加入优先队列
                came_from[next] = current
    return came_from, cost_so_far


a_star_search((1, 2), ())
