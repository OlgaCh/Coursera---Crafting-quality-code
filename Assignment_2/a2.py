# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, ch, row, col, num=0):
        self.symbol = ch
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num

    def __str__(self):
        return  '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)   

    def set_location(self, r, c):
        self.row = r
        self.col = c

    def eat_sprout(self):
        self.num_sprouts_eaten += 1

def calculate_num_sprouts(maze):
    count = 0
    for r in maze:
        for c in r:
            if c == SPROUT:
                count += 1
    return count

class Maze:
    """ A 2D maze. """

    def __init__(self, m, rat_1, rat_2, num_sprouts_left):
        self.maze = m
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = calculate_num_sprouts(self.maze)

    def is_wall(self, row, column):
        if self.maze[row][column] == WALL:
            return True
        else:
            return False

    def get_charactes(self, row, column):
        return self.maze[row][column] 

    def move(self, rat, vert, horiz):
        cur_row = rat.raw
        cur_col = rat.col
        new_col = cur_row + horiz
        new_row = cur_col + vert
        if self.maze[new_row][new_col] == WALL:
            return False
        rat.set_location(new_row, new_col)
        if self.maze[self.row][self.col] == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_lef -= 1
            self.maze[new_row][new_col] = HALL
        return True

    def __str__(self):
        for r in self.maze:
            for c in r:
                print c
            print '\n'
        print self.rat_1
        print self.rat_2


  
