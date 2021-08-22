import pygame
from pygame.locals import *
import sys,os,random
from random import randint

MAZE_WITHDETH = 21
MAZE_HEIGHT = 21
BLOCK_SIZE = 30

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (122,122,122)

FPS = 30
# # 生成初始矩阵
# maze = [[i%2 for i in range(MAZE_WITHDETH)] for j in range(MAZE_HEIGHT)]
# for i in range(int(0.5*(MAZE_WITHDETH+1))):
#     maze[i*2] = [0 for i in range(MAZE_WITHDETH)]
# # 生成起点,0为上边，顺时针
# start = randint(0,3)
# start_point = []
# if start == 0:
#     start_point == [2 * int(randint(1, (MAZE_WITHDETH - 1)/2))-1, 1]
# elif start == 1:
#     start_point == [-2, 2 * int(randint(1, (MAZE_HEIGHT-1)/2))-1]
# elif start == 2:
#     start_point = [2 * int(randint(1, (MAZE_WITHDETH - 1)/2))-1, -2]
# elif start == 3:
#     start_point = [1, 2 * int(randint(1, (MAZE_HEIGHT-1)/2))-1]


class Maze(pygame.sprite.Sprite):
    def __init__(self, MAZE_WITHDETH:int, MAZE_HEIGHT:int, CELL_SIZE:int):

        # Randomized Prim's algorithm
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
            
    def colide(self):

    def update(self):
        
        







class Maze(pygame.sprite.Sprite):
    def __init__(self, size,block_size, walls):
        """
        params:
        size    地图尺寸
        block_size  单元格尺寸
        walls       地图数据
        """
        pygame.sprite.Sprite.__init__(self)
        self.block_size = block_size
        """迷宫中墙的数据
        [所有
            [竖直
                [[a,b],[c,d]],  起点[0,a]    终点[0,b]
                [[]]
                ],
            [水平
                [[]],
                [[]]
                ]
        ]
        """
        self.walls = walls
        self.image = pygame.Surface(size)
        d=walls[0]
        index = 0
        for lines in d:
            for line in lines:
                pygame.draw.line(self.image, color=BLACK, start_pos=[index, line[0]], end_pos=[index, line[1]])
            index += 1
        d = walls[1]
        index = 0
        for lines in d:
            for line in lines:
                pygame.draw.line(self.image, color=BLACK, start_pos=[line[0], index], end_pos=[line[1], index])
            index += 1
        
        def generate(self):
            

    def can_go(self, s_pos, e_pos):
        # 判断从s_pos 到 e_pos是否可以通过
        start = [0,0]
        end = [0,0]
        # 映射
        for i in range(2):
            start[i] = int(s_pos[i] / self.block_size[i])
            end[i] = int(e_pos[i] / self.block_size[i])
        if start[0] == end[0]:
            if start[1] == end[1]:
                return True
            else:
                dis = max(start[1], end[1])
                for line in self.walls[0][start[0]]:
                    if line[0] < dis < line[1]:
                        return False
                return True
        else:
            if start[0] == end[0]:
                return True
            else:
                dis = max(start[0], end[0])
                for line in self.walls[1][[start[1]]]:
                    if line[0] < dis < line[1]:
                        return False
                return True

class player(pygame.sprite.Sprite):
    def __init__(self, spt):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.topleft = spt
        self.speed = 5
    def update(self, direct):
        if direct == 0:
            self.rect.top -= self.speed
        elif direct == 1:
            self.rect.right += self.speed
        elif direct == 2:
            self.rect.bottom += self.speed
        elif direct == 3:
            self.rect.left -= self.speed

pygame.init()
screen = pygame.display.set_mode((MAZE_WITHDETH*BLOCK_SIZE,MAZE_HEIGHT*BLOCK_SIZE))
clock = pygame.time.Clock()

w = map2pos(maze, BLOCK_SIZE)
# walls = pygame.sprite.Group()
# for i in w:
#     walls.add(wall(BLOCK_SIZE, i))
m = Maze([800,600], [60,60], w)
p = player([31,31])
direct = -1
while True:
    screen.fill(WHITE)
    # colides = pygame.sprite.spritecollide(p,walls,False)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            # for c in colides:
            #     if p.rect.right == c.rect.left:
            #         direct = -1
            #         break
            direct = 1
        elif keys[K_UP]:
            # for c in colides:
            #     if p.rect.top == c.rect.bottom:
            #         direct = -1
            direct = 0
        elif keys[K_DOWN]:
            # for c in colides:
            #     if p.rect.bottom == c.rect.top:
            #         direct = -1
            direct = 2
        elif keys[K_LEFT]:
            # for c in colides:
            #     if p.rect.left == c.rect.right:
            #         direct = -1
            direct = 3 
        else:
            direct = -1

    

    # if not pygame.sprite.spritecollide(p, walls, False):
    p.update(direct)
    
    screen.blit(p.image, p.rect)
    walls.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

    