# code to run and track comparisons of the path planning algorithms fromt eh PythonRobotics github 
# and the a-star implementation from the medium article

import matplotlib.pyplot as plt
import numpy as np
import time

from a_star import AStarPlanner
from bidirectional_a_star import BidirectionalAStarPlanner
from breadth_first_search import BreadthFirstSearchPlanner
from dijkstra import Dijkstra
from rrt_star import RRTStar
from a_star_impl import astar

# generate map info

maps = []

obstacles = []
for i in range(3,9):
    obstacles.append((4, i))

boundaries = []
for i in range(11):
    boundaries.append((i, 0))
    boundaries.append((0, i))
    boundaries.append((10, i))
    boundaries.append((i, 10))


maps.append({
    'start': (1,1),
    'goal': (9,7),
    'obstacles': obstacles,
    'boundaries': boundaries,
    'min_x_y': 0,
    'max_x_y': 10
})

times = {
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
    a_star.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    times['a-star'] += after - before

    before = time.time()
    bidir_a_star = BidirectionalAStarPlanner(ox, oy, 1, 1)
    bidir_a_star.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    times['bidir-a-star'] += after - before

    before = time.time()
    bfs = BreadthFirstSearchPlanner(ox, oy, 1, 1)
    bfs.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    times['bfs'] += after - before

    before = time.time()
    dijkstra = Dijkstra(ox, oy, 1, 1)
    dijkstra.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    times['dijkstra'] += after - before

    before = time.time()
    rrt = RRTStar(ox, oy, 1, 1)
    rrt.planning(m['start'][0], m['start'][1], m['goal'][0], m['goal'][1])
    after = time.time()
    times['rrt-star'] += after - before

    before = time.time()
    astar(m, m['start'], m['goal'])
    after = time.time()
    times['a-star_impl'] += after - before

    
