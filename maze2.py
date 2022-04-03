from enum import Enum,auto
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
RED = (255, 0 , 0)

FPS = 60

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()
    NONE = auto()

class Maze(pygame.sprite.Sprite):
    def __init__(self, maze_withdeth:int, maze_height:int, cell_size:int):
        self.maze_withdeth = maze_withdeth
        self.maze_height = maze_height
        self.t_cell_w = 2*maze_withdeth-1
        self.t_cell_h = 2*maze_height-1
        self.cell_size = cell_size
        self.i_withdeth = self.t_cell_w * cell_size
        self.i_height = self.t_cell_h * cell_size
        self.end_point = (self.cell_size*(self.t_cell_w - 0.5), self.cell_size*(self.t_cell_h - 0.5))
        self.colide_cell = [[0,0],[0,0]]

        self.map = self.wall2map(self.maze_generate(self.maze_withdeth, self.maze_height))
        self.image = self.show_map()

    # Randomized Prim's algorithm
    def maze_generate(self, maze_withdeth, maze_height):
        """使用Randomized Prim算法生成迷宫地图数据，walls中walls[0]保存水平方向上的墙，walls[1]保存竖直方向上的墙"""
        # return cell on the both sides of the wall
        def vertical_wall_cell(pos):
            return (pos + int(pos/(maze_withdeth-1)), pos + int(pos/(maze_withdeth-1)) + 1)
        def horizontal_wall_cell(pos):
            return (pos, pos + maze_withdeth)

        n_cell = maze_withdeth*maze_height
        v_walls = (maze_withdeth-1)*maze_height - 1
        h_walls = maze_withdeth*(maze_height-1) - 1

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

    def wall2map(self, wall):
        """将原始数据转换为（2w-1，2h-1）的list，方便后续使用。映射过程中将墙扩展为1格。其中1代表该格有墙"""
        map = [[0 for i in range(self.maze_withdeth * 2 - 1)] for j in range(self.maze_height * 2 - 1)] # [2w-1, 2h-1]
        # horizontal
        for i in range(len(wall[0])):
            map[(i//(self.maze_withdeth-1))*2][(i%(self.maze_withdeth-1))*2+1] = wall[0][i]
        # vertical
        for i in range(len(wall[1])):
            map[(i//(self.maze_withdeth))*2+1][(i%(self.maze_withdeth))*2] = wall[1][i]
        # gap
        for i in range((self.maze_withdeth-1) * (self.maze_height-1)):
            map[(i//(self.maze_withdeth-1))*2+1][(i%(self.maze_withdeth-1))*2+1] = 1
        return map

    def show_map(self):
        """将map中的数据绘制在image上"""
        image = pygame.Surface((self.i_withdeth,self.i_height))
        for i in range(self.t_cell_h):
            for j in range(self.t_cell_w):
                if self.map[i][j]:
                    pygame.draw.rect(image, BLACK, (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(image, WHITE, (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
        # draw a circle as end flag
        pygame.draw.circle(image, RED, self.end_point, 0.5*self.cell_size)
        return image
            
    def colide(self, r:pygame.Rect) -> bool:
        left = r.left//self.cell_size
        top = r.top//self.cell_size
        right = r.right//self.cell_size
        bottom = r.bottom//self.cell_size
        self.colide_cell = [[left*self.cell_size, top*self.cell_size], [right*self.cell_size, bottom*self.cell_size]]
        # detect if the object being in the surface arange
        if self._is_point_in_box(r.topright) and self._is_point_in_box(r.bottomleft):
            # if topleft and bottomright not in the same cell
            if left != right or top != bottom:
                return self._if_map_at(left, top) or self._if_map_at(right, bottom) or self._if_map_at(left, bottom) or self._if_map_at(right, top)
        else:
            return True

    def _is_point_in_box(self, point:pygame.Rect.bottomleft) -> bool:
        return point[0] <= self.i_withdeth and point[1] <= self.i_height and point[0] >= 0 and point[1] >= 0

    def _if_map_at(self, x, y) -> bool:
        # map的x，y坐标对调了
        if x < self.t_cell_w and y < self.t_cell_h:
            return self.map[y][x]

    def update(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self,size, speed, end_point:tuple[int, int]):
        self.size = size
        self.image = pygame.Surface((size,size))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.speed = speed
        self.direction = Direction.NONE
        self.old_rect = [0,0]
        self.end_point = end_point
        self.end_flag = False

    def update(self):
        if self.direction == Direction.UP:
            self.old_rect = self.rect.topleft
            self.rect.top -= self.speed
        elif self.direction == Direction.RIGHT:
            self.old_rect = self.rect.topleft
            self.rect.right += self.speed
        elif self.direction == Direction.DOWN:
            self.old_rect = self.rect.topleft
            self.rect.bottom += self.speed
        elif self.direction == Direction.LEFT:
            self.old_rect = self.rect.topleft
            self.rect.left -= self.speed
        if self.end_point[0] - self.rect.left < 5 and self.end_point[1] - self.rect.top < 5:
            self.end_flag = True
    
    def set_direction(self, direction:Direction = Direction.NONE):
        self.direction = direction
    
    def reset_pos(self, colide_cell):
        if self.rect.left - self.old_rect[0] != 0:
            if self.old_rect[0] > colide_cell[0][0] and self.old_rect[0] < colide_cell[1][0]:
                self.rect.right = colide_cell[1][0] - 1
            else:
                self.rect.left = colide_cell[1][0] + 1
        else:
            if self.old_rect[1] > colide_cell[0][1] and self.old_rect[1] <colide_cell[1][1]:
                self.rect.bottom = colide_cell[1][1] - 1
            else:
                self.rect.top = colide_cell[1][1] + 1

    def is_end(self):
        return self.end_flag

m = Maze(12,12,30)
p = Player(10, 5, m.end_point)


pygame.init()
screen = pygame.display.set_mode((m.i_withdeth,m.i_height))
clock = pygame.time.Clock()
# background = pygame.Surface((800,600)).convert_alpha()
# background.fill(GRAY)
while True:
    # screen.fill(WHITE)
    # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            p.set_direction(Direction.RIGHT)
        elif keys[K_UP]:
            p.set_direction(Direction.UP)
        elif keys[K_DOWN]:
            p.set_direction(Direction.DOWN)
        elif keys[K_LEFT]:
            p.set_direction(Direction.LEFT) 
        else:
            p.set_direction()

    # p.set_direction(Direction.RIGHT)

#     # if not pygame.sprite.spritecollide(p, walls, False):
    p.update()
    b = m.colide(p.rect)
    if b:
        p.reset_pos(m.colide_cell)
    if p.is_end():
        print("You have arrived the end.")
        sys.exit()
    # p.set_direction(Direction.DOWN)
    
    screen.blit(m.image, (0,0))
    screen.blit(p.image, p.rect)
    pygame.display.update()
    clock.tick(FPS)