from random import randint

def maze_generate(MAZE_WITHDETH, MAZE_HEIGHT):
            # return cell on the both sides of the wall
            def vertical_wall_cell(pos):
                return (pos + int(pos/(MAZE_WITHDETH-1)), pos + int(pos/(MAZE_WITHDETH-1)) + 1)
            def horizontal_wall_cell(pos):
                return (pos, pos + MAZE_WITHDETH)

            n_cell = MAZE_WITHDETH*MAZE_HEIGHT
            v_walls = (MAZE_WITHDETH-1)*MAZE_HEIGHT - 1
            h_walls = MAZE_WITHDETH*(MAZE_HEIGHT-1) - 1

            cells = [i for i in range(n_cell)] # cells
            walls = [[1] * (v_walls+1),[1] * (h_walls+1)] # [horizontal, vertical]
            # when cell = [0], the circle finish
            while len(set(cells)) != 1:
                # randomly select a wall and check cells on the both sides of the wall whether in the same group
                if randint(0,1) == 0: # vertical
                    wall = randint(0,v_walls)
                    if walls[0][wall] != 0:
                        cel = vertical_wall_cell(wall)
                        if cells[cel[0]] != cells[cel[1]]:
                            tmp = cells[cel[0]]
                            for c in range(n_cell):
                                if cells[c] == tmp:
                                    cells[c] = cells[cel[1]]
                            walls[0][wall] = 0 # remove the wall
                else: # horizontal
                    wall = randint(0,h_walls)
                    if walls[1][wall] != 0:
                        cel = horizontal_wall_cell(wall)
                        if cells[cel[0]] != cells[cel[1]]:
                            tmp = cells[cel[0]]
                            for c in range(n_cell):
                                if cells[c] == tmp:
                                    cells[c] = cells[cel[1]]
                            walls[1][wall] = 0 # remove the wall

            return walls

print(maze_generate(20,20))