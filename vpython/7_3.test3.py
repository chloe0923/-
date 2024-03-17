"""
黑洞不會動
恆星的小球被黑洞拉走
pip3 install vpython
"""
from vpython import *
#from astropy.constants import G
import math 
import random

"""
 1. 參數設定, 設定變數及初始值
"""
size = 5             # 小球半徑
R = 20*size          # 圓周運動半徑
#g = 9.8                # 重力加速度 9.8 m/s^2
ratio = 0.1           # 速度, 加速度箭頭長度與實際的比例
t = 0                 # 時間
dt = 0.0000001           # 時間間隔, 取 0.0001 以降低誤差
starM = 3e+14             #kg
black_holeM = 3e+23
G=6.67e-11



"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=600, height=600, x=0, y=0, background=color.black)

layer2_R = 100        #m
g = G*starM/(layer2_R**2) #m/s^2

#v0 = 1*sqrt(g*layer2_R)      # 小球初速, 1 ~ 7 sqrt(g*R)
balls_list = []
for _ in range(10):
    # https://zh.wikipedia.org/wiki/%E7%90%83%E5%BA%A7%E6%A8%99%E7%B3%BB#%E7%9B%B4%E8%A7%92%E5%BA%A7%E6%A8%99%E7%B3%BB
    theta = random.random()*2*math.pi
    phi = random.random()*2*math.pi
    layer2_pos = vec(layer2_R*math.sin(theta)*math.cos(phi), layer2_R*math.sin(theta)*math.sin(phi), layer2_R*math.cos(theta))
    layer2_plane_pos = vec(random.random(), random.random(), 0)
    layer2_d = layer2_pos.x**2+layer2_pos.y**2+layer2_pos.z**2
    layer2_plane_pos.z = (layer2_d-layer2_plane_pos.x*layer2_pos.x-layer2_plane_pos.y*layer2_pos.y)/layer2_pos.z
    v0=(layer2_plane_pos-layer2_pos)
    v0=v0/v0.mag*sqrt(g*layer2_R)
    balls_list.append(sphere(pos=layer2_pos, radius=0.5*size, make_trail=True, retain=100000, v=v0, texture = textures.wood_old, R = layer2_R))

black_hole = ring(pos = vec(300, 0, 0), radius = 30, thickness = 10, color = color.red, emissive = True, M = black_holeM)
center = sphere(pos=vec(0, 0, 0), axis=vec(0, 0, 2*size), radius=3*size, texture = textures.metal, emissive=True, M = starM)



"""
rope = cylinder(pos=vec(0, 0, 0), axis=ball.pos, radius=0.1*size, color=color.yellow)
"""

"""
axis_size = 60

arrow_x = arrow(pos = vec(0, 0, 0), axis = vec(axis_size, 0, 0), radius = 0.1, color = color.red)

arrow_y = arrow(pos = vec(0, 0, 0), axis = vec(0, axis_size, 0), radius = 0.1, color = color.green)

arrow_z = arrow(pos = vec(0, 0, 0), axis = vec(0, 0, axis_size), radius = 0.1, color = color.blue)
"""

"""
b3arrow_v = arrow(pos=ball3.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.green)
b3arrow_a = arrow(pos=ball3.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.blue)
b3gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i>(s)",
           ytitle="green: <i>v</i>(m/s), red: <i>a<sub>t</sub></i>(m/s<sup>2</sup>), blue: <i>a<sub>n</sub></i>(m/s<sup>2</sup>)")
b3_b3vt_plot = gcurve(graph=b3gd, color=color.green)
b3_b3at_plot = gcurve(graph=b3gd, color=color.red)
b3_b3an_plot = gcurve(graph=b3gd, color=color.blue)
"""

"""
 3. 自訂函式, findan 計算法線加速度, findat 計算切線加速度
"""

def findBallAn(ball):
    an = -ball.v.mag2 / ball.R * ball.pos.norm()
    return an
"""
def findat(pos):
    x = pos.x
    y = pos.y
    z = pos.z
    r = sqrt(x**2 + y**2+z**2)
    sintheta = abs(x)/r
    costheta = abs(y)/r
    absat = g*sintheta
    aty = -absat*sintheta
    if((x <= 0 and y <= 0) or (x >=0 and y>= 0)):
        atx = +absat*costheta
    elif((x <= 0 and y >= 0) or (x >= 0 and y <= 0)):
        atx = -absat*costheta
    at = vec(atx, aty, 0)
    return at
"""

"""
 4. 物體運動部分, 小球回到出發點 5 次停止運作
"""

i = 0                 # 小球回到出發點的次數
while(i < 5):
    # 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(5000)
    # 移除離黑洞過近的小球
    balls_list_new = []
    for ball in balls_list:
        black_dis_vec = ball.pos-black_hole.pos
        if black_dis_vec.mag > black_hole.radius:
            balls_list_new.append(ball)
        else:
            ball.visible = False
            del ball
    balls_list = balls_list_new
    # 計算小球 an 更新加速度, 速度, 位置
    for ball in balls_list:
        """
        ball.a = findBallAn(ball)
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        """
        star_a = -G*center.M/(ball.pos.mag2)*ball.pos.norm()
        black_dis_vec = ball.pos-black_hole.pos
        black_hole_a = -G*black_hole.M/(black_dis_vec.mag2)*black_dis_vec.norm() 
        ball.a = star_a + black_hole_a
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        
        
    # 更新時間
    t += dt