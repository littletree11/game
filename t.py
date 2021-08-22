# class a(object):
#   def __init__(self):
#    self.a = 1
#    self.b = [0, self.a]
#   def add(self):
#    self.b[1] += 10

# test = a()
# test.add()
# print(test.b, test.a)

class a(object):
  time = 0
  def __init__(self):
    self.t = 1
    print('a')
  def pp(self):
    print('a_p')

class b(a):
  def __init__(self):
    print('b')
  def pp(self):
    print('b_p')

class c(a):
    def __init__(self):
      print('c')
      super().__init__()
    def pp(self):
      print('c_p')
      super().pp()

a1 = a()
b1 = b()
c1 = c()
a1.pp()
b1.pp()
c1.pp()
