import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import time
import keyboard


def check_if_cell_lives(x, y, board):
    maxx = board.shape[0]-1
    maxy = board.shape[1]-1
    neighbour_count = 0
    if x != 0 and y != 0:
        neighbour_count += currentgen[x - 1, y - 1]
    if x != 0:
        neighbour_count += currentgen[x - 1, y]
    if y != 0:
        neighbour_count += currentgen[x    , y - 1]
    if x != maxx and y != maxy:
        neighbour_count += currentgen[x + 1, y + 1]
    if x != maxx:
        neighbour_count += currentgen[x + 1, y]
    if y != maxy:
        neighbour_count += currentgen[x    , y + 1]
    if x != maxx and y != 0:
        neighbour_count += currentgen[x + 1, y - 1]
    if x != 0 and y != maxy:
        neighbour_count += currentgen[x - 1, y + 1]


    if board[x, y] == 1 and (neighbour_count == 2 or neighbour_count == 3):
        # print("Any live cell with two or three live neighbours survives.")
        return 1
    elif board[x, y] == 0 and neighbour_count == 3:
        # print("Any dead cell with three live neighbours becomes a live cell.")
        return 1
    # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    return 0


def insert_shape(board, shape):
    match shape:
        case "block":
            board[0, 0] = 1
            board[0, 1] = 1
            board[1, 0] = 1
            board[1, 1] = 1
        case "beehive":
            board[0, 1] = 1
            board[0, 2] = 1
            board[1, 0] = 1
            board[1, 3] = 1
            board[2, 1] = 1
            board[2, 2] = 1
        case "blinker":
            board[1, 0] = 1
            board[1, 1] = 1
            board[1, 2] = 1
        case "pentadecathlon":
            board[2, 3] = 1
            board[2, 4] = 1
            board[2, 5] = 1
            board[3, 2] = 1
            board[3, 6] = 1
            board[4, 2] = 1
            board[4, 6] = 1
            board[5, 3] = 1
            board[5, 4] = 1
            board[5, 5] = 1

            board[10, 3] = 1
            board[10, 4] = 1
            board[10, 5] = 1
            board[11, 2] = 1
            board[11, 6] = 1
            board[12, 2] = 1
            board[12, 6] = 1
            board[13, 3] = 1
            board[13, 4] = 1
            board[13, 5] = 1

        case _:
            print("shape not found, inserting a block")
            board[0, 0] = 1
            board[0, 1] = 1
            board[1, 0] = 1
            board[1, 1] = 1
    return board


def draw_board(board):
    currentaxis = plt.gca()
    currentaxis.set_aspect('equal')
    step = 1/board.shape[0]
    for ii in range(board.shape[0]):
        for jj in range(board.shape[1]):
            if board[ii, jj] == 1:
                currentaxis.add_patch(Rectangle((jj * step, ii * step), step, step, fill=1, alpha=1))
    plt.show()
    return True


currentgen = np.zeros((20, 20))
nextgen = currentgen.copy()

currentgen = insert_shape(currentgen, input("choose initial shape out of: block, beehive, blinker, pentadecathlon"))
plt.figure()

last_draw = time.time()
draw_board(currentgen)

# print(currentgen)

while True:
    if keyboard.is_pressed("space"):
        break
    if last_draw + 1 < time.time():
        for i in range(currentgen.shape[0]):
            for j in range(currentgen.shape[1]):
                nextgen[i, j] = check_if_cell_lives(i, j, currentgen)
        currentgen = nextgen.copy()
        draw_board(currentgen)
        last_draw = time.time()
    # print(currentgen)
