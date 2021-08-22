import pygame
from pygame.locals import *
import sys,random,math,os,platform
# GPU
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# 包装的Group
class Groups(pygame.sprite.Group):
    def __init__(self, **args):
        pygame.sprite.Group.__init__(**args)
    def draw(self, surface:pygame.Surface):
        for s in self.sprites():
            surface.blit(s.image, s.rect.topleft)

# 实体类,读取图片
class DObject(pygame.sprite.Sprite):
    def __init__(self, image_name, image_number, image_width, image_height):
        super(DObject, self).__init__()
        self.image_name = image_name
        self.image_number = image_number
        self.image_width = image_width
        self.image_height = image_height
        # 加载并转换图片
        self.images = []
        img = pygame.image.load(image_name).convert_alpha()
        for i in range(self.image_number):
            self.images.append(img.subsurface((i*image_width,0,image_width,image_height)).copy())

class Dino(DObject):
    def __init__(self, base, **args):
        super(Dino, self).__init__(**args)
        self.speed = -8 / 2
        self.du = 90
        self.h = 100
        self.jumping = False
        self.g = -1 * (self.speed/self.du)
        # self.t = math.sqrt((2*self.h)/self.g)/self.du
        self.t = 2
        self.base = base - self.image_height
        self.v = 0
        self.image = self.images[0]
        self.index = 0
        self.frame = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (40, self.base)
        

    def update(self):
        if self.jumping:
            # if self.rect.top < self.base:
            self.index = 0
            self.rect.top += int(self.v * self.t + 0.5 * self.g * (self.t**2))
            self.v += self.g * self.t
            # else:
            if not self.rect.top < self.base:
                self.rect.top = self.base
                self.v = 0
                self.jumping = False
        if self.index > self.image_number - 1:
            self.index = 0
        if self.frame > 9:
            self.image = self.images[self.index]
            self.index += 1
            self.frame = 0
        self.frame += 1
    
    def jump(self):
        if not self.rect.top < self.base:
            self.jumping = True
            self.v = self.speed
# 随机出现的树类
class Tree(DObject):
    def __init__(self, base, **args):
        super(Tree, self).__init__(**args)
        self.speed = 10/2
        self.base = base - self.image_height
        self.image = self.images[random.randint(0, self.image_number-1)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [800, self.base]
    
    def update(self):
        self.rect.left -= self.speed
        if self.rect.left < -20:
            self.kill()

class Cloud(DObject):
    def __init__(self, base, **args):
        super(Cloud, self).__init__(**args)
        self.speed = 10/4
        self.base = base - self.image_height - 100
        self.image = self.images[random.randint(0,self.image_number-1)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [800, self.base]
    def update(self):
        self.rect.left -= self.speed
        if self.rect.left < -20:
            self.kill()


# 颜色
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (122,122,122,128)
BASE = 400

fps = 60
# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
# 设置时钟
clock = pygame.time.Clock()
# 加载字体
font = pygame.font.SysFont('arial', 16)
score = 0 # 分数
run = True
last_tree = 0
background = pygame.Surface((800,600)).convert_alpha()
background.fill(GRAY)

di = Dino(BASE, image_name='kohi_kohi.png', image_number=5,image_width=58,image_height=90)

tree_group = pygame.sprite.Group()
cloud_group = Groups()
tree_group.add(Tree(BASE, image_name='kohi_tree.png',image_number=2,image_width=43,image_height=90))
cloud_group.add(Cloud(BASE, image_name='images/kohi_cloud.png',image_number=2,image_width=90,image_height=90))
# main loop
while run:
    # screen.fill(BLACK)
    screen.blit(background, (0,0))
    score_surface = font.render("Score:  " + str(score), True, BLACK)
    # ujump = True # 是否跳跃
    # 判断输入
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # ujump = False
                di.jump()
            if event.key == K_ESCAPE:
                sys.exit()
        elif event.type == QUIT:
            sys.exit()

    re = pygame.draw.rect(screen, BLACK, (0,BASE, 800, 10))
    # trees and cloud
    if len(tree_group.sprites()) <= 2 and last_tree > 60:
        if random.randint(1, 60) < 3:
            tree_group.add(Tree(BASE, image_name='kohi_tree.png',image_number=2,image_width=43,image_height=90))
            last_tree = 0
    if len(cloud_group.sprites()) < 1:
        cloud_group.add(Cloud(BASE, image_name='images/kohi_cloud.png',image_number=2,image_width=90,image_height=90))
    # 更新位置
    if not pygame.sprite.spritecollide(di, tree_group, False):
        tree_group.update()
        cloud_group.update()
        di.update()
        score += 10
        
    # 绘制
    cloud_group.draw(screen)
    tree_group.draw(screen)
    screen.blit(score_surface, (600,100))
    screen.blit(di.image, di.rect)
    last_tree += 1
    # 刷新
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(fps)
    