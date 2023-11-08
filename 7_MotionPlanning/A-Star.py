import time

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    # def __repr__(self):
    #     return str(self.position)
    
    # def __hash__(self):
    #     return hash(repr(self))

    def __str__(self):
        return f"Pos: {self.position}"
        

class Maze():
    """A maze class for A* Pathfinding"""

    def __init__(self, start, end, obstacles):
        self.start = start
        self.end = end
        self.obstacles = obstacles


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    
    openDict = {}
    closedDict = {}

    startNode = Node(None, start)
    startNode.f = startNode.g = startNode.h = 0

    endNode = Node(None, end)
    endNode.f = endNode.g = endNode.h = 0

    openDict[startNode.position] = startNode

    while len(openDict) > 0:
        currentNode = openDict[min(openDict, key=lambda o: openDict[o].f)]

        del openDict[currentNode.position]
        closedDict[currentNode.position] = currentNode

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])

            # Check if node position is valid
            if node_position[0] < maze.start[0] or node_position[0] > maze.end[0] or node_position[1] < maze.start[1] or node_position[1] > maze.end[1]:
                continue

            # check if node is on obstacle
            if node_position in maze.obstacles:
                continue

            # create new node
            newNode = Node(currentNode, node_position)

            children.append(newNode)

        for child in children:
            if child.position in closedDict:
                continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            if child.position in openDict:
                if child.g < openDict[child.position].g:
                    openDict[child.position] = child
                else:
                    continue
            
            openDict[child.position] = child



def main():

    obstacles = set()
    for i in range(-10, 40):
        obstacles.add((20, i))
    for i in range(20, 60):
        obstacles.add((40, i))

    m_start = (-10, -10)
    m_end = (60,60)
    maze = Maze(m_start, m_end, obstacles)

    start = (10,10)
    end = (50,50)

    print("running")
    before = time.time()

    path = astar(maze, start, end)

    after = time.time()
    print(f"done in {after - before:.3f} seconds")
    print(path)


if __name__ == '__main__':
    main()
