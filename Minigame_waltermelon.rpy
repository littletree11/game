# init 3 python:
#     # import pymunk.pygame_util
#     import pymunk

#     def get_file(self, path):
#             return renpy.file(path)

#     #水果类别
#     class PuTao():
#         def __init__(self):
#             self.mass = 4000  # 质量
#             self.radius = 20  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 100000
#             self.circle.collision_type = 1
#             self.high=0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/01.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class YingTao:
#         def __init__(self):
#             self.mass = 9000  # 质量
#             self.radius = 30  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 2
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/02.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class Hanamaru:
#         def __init__(self):
#             self.mass = 17640  # 质量
#             self.radius = 42  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 3
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/03.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class NingMeng:
#         def __init__(self):
#             self.mass = 21160  # 质量
#             self.radius = 46  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type=4
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/04.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class MiHouTao:
#         def __init__(self):
#             self.mass = 33640  # 质量
#             self.radius = 58  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 5
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/05.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class Tomato:
#         def __init__(self):
#             self.mass = 49000  # 质量
#             self.radius = 70  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 6
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/06.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class MoMo:
#         def __init__(self):
#             self.mass = 54760  # 质量
#             self.radius = 74  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 7
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/07.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class BoLuo:
#         def __init__(self):
#             self.mass = 100000  # 质量
#             self.radius = 100  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 8
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/08.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class YeZi:
#         def __init__(self):
#             self.mass = 116640  # 质量
#             self.radius = 108  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 9
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/09.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class BanXiGua:
#         def __init__(self):
#             self.mass = 144000  # 质量
#             self.radius = 120  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 10
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/10.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
#     class XiGua:
#         def __init__(self):
#             self.mass = 243360  # 质量
#             self.radius = 156  # 半径
#             self.body = pymunk.Body(self.mass, moment=10)
#             self.circle = pymunk.Circle(self.body, self.radius)
#             self.circle.elasticity = 0.15
#             self.circle.friction = 0.9
#             self.circle.collision_type = 11
#             self.high = 0
#         def High(self):
#             return self.high
#         def Higher(self):
#             self.high+=1
#         def Circle(self):
#             return self.radius
#         def Draw(self):
#             self.image = pygame.image.load(get_file('images/watermelon/11.png'))
#             self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
#             return self.image
    

#     #分数计算
#     class Score():
#         def __init__(self):
#             self.score=0

#     #碰撞检测
#     def coll_begin (arbiter,space,data):
#         Shape_0=arbiter.shapes[0]
#         Shape_1 = arbiter.shapes[1]
#         i=arbiter.shapes[0].collision_type
#         x1, y1 = arbiter.shapes[0].body.position
#         x2, y2 = arbiter.shapes[1].body.position
#         if y1 > y2:
#             space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
#             space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
#             for fruit in Fruit:
#                 if fruit.body.position==arbiter.shapes[0].body.position:
#                     Fruit.remove(fruit)
#             for fruit in Fruit:
#                 if fruit.body.position==arbiter.shapes[1].body.position:
#                     Fruit.remove(fruit)
#             Creat_Fruit(x1,y1,i)
#             if i!=10:
#                 Score_Final.score+=i
#             elif i==10:
#                 Score_Final.score+=i
#                 Score_Final.score+=100
#         if y1 < y2:
#             space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
#             space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
#             for fruit in Fruit:
#                 if fruit.body.position==arbiter.shapes[0].body.position:
#                     Fruit.remove(fruit)
#             for fruit in Fruit:
#                 if fruit.body.position==arbiter.shapes[1].body.position:
#                     Fruit.remove(fruit)
#             Creat_Fruit(x2, y2, i)
#             if i!=10:
#                 Score_Final.score+=i
#             elif i==10:
#                 Score_Final.score+=i
#                 Score_Final.score+=100
#         if y1 == y2:
#             if x1 < x2:
#                 space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
#                 space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
#                 for fruit in Fruit:
#                     if fruit.body.position == arbiter.shapes[0].body.position:
#                         Fruit.remove(fruit)
#                 for fruit in Fruit:
#                     if fruit.body.position == arbiter.shapes[1].body.position:
#                         Fruit.remove(fruit)
#                 Creat_Fruit(x2, y2, i)
#                 if i != 10:
#                     Score_Final.score += i
#                 elif i == 10:
#                     Score_Final.score += i
#                     Score_Final.score += 100
    
