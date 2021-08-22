import pygame,renpy
from pygame.locals import *
import sys,random,math,os,platform
# GPU
# if platform.system() == 'Windows':
#     os.environ['SDL_VIDEODRIVER'] = 'windib'
# 恐龙类
class dino(pygame.sprite.Sprite):
    def __init__(self, base):
        super().__init__(self)
        self.speed = -6 / 2
        self.du = 90
        self.h = 100

        self.g = -1 * (self.speed/self.du)
        # self.t = math.sqrt((2*self.h)/self.g)/self.du
        self.t = 5
        self.base = base
        self.v = 0
        self.image = pygame.Surface((20, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (40, self.base)

    def update(self, ujump):
        if self.rect.top <self.base:
            ujump = True
        if ujump:
            self.rect.top += int(self.v * self.t + 0.5 * self.g * (self.t**2))
            self.v += self.g * self.t
            if not self.rect.top < self.base:
                self.rect.top = self.base
                self.v = 0
        else:
            self.v = self.speed
            self.rect.top += (self.v * self.t + 0.5 * self.g * (self.t**2))
            self.v += self.g * self.t
# 随机出现的树类
class tree(pygame.sprite.Sprite):
    def __init__(self, base):
        super().__init__(self)
        self.speed = 10/2

        self.image = pygame.Surface((20,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = [800, base-10]
        self.image.fill(GREEN)
    
    def update(self):
        self.rect.left -= self.speed
        if self.rect.left < -20:
            self.kill()

class Dino(renpy.Displayable):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (122,122,122)
    BASE = 360
    def __init__(self):
        self.score = 0
        self.last_tree = 0
        self.oldst = None
        self.ujump = True

        self.base_line = Solid(WHITE, xsize = 1280, ysize=10)
        self.di = dino(BASE)
        self.tree_group = pygame.sprite.Group()
        self.tree_group.add(tree(BASE))

    def render(self, width, heigh, st, at):
        if self.oldst == None:
            self.oldst = st
        dtime = st - self.oldst

        screen = renpy.Render(width, heigh)

        if len(self.tree_group.sprites()) <= 2 and self.last_tree > 30:
            if random.randint(1, 60) < 3:
                self.tree_group.add(tree(BASE))
                self.last_tree = 0
        # 更新位置
        if not pygame.sprite.spritecollide(self.di, self.tree_group, False):
            self.di.update(ujump)
            self.tree_group.update()
            self.score += 10

        screen.blit(self.base_line, (0,400))
        screen.blit(self.dino.image, self.dino.image.rect)
        self.tree_group.draw(screen)

        renpy.redraw(self, 0)
        return screen

    def event(self, ev, x, y , st):
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                self.ujump = False


# # 颜色
# BLACK = (0,0,0)
# WHITE = (255,255,255)
# GREEN = (122,122,122)
# BASE = 360

# fps = 60
# # 初始化
# screen = pygame.display.set_mode((800, 600))
# # 设置时钟
# clock = pygame.time.Clock()
# # 加载字体
# font = pygame.font.SysFont('arial', 16)
# score = 0 # 分数
# run = True
# last_tree = 0
# di = dino(BASE)
# tree_group = pygame.sprite.Group()
# tree_group.add(tree(BASE))

# # main loop
# while run:
#     score_surface = font.render("Score:  " + str(score), True, WHITE)
#     ujump = True # 是否跳跃
#     # 判断输入
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_SPACE:
#                 ujump = False
#             if event.key == K_ESCAPE:
#                 sys.exit()
#         elif event.type == QUIT:
#             sys.exit()

#     re = pygame.draw.rect(screen, WHITE, (0,400, 800, 10))

#     if len(tree_group.sprites()) <= 2 and last_tree > 30:
#         if random.randint(1, 60) < 3:
#             tree_group.add(tree(BASE))
#             last_tree = 0
#     # 更新位置
#     if not pygame.sprite.spritecollide(di, tree_group, False):
#         di.update(ujump)
#         tree_group.update()
#         score += 10
#     else:
#         pass
#     # 绘制
#     screen.blit(di.image, di.rect)
#     tree_group.draw(screen)
#     screen.blit(score_surface, (600,100))
#     last_tree += 1
#     # 刷新
#     pygame.display.update()
#     screen.fill(BLACK)
#     clock.tick(fps)
    