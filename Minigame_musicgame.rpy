init 2 python:
    # 状态标志，renpy因为未知原因无法使用enum
    class Status(object):
        intro = 1
        snew = 2
        stop = 3
        main = 4
        gameover = 5

    class Button:
        def __init__(self, x, y, width, height, fg, bg, content, fontsize):
            self.able = True
            # self.font = pygame.font.Font("浪漫雅圆.ttf", fontsize)
            self.content = content
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.fg = fg
            self.bg = bg
            self.image = renpy.Render(self.width, self.height)
            self.image.canvas().rect(self.bg, (0,0, self.width, self.height))
            self.rect = pygame.Rect(x,y,self.width, self.height)
            # self.rect.x = self.x
            # self.rect.y = self.y
            # self.text = self.font.render(self.content, True, self.fg)
            self.text = Text(self.content, size=fontsize, color=self.fg)
            # self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
            # self.text_rect = self.text.canvas().get_surface()
            self.text_rect = pygame.Rect(0,0,self.width, self.height)
            self.text_rect.center = (self.width / 2, self.height / 2)
            # self.image.place(self.text, self.text_rect.left, self.text_rect.top)
            self.image.place(self.text, 15, 0)

        def is_pressed(self, pos, pressed):
            if self.able:
                if self.rect.collidepoint(pos):
                    if pressed[0]:
                        return True
                    return False
                return False
    class FirstLine():
        def __init__(self, game):
            self.x = 200
            self.y = 0
            self.life = True
            self.game = game

        def PostX(self):
            return self.x

        def PostY(self):
            return self.y

        def Draw(self):
            return self.game.block
    class SecondLine(FirstLine):
        def __init__(self, game):
            self.x = 476
            self.y = 0
            self.life = True
            self.game = game
    class ThirdLine(FirstLine):
        def __init__(self, game):
            self.x = 754
            self.y = 0
            self.life = True
            self.game = game
    class FourthLine(FirstLine):
        def __init__(self, game):
            self.x = 1030
            self.y = 0
            self.life = True
            self.game = game
    
    class MinigameMusicgame(renpy.Displayable):
        def __init__(self):
            super(MinigameMusicgame, self).__init__()
            self.SCREEN_WIDTH = 1280
            self.SCREEN_HEIGHT = 720
            self.clock = pygame.time.Clock()
            self.running = True
            self.thetime = 0
            self.theline = []
            self.a=0
            self.oldtime = 0
            self.realfirst = []
            self.realsecond = []
            self.realthird = []
            self.realfourth = []
            self.realblocks = []
            self.score = 0
            self.comble = 0
            self.background = pygame.image.load(self.get_file('images/music_background.png')).convert_alpha()
            self.background1 = pygame.image.load(self.get_file('images/music_background1.png')).convert_alpha()
            self.block = pygame.image.load(self.get_file('images/music_1.png')).convert_alpha()
            self.block = pygame.transform.smoothscale(self.block, (50, 50))
            self.stop1 = pygame.image.load(self.get_file('images/music_1-1.png')).convert_alpha()
            self.stop2 = pygame.image.load(self.get_file('images/music_2-1.png')).convert_alpha()
            self.stop3 = pygame.image.load(self.get_file('images/music_3-1.png')).convert_alpha()

            self.status = Status.intro
            self.play_button = Button(10, 50, 100, 50, WHITE, BLACK, "play", 40)
            self.stop_time = 1
            self.playing = False
            self.FPS = 50
            self.interval = 1.0/self.FPS

        def render(self, width, heigh, st, at):
            screen = renpy.Render(width, heigh)
            if self.status == Status.intro:
                self.intro(screen)
            elif self.status == Status.snew:
                self.new()
            elif self.status == Status.stop:
                self.stop(screen)
            elif self.status == Status.main:
                self.main(screen, st)
            elif self.status == Status.gameover:
                self.gameover(screen)

            if st - self.oldtime > self.interval:
                gap = 2*self.interval - (st - self.oldtime)
            else:
                gap = self.interval
            # print(gap)
            # print("interval: " + str(self.interval))
            renpy.redraw(self, gap)
            self.oldtime = st
            return screen

        def event(self, ev, x, y , st):
            if self.status == Status.intro:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = (x,y)
                    mouse_pressed = pygame.mouse.get_pressed()
                    if self.play_button.is_pressed(mouse_pos, mouse_pressed):
                        self.status = Status.snew
            elif self.status == Status.main:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_a:
                        if self.realfirst:
                            if 576 + 30 >= self.realfirst[0].PostY() >= 576 - 30:
                                self.score += 100
                                self.comble += 1
                            else:
                                self.score += 30
                                self.comble = 0
                            self.realfirst.remove(self.realfirst[0])
                            self.realblocks = self.realfirst + self.realsecond + self.realthird + self.realfourth
                    if ev.key == pygame.K_d:
                        if self.realsecond:
                            if 576 + 30 >= self.realsecond[0].PostY() >= 576 - 30:
                                self.score += 100
                                self.comble += 1
                            else:
                                self.score += 30
                                self.comble = 0
                            self.realsecond.remove(self.realsecond[0])
                            self.realblocks = self.realfirst + self.realsecond + self.realthird + self.realfourth
                    if ev.key == pygame.K_k:
                        if self.realthird:
                            if 576 + 30 >= self.realthird[0].PostY() >= 576 - 30:
                                self.score += 100
                                self.comble += 1
                            else:
                                self.score += 30
                                self.comble = 0
                            self.realthird.remove(self.realthird[0])
                            self.realblocks = self.realfirst + self.realsecond + self.realthird + self.realfourth
                    if ev.key == pygame.K_l:
                        if self.realfourth:
                            if 576 + 30 >= self.realfourth[0].PostY() >= 576 - 30:
                                self.score += 100
                                self.comble += 1
                            else:
                                self.score += 30
                                self.comble = 0
                            self.realfourth.remove(self.realfourth[0])
                            self.realblocks = self.realfirst + self.realsecond + self.realthird + self.realfourth
            elif self.status == Status.gameover:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = (x,y)
                    mouse_pressed = pygame.mouse.get_pressed()
                    if self.restart_button.is_pressed(mouse_pos, mouse_pressed):
                        # self.status = Status.snew
                        return self.score

        def draw_text(self, text, colour, x, y, fontsize, screen):
            # font = pygame.font.Font("浪漫雅圆.ttf", fontsize)
            # img = font.render(text, True, colour)
            img = Text(text)
            screen.place(img, x, y)
        def new(self):
            # self.playing = True
            self.thetime=0
            self.realblocks.clear()
            self.realfirst.clear()
            self.realsecond.clear()
            self.realthird.clear()
            self.realfourth.clear()
            self.theline = [[100, 1, 0, 0, 0], [119, 0, 0, 1, 0], [137, 0, 0, 0, 1], [155, 0, 1, 0, 0], [174, 1, 0, 0, 0],
            [192, 0, 1, 0, 0], [210, 1, 0, 0, 0], [247, 0, 1, 0, 0], [265, 0, 0, 1, 0], [283, 0, 0, 0, 1],
            [320, 0, 1, 0, 0], [338, 1, 0, 0, 0], [356, 0, 1, 0, 0], [393, 1, 0, 0, 0], [411, 0, 1, 0, 0],
            [429, 1, 0, 0, 0], [466, 0, 1, 0, 0], [484, 0, 0, 0, 1], [502, 0, 0, 1, 0], [539, 1, 0, 0, 0],
            [557, 0, 1, 0, 0], [576, 1, 0, 0, 0], [594, 0, 1, 0, 0], [621, 0, 0, 0, 1], [649, 1, 0, 0, 0],
            [685, 0, 0, 0, 1], [703, 0, 0, 1, 0], [740, 0, 0, 1, 0], [758, 0, 0, 1, 0], [776, 0, 1, 0, 0],
            [831, 0, 1, 0, 0], [850, 1, 0, 0, 0], [904, 1, 0, 0, 0], [923, 0, 0, 0, 1], [977, 0, 0, 1, 0],
            [996, 0, 0, 0, 1], [1050, 1, 0, 0, 0], [1069, 0, 1, 0, 0], [1124, 0, 0, 0, 1], [1142, 0, 1, 0, 0],
            [1178, 0, 0, 0, 1], [1215, 0, 0, 0, 1], [1244, 0, 1, 0, 0], [1262, 1, 0, 0, 0], [1281, 0, 1, 0, 0],
            [1308, 1, 0, 0, 0], [1326, 0, 0, 1, 0], [1344, 0, 1, 0, 0], [1363, 0, 1, 0, 0], [1381, 0, 0, 1, 0],
            [1418, 1, 0, 0, 0], [1454, 0, 0, 0, 1], [1472, 0, 1, 0, 0], [1491, 1, 0, 0, 0], [1509, 0, 0, 1, 0],
            [1527, 0, 1, 0, 0], [1564, 0, 0, 0, 1], [1600, 0, 1, 0, 0], [1618, 0, 0, 0, 1], [1637, 1, 0, 0, 0],
            [1655, 0, 1, 0, 0], [1673, 0, 1, 0, 0], [1710, 0, 1, 0, 0], [1728, 1, 0, 0, 0], [1756, 0, 0, 1, 0],
            [1774, 0, 0, 0, 1], [1792, 0, 0, 1, 0], [1810, 0, 0, 0, 1], [1829, 0, 1, 0, 0], [1847, 1, 0, 0, 0],
            [1874, 1, 0, 0, 0], [1911, 0, 0, 1, 0], [1929, 1, 0, 0, 0], [1947, 0, 1, 0, 0], [1984, 0, 0, 1, 0],
            [2002, 0, 0, 1, 0], [2020, 0, 0, 0, 1], [2057, 1, 0, 0, 0], [2075, 0, 1, 0, 0], [2094, 0, 1, 0, 0],
            [2148, 0, 0, 1, 0], [2167, 0, 1, 0, 0], [2221, 0, 1, 0, 0], [2240, 1, 0, 0, 0], [2258, 1, 0, 0, 0],
            [2294, 0, 0, 1, 0], [2313, 0, 0, 0, 1], [2349, 0, 1, 0, 0], [2368, 1, 0, 0, 0], [2395, 0, 0, 0, 1],
            [2422, 0, 0, 0, 1], [2442, 0, 0, 1, 0], [2460, 1, 0, 0, 0], [2479, 0, 0, 0, 1], [2497, 0, 0, 0, 1],
            [2515, 0, 0, 1, 0], [2533, 1, 0, 0, 0], [2552, 0, 0, 0, 1], [2579, 0, 1, 0, 0], [2606, 0, 0, 0, 1],
            [2625, 0, 1, 0, 0], [2643, 0, 1, 0, 0], [2661, 1, 0, 0, 0], [2680, 0, 0, 0, 1], [2698, 0, 1, 0, 0],
            [2725, 0, 0, 1, 0], [2753, 1, 0, 0, 0], [2771, 0, 0, 1, 0], [2789, 0, 1, 0, 0], [2807, 0, 0, 0, 1],
            [2826, 1, 0, 0, 0], [2844, 0, 0, 1, 0], [2871, 1, 0, 0, 0], [2917, 1, 0, 0, 0], [2935, 1, 0, 0, 0],
            [2954, 0, 1, 0, 0], [2972, 0, 0, 0, 1], [2990, 1, 0, 0, 0], [3008, 0, 1, 0, 0], [3027, 0, 0, 1, 0],
            [3045, 1, 0, 0, 0], [3063, 0, 0, 1, 0], [3082, 0, 0, 1, 0], [3100, 0, 1, 0, 0], [3118, 1, 0, 0, 0],
            [3136, 0, 0, 1, 0], [3164, 0, 1, 0, 0], [3191, 0, 0, 0, 1], [3210, 1, 0, 0, 0], [3228, 1, 0, 0, 0],
            [3246, 0, 1, 0, 0], [3264, 0, 0, 1, 0], [3283, 1, 0, 0, 0], [3310, 0, 0, 0, 1], [3337, 1, 0, 0, 0],
            [3356, 0, 0, 1, 0], [3374, 0, 1, 0, 0], [3392, 0, 0, 0, 1], [3410, 1, 0, 0, 0], [3429, 0, 0, 1, 0],
            [3465, 0, 1, 0, 0], [3502, 0, 1, 0, 0], [3520, 0, 1, 0, 0], [3538, 1, 0, 0, 0], [3557, 0, 0, 1, 0],
            [3575, 0, 1, 0, 0], [3612, 0, 0, 1, 0], [3639, 0, 0, 1, 0], [3666, 1, 0, 0, 0], [3685, 0, 1, 0, 0],
            [3703, 1, 0, 0, 0], [3721, 0, 1, 0, 0], [3758, 0, 0, 0, 1], [3785, 0, 0, 0, 1], [3813, 1, 0, 0, 0],
            [3831, 1, 0, 0, 0], [3849, 1, 0, 0, 0], [3867, 0, 1, 0, 0], [3904, 0, 0, 0, 1], [3940, 0, 0, 1, 0],
            [3959, 0, 1, 0, 0], [3977, 1, 0, 0, 0], [3995, 1, 0, 0, 0], [4014, 0, 1, 0, 0], [4050, 0, 0, 0, 1],
            [4087, 0, 0, 1, 0], [4105, 0, 1, 0, 0], [4123, 0, 0, 0, 1], [4141, 0, 0, 1, 0], [4160, 0, 0, 1, 0],
            [4178, 1, 0, 0, 0], [4197, 1, 0, 0, 0], [4215, 1, 0, 0, 0], [4233, 0, 0, 0, 1], [4270, 1, 0, 0, 0],
            [4288, 0, 1, 0, 0], [4306, 1, 0, 0, 0], [4324, 0, 0, 0, 1], [4343, 1, 0, 0, 0], [4361, 0, 0, 1, 0],
            [4379, 0, 0, 0, 1], [4398, 0, 0, 0, 1], [4416, 1, 0, 0, 0], [4434, 0, 1, 0, 0], [4452, 0, 0, 1, 0],
            [4471, 0, 1, 0, 0], [4489, 0, 1, 0, 0], [4507, 0, 0, 0, 1], [4525, 0, 1, 0, 0], [4544, 1, 0, 0, 0],
            [4562, 0, 1, 0, 0], [4580, 0, 0, 0, 1], [4598, 1, 0, 0, 0], [4617, 0, 0, 1, 0], [4635, 1, 0, 0, 0],
            [4653, 0, 0, 1, 0], [4672, 0, 0, 1, 0], [4690, 0, 1, 0, 0], [4782, 0, 0, 0, 1], [4800, 0, 0, 0, 1],
            [4818, 0, 0, 0, 1], [4836, 0, 0, 1, 0], [4855, 1, 0, 0, 0], [4891, 0, 1, 0, 0], [4910, 0, 1, 0, 0],
            [4928, 0, 0, 0, 1], [4946, 0, 0, 0, 1], [4964, 0, 0, 1, 0], [4983, 1, 0, 0, 0], [5001, 0, 0, 1, 0],
            [5037, 0, 0, 0, 1], [5056, 0, 1, 0, 0], [5074, 0, 0, 1, 0], [5101, 0, 0, 0, 1], [5138, 0, 0, 0, 1],
            [5156, 0, 0, 0, 1], [5174, 0, 0, 0, 1], [5257, 1, 0, 0, 0], [5284, 0, 1, 0, 0], [5321, 0, 1, 0, 0],
            [5331, 1, 0, 0, 0], [5350, 1, 0, 0, 0], [5386, 1, 0, 0, 0], [5404, 0, 1, 0, 0], [5450, 0, 1, 0, 0],
            [5468, 0, 1, 0, 0], [5486, 1, 0, 0, 0], [5505, 0, 1, 0, 0], [5532, 0, 1, 0, 0], [5550, 1, 0, 0, 0],
            [5596, 0, 1, 0, 0], [5614, 0, 1, 0, 0], [5633, 1, 0, 0, 0], [5651, 0, 1, 0, 0], [5678, 1, 0, 0, 0],
            [5697, 0, 0, 0, 1], [5715, 0, 1, 0, 0], [5751, 0, 1, 0, 0], [5770, 0, 1, 0, 0], [5788, 0, 1, 0, 0],
            [5806, 1, 0, 0, 0], [5824, 0, 0, 0, 1], [5843, 1, 0, 0, 0], [5870, 0, 0, 1, 0], [5888, 0, 0, 1, 0],
            [5907, 0, 1, 0, 0], [5925, 0, 0, 1, 0], [5943, 0, 1, 0, 0], [5989, 1, 0, 0, 0], [6007, 0, 1, 0, 0],
            [6025, 0, 0, 0, 1], [6044, 0, 0, 1, 0], [6062, 0, 0, 0, 1], [6135, 0, 0, 0, 1], [6153, 0, 1, 0, 0],
            [6172, 1, 0, 0, 0], [6190, 0, 0, 1, 0], [6208, 1, 0, 0, 0], [6245, 0, 1, 0, 0], [6272, 0, 0, 1, 0],
            [6300, 1, 0, 0, 0], [6318, 0, 1, 0, 0], [6336, 0, 1, 0, 0], [6354, 1, 0, 0, 0], [6391, 1, 0, 0, 0],
            [6409, 0, 1, 0, 0], [6446, 1, 0, 0, 0], [6464, 1, 0, 0, 0], [6482, 0, 1, 0, 0], [6500, 0, 0, 0, 1],
            [6519, 0, 0, 1, 0], [6538, 0, 0, 1, 0], [6556, 1, 0, 0, 0], [6575, 0, 0, 0, 1], [6593, 0, 0, 0, 1],
            [6611, 0, 0, 0, 1], [6620, 1, 0, 0, 0], [6639, 1, 0, 0, 0], [6675, 0, 1, 0, 0], [6694, 1, 0, 0, 0],
            [6712, 1, 0, 0, 0], [6730, 1, 0, 0, 0], [6748, 1, 0, 0, 0], [6767, 0, 1, 0, 0], [6785, 0, 1, 0, 0],
            [6821, 0, 0, 1, 0], [6840, 0, 0, 0, 1], [6858, 0, 0, 0, 1], [6876, 0, 0, 0, 1], [6894, 0, 1, 0, 0],
            [6913, 0, 1, 0, 0], [6931, 1, 0, 0, 0], [6968, 1, 0, 0, 0], [6986, 0, 1, 0, 0], [7004, 1, 0, 0, 0],
            [7022, 0, 0, 0, 1], [7041, 1, 0, 0, 0], [7068, 1, 0, 0, 0], [7086, 1, 0, 0, 0], [7105, 0, 1, 0, 0],
            [7123, 0, 0, 1, 0], [7141, 1, 0, 0, 0], [7159, 0, 0, 1, 0], [7178, 0, 0, 1, 0], [7196, 0, 1, 0, 0],
            [7214, 1, 0, 0, 0], [7232, 0, 0, 1, 0], [7260, 0, 1, 0, 0], [7278, 1, 0, 0, 0], [7296, 0, 1, 0, 0],
            [7315, 0, 1, 0, 0], [7333, 0, 1, 0, 0], [7351, 1, 0, 0, 0], [7369, 0, 1, 0, 0], [7379, 1, 0, 0, 0],
            [7406, 0, 0, 0, 1], [7424, 0, 0, 1, 0], [7442, 0, 0, 0, 1], [7461, 0, 0, 0, 1], [7479, 0, 1, 0, 0],
            [7497, 0, 1, 0, 0], [7516, 0, 0, 0, 1], [7561, 0, 1, 0, 0], [7580, 1, 0, 0, 0], [7598, 0, 1, 0, 0],
            [7616, 1, 0, 0, 0], [7634, 0, 0, 1, 0], [7653, 0, 0, 1, 0], [7671, 0, 0, 0, 1], [7689, 0, 0, 1, 0],
            [7708, 0, 0, 0, 1], [7727, 0, 0, 0, 1], [7745, 0, 0, 0, 1], [7763, 0, 0, 1, 0], [7781, 0, 0, 0, 1],
            [7800, 0, 0, 1, 0], [7818, 0, 0, 0, 1], [7836, 0, 0, 0, 1], [7854, 1, 0, 0, 0], [7873, 1, 0, 0, 0],
            [7891, 1, 0, 0, 0], [7909, 0, 1, 0, 0], [7928, 1, 0, 0, 0], [7946, 0, 1, 0, 0], [7964, 1, 0, 0, 0],
            [7982, 1, 0, 0, 0], [8001, 0, 0, 1, 0], [8019, 0, 0, 0, 1], [8037, 0, 0, 1, 0], [8055, 0, 0, 1, 0],
            [8074, 0, 0, 1, 0], [8092, 0, 0, 1, 0], [8110, 0, 0, 0, 1], [8128, 1, 0, 0, 0], [8147, 0, 1, 0, 0],
            [8165, 1, 0, 0, 0], [8183, 0, 1, 0, 0], [8202, 0, 1, 0, 0], [10000, 0, 0, 0, 0]]
            self.score=0
            self.comble=0
            # pygame.mixer.music.play()
            # self.stop()
            # print(self.status)
            self.status= Status.stop

        def create_blocks(self):
            if self.theline[0][0] <= self.thetime:
                if self.theline[0][1] == 1:
                    first = FirstLine(self)
                    self.realfirst.append(first)
                if self.theline[0][2] == 1:
                    second = SecondLine(self)
                    self.realsecond.append(second)
                if self.theline[0][3] == 1:
                    third = ThirdLine(self)
                    self.realthird.append(third)
                if self.theline[0][4] == 1:
                    fourth = FourthLine(self)
                    self.realfourth.append(fourth)
                self.theline.remove(self.theline[0])
                self.realblocks = self.realfirst + self.realsecond + self.realthird + self.realfourth

        def drop(self, screen):
            screen.blit(self.background, (0, 0))
            for block in self.realblocks:
                if block.y >= 700:
                    block.life = False
                    self.comble = 0
                    self.realblocks.remove(block)
                    if block.x == 200:
                        del (self.realfirst[0])
                    elif block.x == 476:
                        del (self.realsecond[0])
                    elif block.x == 754:
                        del (self.realthird[0])
                    elif block.x == 1030:
                        del (self.realfourth[0])
                else:
                    block.y += 4 * self.a
                    screen.blit(block.Draw(), (block.PostX(), block.PostY()))

        def intro(self, screen):
            screen.blit(self.background, (0, 0))
            screen.blit(self.play_button.image, self.play_button.rect.topleft)

        def stop(self, screen):
            if self.stop_time >= 154:
                # print(self.status)
                self.status = Status.main
            if 50 >= self.stop_time > 0:
                screen.blit(self.background, (0, 0))
                screen.blit(self.stop3, (250, 150))
            if 100 >= self.stop_time > 50:
                screen.blit(self.background, (0, 0))
                screen.blit(self.stop2, (250, 150))
            if 150 > self.stop_time > 100:
                screen.blit(self.background, (0, 0))
                screen.blit(self.stop1, (250, 150))
            self.stop_time += 1

        def main(self, screen, st):
            # self.a = self.clock.get_time()/20
            if not self.playing:
                if renpy.music.is_playing():
                    renpy.music.stop()
                renpy.play('./audio/JayZhou.mp3', channel='music')
                self.playing = True

            self.a = 100.0
            self.thetime += self.a
            # print(self.thetime)
            # 判断歌曲是否结束
            if self.thetime >= 8410:
                renpy.music.stop()
                self.status = Status.gameover
            
            self.create_blocks()
            self.drop(screen)
            self.draw_text("Score:" + str(self.score), WHITE, 1050, 30, 40, screen)
            if self.comble >= 3:
                self.draw_text("Comble " + str(self.comble), BLUE, 1050 / 2, 30, 40, screen)

        def gameover(self, screen):
            # 生成分数
            if self.playing == True:
                self.playing = False
                # text = self.font.render("Your Score is:"+str(self.score), True, BLACK)
                self.score_text = Text("Your Score is:"+str(self.score))
                self.restart_button = Button(10, self.SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, "END", 30)
                # text_rect = text.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2-40))
            
            screen.blit(self.background1, (0, 0))
            screen.blit(self.restart_button.image, self.restart_button.rect.topleft)
            screen.place(self.score_text, self.SCREEN_WIDTH / 2, (self.SCREEN_HEIGHT / 2)-40)
            # print(self.restart_button.rect)
            

        def get_file(self, path):
            return renpy.file(path)

screen musicgame():
    add MinigameMusicgame()