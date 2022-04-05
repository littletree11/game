init 0 python:
    import pygame
    # from pygame.locals import *
    import sys,random,math,os,platform
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    BLUE = (78, 213, 254)
    WHITE = (255, 255, 255)
    BASE = 400
    class Groups(pygame.sprite.Group):
        def __init__(self, **args):
            super(Groups, self).__init__()
        def draw(self, surface):
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
            file_tmp = renpy.file(image_name)
            img = pygame.image.load(file_tmp).convert_alpha()
            for i in range(self.image_number):
                self.images.append(img.subsurface((i*image_width,0,image_width,image_height)).copy())

    class Dino(DObject):
        def __init__(self, base, **args):
            super(Dino, self).__init__(**args)
            self.speed = -8
            self.du = 180
            self.h = 100
            self.jumping = False
            # self.g = -1 * (self.speed/self.du)
            self.g = 0.1
            # self.t = math.sqrt((2*self.h)/self.g)/self.du
            self.t = 3
            self.base = base - self.image_height
            self.v = 0
            self.image = self.images[0]
            self.index = 0
            self.frame = 0
            self.rect = self.image.get_rect()
            self.rect.topleft = (80, self.base)

        def update(self,dtime):
            t = self.t
            if self.jumping:
                # if self.rect.top < self.base:
                self.index = 0
                self.rect.top += int(self.v * t + 0.5 * self.g * (t**2))
                self.v += self.g * t
                # else:
                if self.rect.top > self.base:
                    self.rect.top = self.base
                    self.v = 0
                    self.jumping = False
            if self.index > self.image_number - 1:
                self.index = 0
            if self.frame > 5:
                self.image = self.images[self.index]
                self.index += 1
                self.frame = 0
            self.frame += 1
        
        def jump(self):
            if not self.jumping:
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
            self.rect.topleft = [1280, self.base]
        
        def update(self):
            self.rect.left -= self.speed
            if self.rect.right < -20:
                self.kill()

    class Cloud(DObject):
        def __init__(self, base, **args):
            super(Cloud, self).__init__(**args)
            self.speed = 2
            self.base = base - self.image_height - 100
            self.image = self.images[random.randint(0,self.image_number-1)]
            self.rect = self.image.get_rect()
            self.rect.topleft = [1280, self.base]
        def update(self):
            self.rect.left -= self.speed
            if self.rect.right < -20:
                self.kill()


    class MiniDino(renpy.Displayable):
        def __init__(self):
            super(MiniDino, self).__init__()
            self.score = 0
            self.last_tree = 0
            self.oldst = None
            # self.fonts = pygame.font.SysFont('arial', 16)
            # self.base_line = Solid(WHITE, xsize = 1280, ysize=10)
            # self.base_line = pygame.Surface((1280,10))
            self.base_line = renpy.Render(1280,10)
            self.base_line.canvas().rect(WHITE, (0,0,1280,10))
            self.di = Dino(BASE,image_name='images/kohi_kohi.png', image_number=5,image_width=58,image_height=90)
            self.tree_group = Groups()
            self.tree_group.add(Tree(BASE,image_name='images/kohi_tree.png',image_number=2,image_width=43,image_height=90))
            self.cloud_group = Groups()
            self.cloud_group.add(Cloud(BASE, image_name='images/kohi_cloud.png',image_number=2,image_width=90,image_height=90))
            self.finish = False

        def render(self, width, heigh, st, at):
            # score_face = self.fonts.render('Score:'+str(self.score), True, BLACK)
            score = renpy.render(Text('Score:'+str(self.score)), 100,300,0,0)
            if self.oldst == None:
                self.oldst = st
                dtime = 0.01
            else:
                dtime = st - self.oldst

            screen = renpy.Render(width, heigh)
            if len(self.tree_group.sprites()) <= 2 and self.last_tree > 60:
                if random.randint(1, 60) < 3:
                    self.tree_group.add(Tree(BASE,image_name='images/kohi_tree.png',image_number=2,image_width=43,image_height=90))
                    self.last_tree = 0
            if len(self.cloud_group.sprites()) < 3:
                self.cloud_group.add(Cloud(BASE, image_name='images/kohi_cloud.png',image_number=2,image_width=90,image_height=90))
            # 更新位置
            if not pygame.sprite.spritecollide(self.di, self.tree_group, False):
                self.di.update(dtime)
                self.tree_group.update()
                self.cloud_group.update()
                self.score += 10
            else:
                self.finish = True

            self.tree_group.draw(screen)
            self.cloud_group.draw(screen)
            screen.blit(score, (1000,100))
            screen.blit(self.base_line, (0,BASE))
            screen.blit(self.di.image, self.di.rect.topleft)
            
            self.last_tree += 1

            renpy.redraw(self, 0)
            return screen

        def event(self, ev, x, y , st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    self.di.jump()
            if self.finish:
                return self.score


screen dino():
    # default d = MiniDino()
    # add d
    add MiniDino()