#     #随机计算
#     class Random(object):
#         def __init__(self):
#             self.rana=random.randint(1,10)
#         def random(self):
#             if 1 <= self.rana <= 2:
#                 return 1
#             if 3 <= self.rana <= 4:
#                 return 2
#             if 5 <= self.rana <= 7:
#                 return 3
#             if self.rana == 8:
#                 return 4
#             if 9 <= self.rana <= 10:
#                 return 5

#     class MinigaeWatermelon(renpy.Displayable):
#         def __init__(self):
#             super(MinigaeWatermelon, self).__init__()
#             self.Fruit=[]
#             self.putao=PuTao()
#             self.yingtao=YingTao()
#             self.hanamaru=Hanamaru()
#             self.ningmeng=NingMeng()
#             self.mihoutao=MiHouTao()
#             self.SCREEN_WIDTH=400
#             self.SCREEN_HEIGHT=600

#             #背景
#             self.background=pygame.image.load(get_file("images/watermelon/background.png"))

#             #鼠标
#             self.Number_Mouse = 0

#             #pymunk空间设置
#             self.space = pymunk.Space()

#             #pymunk重力设置
#             self.space.gravity = 0, 900

#             #生成地面以及墙壁
#             ground_0 = self.space.static_body
#             segment_0= pymunk.Segment(ground_0, (0,SCREEN_HEIGHT), (SCREEN_WIDTH,SCREEN_HEIGHT), 1)
#             segment_1=pymunk.Segment(ground_0,(-50,0),(-50,600),50)
#             segemt_2=pymunk.Segment(ground_0,(450,0),(450,600),50)
#             segment_0.elasticity = 1
#             segment_0.friction=100000
#             self.space.add(segment_0,segment_1,segemt_2)

#             for i in range(1,11):
#                 handler=self.space.add_collision_handler(i,i)
#                 handler.post_solve=coll_begin

#             self.Score_Final=Score()
#             self.Mouse_Nothing=1
#             self.Mouse_Count=0

#             #延迟
#             self.Delay=0
#             self.Falldown=0
#             self.x=0

#             self.FPS = 60
#             self.interval = 1.0/self.FPS
#             self.playing = True
        
#         def render(self, width, heigh, st, at):
#             screen = renpy.Render(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

#             # 背景
#             screen.blit(self.background, (0, 0))
#             #分数
#             # Text_Show = Text.render('score: {}'.format(str(Score_Final.score)), 1, (0, 0, 0))
#             # screen.blit(Text_Show, (300, 30))
#             Text_Show = Text('score: {}'.format(str(self.Score_Final.score)))
#             screen.place(Text_Show, (300, 30))
#             # 死线
#             # self.DrawLine(background)
#             self.DrawLine(screen)

#             #绘制水果
#             for f in self.Fruit:
#                 screen.blit(f.Draw(),(f.body.position.x-f.Circle(),f.body.position.y-f.Circle()))

#             #游戏失败检测
#             for fruit in self.Fruit:
#                 if fruit.body.position.y<=100:
#                     fruit.Higher()
#                     if fruit.High()>=100:
#                         self.playing = False
#             #下落延迟检测
#             if self.Falldown==1:
#                 self.Delay += 1
#                 if self.Delay>=120:
#                     self.Falldown=0
#                     self.Delay=0
#             # 更新
#             self.space.step(0.01)

#             renpy.redraw(self, self.interval)
#             return screen

#         def event(self, ev, x, y , st):
#             # 鼠标
#             Mouse_X = x
#             Mouse_Press = pygame.mouse.get_pressed()

#             #小球位置
#             if self.Mouse_Count == 0:
#                 b=Random()
#                 self.Mouse_Count = 1
#             if 1 <= self.Mouse_Nothing <= 3 and self.Falldown==0:
#                 screen.blit(putao.Draw(), (Mouse_X - 20, 30))
#             if self.Mouse_Nothing == 4 and self.Falldown==0:
#                 screen.blit(yingtao.Draw(), (Mouse_X - 30, 20))
#             if self.Mouse_Nothing == 5 and self.Falldown==0:
#                 screen.blit(hanamaru.Draw(), (Mouse_X - 42, 8))
#             if self.Mouse_Nothing > 5 and self.Falldown==0:
#                 if b.random() == 1:
#                     screen.blit(putao.Draw(), (Mouse_X - 20, 30))
#                 if b.random() == 2:
#                     screen.blit(yingtao.Draw(), (Mouse_X - 30, 20))
#                 if b.random() == 3:
#                     screen.blit(hanamaru.Draw(), (Mouse_X - 42, 8))
#                 if b.random() == 4:
#                     screen.blit(ningmeng.Draw(), (Mouse_X - 46, 4))
#                 if b.random() == 5:
#                     screen.blit(mihoutao.Draw(), (Mouse_X - 58, -8))

