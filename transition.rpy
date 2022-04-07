# 一些有用的转场，主要来自官方教程
# 记得复制遮障图片

# 图片类，从图片中白色区域向黑色区域溶解
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8,inverse=True)
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define dream = ImageDissolve("imagedissolve dream.png", 2.0, 64)
define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)

# 渐变类
define fadewhite = Fade(3.0,  0.0,  0.5,  color =  "#000")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

 