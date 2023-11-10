# code to run and track comparisons of the path planning algorithms fromt eh PythonRobotics github 
# and the a-star implementation from the medium article

import time

from a_star import AStarPlanner
from bidirectional_a_star import BidirectionalAStarPlanner
from breadth_first_search import BreadthFirstSearchPlanner
from dijkstra import Dijkstra
from rrt_star import RRTStar
from a_star_impl import astar

# generate map info

maps = []

ox, oy = [], []
for i in range(-10, 60):
    ox.append(i)
    oy.append(-10.0)
for i in range(-10, 60):
    ox.append(60.0)
    oy.append(i)
for i in range(-10, 61):
    ox.append(i)
    oy.append(60.0)
for i in range(-10, 61):
    ox.append(-10.0)
    oy.append(i)
for i in range(-10, 40):
    ox.append(20.0)
    oy.append(i)
for i in range(0, 40):
    ox.append(40.0)
    oy.append(60.0 - i)

for i in range(10):
    maps.append({
        'start': (10.0, 10.0),
        'goal': (50.0, 50.0),
        'obstacles': tuple(zip(ox, oy)),
        'boundaries': (),
        'min_x_y': (-10, -10),
        'max_x_y': (60, 60)
    })

times = {
    'a-star': 0,
    'bidir-a-star': 0,
    'bfs': 0,
    'dijkstra': 0,
    'rrt-star': 0,
    'a-star-impl': 0
}

path_lengths = {
    'a-star': 0,
    'bidir-a-star': 0,
    'bfs': 0,
    'dijkstra': 0,
    'rrt-star': 0,
    'a-star-impl': 0
}

for m in maps:
    complete = m['obstacles'] + m['boundaries']
    ox, oy = zip(*complete)
    before = time.time()
    a_star = AStarPlanner(ox, oy, 1, 1)
    rx, ry = a_star.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    path_lengths['a-star'] += len(rx)
    times['a-star'] += after - before

    before = time.time()
    bidir_a_star = BidirectionalAStarPlanner(ox, oy, 1, 1)
    rx, ry = bidir_a_star.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    path_lengths['bidir-a-star'] += len(rx)
    times['bidir-a-star'] += after - before

    before = time.time()
    bfs = BreadthFirstSearchPlanner(ox, oy, 1, 1)
    rx, ry = bfs.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    path_lengths['bfs'] += len(rx)
    times['bfs'] += after - before

    before = time.time()
    dijkstra = Dijkstra(ox, oy, 1, 1)
    rx, ry = dijkstra.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    path_lengths['dijkstra'] += len(rx)
    times['dijkstra'] += after - before

    r = [0.5 for _ in range(len(ox))]
    obstacleList = tuple(zip(ox, oy, r))
    before = time.time()
    rrt = RRTStar(start=m['start'], goal=m['goal'], rand_area=[m['min_x_y'][0], m['max_x_y'][0]], obstacle_list=obstacleList, expand_dis=1, max_iter=5000, robot_radius=1)
    path = rrt.planning(False)
    after = time.time()
    path_lengths['rrt-star'] += len(path)
    times['rrt-star'] += after - before

    before = time.time()
    path = astar(m, m['start'], m['goal'])
    after = time.time()
    path_lengths['a-star-impl'] += len(path)
    times['a-star-impl'] += after - before

for key in path_lengths.keys():
    path_lengths[key] /= 10

for key in times.keys():
    times[key] /= 10

print(path_lengths)
print(times)