#             if Mouse_Press[0]==1:
#                 if self.Number_Mouse==0 and self.Falldown==0:
#                         self.Number_Mouse=1
#                         self.Mouse_Count = 0
#                         self.Falldown=1
#                         Mouse_Sure = Mouse_X
#                         if self.Mouse_Nothing<=3:
#                             Creat_Fruit(Mouse_Sure,50,0,1)
#                         elif self.Mouse_Nothing==4:
#                             Creat_Fruit(Mouse_Sure,50,0,2)
#                         elif self.Mouse_Nothing==5:
#                             Creat_Fruit(Mouse_Sure, 50, 0, 3)
#                         else:
#                             Creat_Fruit(Mouse_Sure,50,0,b.random())
#                         self.Mouse_Nothing +=1
#             #鼠标抬起
#             if ev.type==pygame.MOUSEBUTTONUP:
#                 self.Number_Mouse=0
#             if not self.playing:
#                 return self.Score_Final.score

#         # 生成水果
#         def Creat_Fruit(x,y=50,i=0,a=0):
#             if i==0:
#                 if a == 1:
#                     putao = PuTao()
#                     putao.body.position = x, 50
#                     self.space.add(putao.body, putao.circle)
#                     self.Fruit.append(putao)
#                 if a == 2:
#                     yingtao = YingTao()
#                     yingtao.body.position = x, 50
#                     self.space.add(yingtao.body, yingtao.circle)
#                     self.Fruit.append(yingtao)
#                 if a == 3:
#                     hanamaru = Hanamaru()
#                     hanamaru.body.position = x, 50
#                     self.space.add(hanamaru.body, hanamaru.circle)
#                     self.Fruit.append(hanamaru)
#                 if a == 4:
#                     ningmeng = NingMeng()
#                     ningmeng.body.position = x, 50
#                     self.space.add(ningmeng.body, ningmeng.circle)
#                     self.Fruit.append(ningmeng)
#                 if a == 5:
#                     mihoutao = MiHouTao()
#                     mihoutao.body.position = x, 50
#                     self.space.add(mihoutao.body, mihoutao.circle)
#                     self.Fruit.append(mihoutao)
#             if i==1:
#                 yingtao = YingTao()
#                 yingtao.body.position = x, y
#                 self.space.add(yingtao.body, yingtao.circle)
#                 self.Fruit.append(yingtao)
#             if i==2:
#                 hanamaru = Hanamaru()
#                 hanamaru.body.position = x, y
#                 self.space.add(hanamaru.body, hanamaru.circle)
#                 self.Fruit.append(hanamaru)
#             if i==3:
#                 ningmeng = NingMeng()
#                 ningmeng.body.position = x, y
#                 self.space.add(ningmeng.body, ningmeng.circle)
#                 self.Fruit.append(ningmeng)
#             if i==4:
#                 mihoutao = MiHouTao()
#                 mihoutao.body.position = x, y
#                 self.space.add(mihoutao.body, mihoutao.circle)
#                 self.Fruit.append(mihoutao)
#             if i==5:
#                 tomato = Tomato()
#                 tomato.body.position = x, y
#                 self.space.add(tomato.body, tomato.circle)
#                 self.Fruit.append(tomato)
#             if i==6:
#                 momo = MoMo()
#                 momo.body.position = x, y
#                 self.space.add(momo.body, momo.circle)
#                 self.Fruit.append(momo)
#             if i==7:
#                 boluo = BoLuo()
#                 boluo.body.position = x, y
#                 self.space.add(boluo.body, boluo.circle)
#                 self.Fruit.append(boluo)
#             if i==8:
#                 yezi = YeZi()
#                 yezi.body.position = x, y
#                 self.space.add(yezi.body, yezi.circle)
#                 self.Fruit.append(yezi)
#             if i==9:
#                 banxigua = BanXiGua()
#                 banxigua.body.position = x, y
#                 self.space.add(banxigua.body, banxigua.circle)
#                 self.Fruit.append(banxigua)
#             if i==10:
#                 xigua = XiGua()
#                 xigua.body.position = x, y
#                 self.space.add(xigua.body, xigua.circle)
#                 self.Fruit.append(xigua)
#             #死线
#         def DrawLine(self, screen):
#             LineColcor=(0,255,255)
#             Line_Start =(0,100)
#             Line_End=(720,100)
#             Line_Width=3
#             screen.canvas().line(LineColcor,Line_Start,Line_End,Line_Width)

# screen watermelon():
#     add MinigaeWatermelon()