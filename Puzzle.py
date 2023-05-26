# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 8

def solve_puzzle(Board, Source, Destination):
    rows = len(Board)
    cols = len(Board[0])

    queue = [Source]
    neighbors = [(0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D')]

    directions = [[""] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    visited[Source[0]][Source[1]] = True

    while len(queue) > 0:
        curr_row, curr_col = queue.pop(0)

        if (curr_row, curr_col) == Destination:
            return path_Taken(directions, Source, Destination)

        for i, j, d in neighbors:
            next_row = curr_row + i
            next_col = curr_col + j
            if 0 <= next_row < rows and 0 <= next_col < cols and Board[next_row][next_col] == '-' and \
                    visited[next_row][next_col] is False:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col))
                directions[next_row][next_col] = d
    return


def path_Taken(dir, Source, Destiniation):
    directions = [Destiniation]
    string = ''
    curr = Destiniation
    while curr != Source:
        if dir[curr[0]][curr[1]] == 'R':
            directions.append((curr[0], curr[1] - 1))
            string = 'R' + string
            curr = (curr[0], curr[1] - 1)
        elif dir[curr[0]][curr[1]] == 'U':
            directions.append((curr[0] + 1, curr[1]))
            string = 'U' + string
            curr = (curr[0] + 1, curr[1])
        elif dir[curr[0]][curr[1]] == 'L':
            directions.append((curr[0], curr[1] + 1))
            string = 'L' + string
            curr = (curr[0], curr[1] + 1)
        elif dir[curr[0]][curr[1]] == 'D':
            directions.append((curr[0] - 1, curr[1]))
            string = 'D' + string
            curr = (curr[0] - 1, curr[1])
    return directions[::-1], string